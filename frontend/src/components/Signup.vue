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
  import authApi from '../api/authAPI';
  
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

  const jsonString = JSON.stringify({
  username: this.username,
  email: this.email,
  password: this.password,
  });

  const response = await axios.post('/signup', jsonString, {
  headers: {
    'Content-Type': 'application/json',
  },
  });
}}}

  

  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>