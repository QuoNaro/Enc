import ky from 'ky';
import { useAuthStore } from '@/stores/authStore'; // Импортируем хранилище Pinia

// Создание экземпляра ky с базовыми настройками
const apiClient = ky.create({
  prefixUrl: 'http://localhost:8000',
  timeout: 10000,
  hooks: {
    beforeRequest: [
      (request) => {
        const authStore = useAuthStore(); // Получаем экземпляр хранилища
        if (authStore.accessToken) {
          request.headers.set('Authorization', `Bearer ${authStore.accessToken}`);
        }
      },
    ],
    afterResponse: [
      async (request, response) => {
        if (response.status === 401) {
          const authStore = useAuthStore(); // Получаем экземпляр хранилища
          authStore.clearToken(); // Очищаем токен
          window.location.href = '/login'; // Перенаправляем на страницу входа
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
      json: { username, email, password },
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
    const response = await apiClient.post('login', {
      json: { username, password },
    });

    const data = await response.json();
    const accessToken = data.access_token;

    if (!accessToken) {
      throw new Error("Access token not found in the response.");
    }

    const authStore = useAuthStore(); // Получаем экземпляр хранилища
    authStore.setToken(accessToken); // Сохраняем токен в Pinia

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
    await apiClient.post('logout'); // Отправляем запрос на выход
    const authStore = useAuthStore(); // Получаем экземпляр хранилища
    authStore.clearToken(); // Очищаем токен
    return true;
  } catch (error) {
    console.error('Logout failed:', error.message || error.response.body);
    throw error;
  }
}

/**
 * Получение защищённых данных
 */
export async function getProtectedData() {
  try {
    const response = await apiClient.get('protected-data'); // Токен добавляется автоматически
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch protected data:', error.message || error.response.body);
    throw error;
  }
}  