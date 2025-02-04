import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null, // Токен доступа
  }),
  actions: {
    // Сохранение токена
    setToken(token) {
      this.accessToken = token;
    },
    // Очистка токена
    clearToken() {
      this.accessToken = null;
    },
    // Проверка аутентификации
    isAuthenticated() {
      return !!this.accessToken;
    },
  },
});