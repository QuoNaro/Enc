<template>
    <form @submit.prevent="login" class="auth-form">
      <div class="form-group">
        <label for="username">{{ $t('auth.username') }}</label>
        <input 
          required 
          type="text" 
          id="username" 
          v-model="username" 
          class="form-control">

      </div>
      <div class="form-group">
        <label for="password">{{ $t('auth.password') }}</label>
        <input 
          required 
          type="password" 
          id="password" 
          v-model="password" 
          class="form-control">
      </div>
      <button type="submit" class="btn btn-primary submit-button">{{ $t('auth.login') }}</button>
    </form>
  </template>

<script>
import nt from '@/utils/notificationService';
import apiClient from '@/utils/api';

export default {
    name: 'SignInForm',
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async login() {
            try {
                const params = new URLSearchParams();
                params.append('username', this.username);
                params.append('password', this.password);
                const response = await apiClient.post('/api/v1/token', params);
                if (typeof localStorage !== 'undefined') {
                    localStorage.setItem('token', response.data.access_token);
                    this.$router.push('/');
                }
            } catch (error) {
                nt.showNotification('error', this.$t('auth.error.auth.AUTH-001'), 2000);
            }
        },
    },
};
</script>

<style lang="scss" src="@/assets/styles/auth.scss" scoped></style>
