from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64

class RSACryptography:
    def __init__(self, key_size=2048):
        """
        Инициализация класса RSACryptography.
        
        :param key_size: Размер ключа (по умолчанию 2048 бит).
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_key_path="private_key.pem", public_key_path="public_key.pem"):
        """
        Сохранение приватного и публичного ключей в файлы.
        
        :param private_key_path: Путь к файлу для сохранения приватного ключа.
        :param public_key_path: Путь к файлу для сохранения публичного ключа.
        """
        # Сохранение приватного ключа
        with open(private_key_path, "wb") as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Сохранение публичного ключа
        with open(public_key_path, "wb") as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def load_keys(self, private_key_path="private_key.pem", public_key_path="public_key.pem"):
        """
        Загрузка приватного и публичного ключей из файлов.
        
        :param private_key_path: Путь к файлу с приватным ключом.
        :param public_key_path: Путь к файлу с публичным ключом.
        """
        # Загрузка приватного ключа
        with open(private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        # Загрузка публичного ключа
        with open(public_key_path, "rb") as f:
            self.public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

    def encrypt(self, data):
        """
        Шифрование данных с использованием публичного ключа и возврат результата в виде Base64-строки.
        
        :param data: Данные для шифрования (в виде строки или bytes).
        :return: Зашифрованные данные в виде Base64-строки.
        """
        if isinstance(data, str):
            data = data.encode('utf-8')  # Преобразование строки в bytes
        
        if not isinstance(data, bytes):
            raise ValueError("Данные должны быть в формате строки или bytes.")
        
        encrypted_data = self.public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted_data).decode('utf-8')  # Возвращаем Base64-строку

    def decrypt(self, encrypted_data_base64):
        """
        Дешифрование данных из Base64-строки с использованием приватного ключа.
        
        :param encrypted_data_base64: Зашифрованные данные в виде Base64-строки.
        :return: Расшифрованные данные в виде строки.
        """
        if not isinstance(encrypted_data_base64, str):
            raise ValueError("Зашифрованные данные должны быть в формате Base64-строки.")
        
        encrypted_data = base64.b64decode(encrypted_data_base64)  # Декодирование Base64
        decrypted_data = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data.decode('utf-8')  # Возвращаем строку
