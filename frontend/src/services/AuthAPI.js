// src/services/AuthAPI.js
import ky from 'ky';

// Создание экземпляра ky с базовыми настройками
const apiClient = ky.create({
  prefixUrl: 'http://localhost:8000', // Базовый URL бэкенда
  timeout: 10000, // Таймаут запроса (опционально)
  hooks: {
    beforeRequest: [
      (request) => {
        // Добавляем токен в заголовок Authorization, если он существует
        const token = localStorage.getItem('access_token');
        if (token) {
          request.headers.set('Authorization', `Bearer ${token}`);
        }
      },
    ],
    afterResponse: [
      async (request, response) => {
        // Обработка ошибок аутентификации (например, истекший токен)
        if (response.status === 401) {
          // Удаляем токен из localStorage при получении ошибки 401
          localStorage.removeItem('access_token');
          // Редирект на страницу входа
          window.location.href = '/login';
        }
        return response;
      },
    ],
  },
});

/**
 * Регистрация нового пользователя
 */
export async function register(username, email, password) {
  try {
    const response = await apiClient.post('signup', {
      json: { username, email, password }, // Отправляем все три поля
    });

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Registration failed:', error.message || error.response.body);
    throw error;
  }
}

/**
 * Авторизация пользователя
 */
export async function login(username, password) {
  try {
    const response = await apiClient.post('login', { // Убран слеш перед 'login'
      json: { username, password },
    });

    const data = await response.json();
    const accessToken = data.access_token;

    localStorage.setItem('access_token', accessToken);
    return data;
  } catch (error) {
    console.error('Login failed:', error.message || error.response.body);
    throw error;
  }
}

/**
 * Выход из аккаунта
 */
export async function logout() {
  try {
    await apiClient.post('logout'); // Убран слеш перед 'logout'
    localStorage.removeItem('access_token');
    return true;
  } catch (error) {
    console.error('Logout failed:', error.message || error.response.body);
    throw error;
  }
}

/**
 * Проверка аутентификации
 */
export function isAuthenticated() {
  return !!localStorage.getItem('access_token'); // Проверяем наличие токена
}

// Экспорт клиента для других запросов
export default apiClient;