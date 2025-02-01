<template>
    <div>
      <h1>Signup</h1>
      <form @submit.prevent="signup">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Signup</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>

  <script>
  import apiClient from '../api/authAPI'; // Импортируем HTTP-клиент
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        message: '',
      };
    },
    methods: {
      async signup() {
        // Валидация данных
        if (!this.username || !this.email || !this.password) {
          this.message = 'All fields are required.';
          return;
        }
        if (this.password.length < 6) {
          this.message = 'Password must be at least 6 characters long.';
          return;
        }
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(this.email)) {
          this.message = 'Invalid email format.';
          return;
        }
  
        // Формируем данные для отправки
        const requestData = {
          username: this.username,
          email: this.email,
          password: this.password,
        };
  
        try {
          // Отправляем POST-запрос на бэкенд
          const response = await apiClient.post('signup', { json: requestData });
          const responseData = await response.json();
          this.message = 'Signup successful!';
          console.log(responseData);
        } catch (error) {
          // Обработка ошибок
          if (error.response) {
            const errorData = await error.response.json();
            this.message = errorData.message || 'An error occurred during signup.';
          } else {
            this.message = 'Network error or server is unreachable.';
          }
          console.error('Error during signup:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>