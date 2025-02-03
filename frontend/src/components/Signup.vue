<template>
  <div class="signup-container">
    <h1>Signup</h1>
    <form @submit.prevent="handleSignup">
      <input
        type="text"
        v-model="username"
        placeholder="Username"
        required
      />
      <input
        type="email"
        v-model="email"
        placeholder="Email"
        required
      />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
      />
      <button type="submit">Signup</button>
    </form>
    <p v-if="message" :class="success ? 'success-message' : 'error'">{{ message }}</p>
  </div>
</template>

<script>
import { register } from '@/services/AuthAPI'; // Импортируем функцию register

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      message: "",
      success: false,
    };
  },
  methods: {
    async handleSignup() {
      // Валидация данных
      if (!this.username || !this.email || !this.password) {
        this.message = "All fields are required.";
        this.success = false;
        return;
      }
      if (this.password.length < 6) {
        this.message = "Password must be at least 6 characters long.";
        this.success = false;
        return;
      }
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(this.email)) {
        this.message = "Invalid email format.";
        this.success = false;
        return;
      }

      try {
        // Формируем данные для отправки
        await register(this.username, this.email, this.password); // Передаём все три поля
        this.message = "Signup successful!";
        this.success = true;
      } catch (error) {
        this.message = error.message || "An error occurred during signup.";
        this.success = false;
        console.error("Error during signup:", error);
      }
    },
  },
};
</script>

<style scoped>
.signup-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: center;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

input {
  display: block;
  width: 100%;
  padding: 8px;
  margin: 10px 0;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

button {
  padding: 10px;
  width: 100%;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #45a049;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}

.success-message {
  color: green;
  font-size: 14px;
  margin-top: 10px;
}
</style>