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
  import axios from 'axios';
  
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
                const response = await axios.post('http://localhost:8000/my', {}, { // Пустой объект для body
                headers: {
                    Authorization: `Bearer ${this.token}`, // Заголовок должен быть здесь
                },
                });
                console.log(response.data)
                this.user = response.data; // Сохраняем данные пользователя
            } catch (error) {
                this.$router.push({ name: 'UserAuth' })
            }
            }
    },
  };
  </script>