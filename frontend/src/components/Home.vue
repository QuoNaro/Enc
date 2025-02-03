<template>
  <div class="home">
    <h1>Welcome to the Home Page!</h1>
    <p>This page is accessible only to authenticated users.</p>
    <button @click="fetchProtectedData">Fetch Protected Data</button>
    <button @click="handleLogout">Logout</button>
    <div v-if="protectedData">{{ protectedData }}</div>
  </div>
</template>

<script>
import { logout } from '@/services/AuthAPI'; // Импортируем функцию logout
import apiClient from '@/services/AuthAPI'; // Импортируем глобального клиента ky

export default {
  data() {
    return {
      protectedData: null, // Данные с защищённого эндпоинта
    };
  },
  methods: {
    async fetchProtectedData() {
      try {
        const response = await apiClient.get('/protected-data'); // Токен добавляется автоматически
        this.protectedData = await response.json();
      } catch (error) {
        alert('Failed to fetch protected data.');
      }
    },
    async handleLogout() {
      try {
        await logout(); // Вызываем функцию logout из AuthAPI
        this.$router.push({ name: 'Login' }); // Переходим на страницу входа
      } catch (error) {
        alert('Logout failed.');
      }
    },
  },
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}

h1 {
  font-size: 2.5em;
  color: #42b983;
}

p {
  font-size: 1.2em;
}

button {
  margin: 10px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #369e74;
}
</style>