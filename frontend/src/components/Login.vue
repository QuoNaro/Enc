<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin" v-if="!isLoggingIn">
      <input
        type="text"
        v-model="username"
        placeholder="Username"
        required
        :disabled="isLoggingIn"
      />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
        :disabled="isLoggingIn"
      />
      <button type="submit" :disabled="isLoggingIn">
        {{ isLoggingIn ? "Logging in..." : "Login" }}
      </button>
    </form>
    <div v-else class="loading">Logging in...</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import { login } from '@/services/AuthAPI'; // Импортируем функцию login

export default {
  data() {
    return {
      username: "",
      password: "",
      isLoggingIn: false, // Флаг для отображения состояния загрузки
      error: null, // Переменная для хранения сообщений об ошибках
    };
  },
  methods: {
    async handleLogin() {
      this.isLoggingIn = true; // Включаем индикатор загрузки
      this.error = null; // Сбрасываем предыдущие ошибки
      try {
        await login(this.username, this.password); // Вызываем функцию login из AuthAPI
        this.$router.push("/home"); // Переходим на главную страницу
      } catch (err) {
        // Обработка ошибок
        this.error = err.message || "An error occurred during login";
      } finally {
        this.isLoggingIn = false; // Выключаем индикатор загрузки
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: center;
}
input {
  display: block;
  width: 100%;
  padding: 8px;
  margin: 10px 0;
  box-sizing: border-box;
}
button {
  padding: 10px;
  width: 100%;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
.loading {
  font-size: 16px;
  color: #666;
}
.error {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}
</style>