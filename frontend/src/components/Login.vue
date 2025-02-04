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
import { login } from '@/services/AuthAPI';

export default {
  data() {
    return {
      username: "",
      password: "",
      isLoggingIn: false,
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      this.isLoggingIn = true;
      this.error = null;
      try {
        await login(this.username, this.password);
        this.$router.push("/home");
      } catch (err) {
        this.error = err.message || "An error occurred during login";
      } finally {
        this.isLoggingIn = false;
      }
    },
  },
};
</script>