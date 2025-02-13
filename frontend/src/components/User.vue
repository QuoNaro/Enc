<template>
    <div v-if="user">
      <h1>Профиль пользователя</h1>
      <p><strong>Имя пользователя:</strong> {{ user.username }}</p>
    </div>
    <div v-else>
      <p>Загрузка...</p>
    </div>
  </template>
  
  <script>
  import apiClient from '@/services/api';
  
  export default {
    name : "MyProfile",
    data() {
      return {
        user: null,
        token: '', // Токен должен быть получен при входе в систему
      };
    },
    created() {
      this.token = localStorage.getItem('token'); // Получаем токен из локального хранилища
      this.fetchUserProfile();
    },
    methods: {
        async fetchUserProfile() {
            try {
                const response = await apiClient.post('/my');
                this.user = response.data;
            } catch (error) {
                this.$router.push({ name: 'UserAuth' })
            }
            }
    },
  };
  </script>