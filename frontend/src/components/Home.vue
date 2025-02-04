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
import { logout } from '@/services/AuthAPI';
import { getProtectedData } from '@/services/AuthAPI'; // Импортируем функцию getProtectedData

export default {
  data() {
    return {
      protectedData: null,
    };
  },
  methods: {
    async fetchProtectedData() {
      try {
        this.protectedData = await getProtectedData(); // Получаем защищённые данные
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