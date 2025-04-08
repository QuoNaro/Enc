import axios from "axios";

// Создаем экземпляр Axios
const apiClient = axios.create({
  baseURL: "http://localhost:8000", // Базовый URL вашего API
  timeout: 5000, // Опциональный таймаут
});

let routerInstance = null;

// Метод для установки экземпляра Vue Router
export function setRouter(router) {
  routerInstance = router;
}

// Интерцептор для запросов: проверка токена и перенаправление
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");

    // Если токен отсутствует и есть экземпляр Vue Router, выполняем перенаправление
    if (!token && routerInstance) {
      routerInstance.push({ name: "UserAuth" }); // Перенаправление на страницу аутентификации
      return Promise.reject(new Error("Unauthorized")); // Отклоняем запрос
    }

    // Если токен существует, добавляем его в заголовок Authorization
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Интерцептор для ответов: обработка ошибок (например, истекший токен)
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Если получена ошибка 401 (неавторизован), выполняем действия
    if (error.response && error.response.status === 401) {
      // Удаляем токен из localStorage
      localStorage.removeItem("token");

      // Если есть экземпляр Vue Router, выполняем перенаправление
      if (routerInstance) {
        routerInstance.push({ name: "UserAuth" });
      }
    }

    return Promise.reject(error);
  }
);

export default apiClient;