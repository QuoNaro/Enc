from sqlalchemy.types import TypeDecorator, LargeBinary
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import os
import json
from settings import AppSettings



class EncryptedJSON(TypeDecorator):
    impl = LargeBinary
    cache_ok = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret_key = None

    def _get_derived_key(self):
        """Получаем ключ из SECRET_KEY через HKDF"""
        if not self.secret_key:
            secret_key = AppSettings().secret_key
            
            hkdf = HKDF(
                algorithm=hashes.SHA256(),
                length=32,  # 256-bit ключ для AES-256-GCM
                salt=None,
                info=b'aes-gcm-encryption',
                backend=default_backend()
            )
            self.secret_key = hkdf.derive(secret_key)
        
        return self.secret_key

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        key = self._get_derived_key()
        nonce = os.urandom(12)  # 96-bit nonce
        
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Шифруем JSON
        ciphertext = encryptor.update(json.dumps(value).encode()) + encryptor.finalize()
        
        # Сохраняем nonce(12) + ciphertext + tag(16)
        return nonce + ciphertext + encryptor.tag

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        key = self._get_derived_key()
        nonce = value[:12]
        tag = value[-16:]
        ciphertext = value[12:-16]

        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Расшифровываем
        decrypted = decryptor.update(ciphertext) + decryptor.finalize()
        return json.loads(decrypted.decode())