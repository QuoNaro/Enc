// src/AuthAPI.js
import ky from 'ky';

const apiClient = ky.create({
  prefixUrl: 'http://localhost:8000', // Базовый URL бэкенда
  timeout: 10000, // Таймаут запроса (опционально)
  headers: {
    'Content-Type': 'application/json', // Заголовок для JSON
  },
});

export default apiClient;