<template>
    <form @submit.prevent="register" class="auth-form">
      <div class="form-group">
        <label for="username">{{ $t('auth.username') }}</label>
        <input 
          required 
          type="text" 
          id="username" 
          v-onlyEng 
          v-model="username" 
          class="form-control"
          @input="debouncedCheckUsername"
        />
        <div v-if="username_error" class="error-message">{{ username_error }}</div>
      </div>
      <div class="form-group">
        <label for="password">{{ $t('auth.password') }}</label>
        <input 
          required 
          type="password" 
          id="password"
          v-password
          v-model="password" 
          class="form-control"
          @input="debouncedInputPassword"
        />
        <ul v-if="password_errors.length > 0" class="error-list">
          <li v-for="(error, index) in password_errors" :key="index" class="error-item">
            {{ error.message }}
          </li>
        </ul>
      </div>
      <button :disabled="isButtonDisabled" type="submit" class="btn btn-primary submit-button">{{ $t('auth.register') }}</button>
    </form>
</template>
  
  <script>
  import apiClient from '@/utils/api';
  import vp from '@/utils/validatePassword';
  import debounce from '@/utils/debounce';

  export default {
    name: 'SignUpForm',
    data() {
      return {
        username: '',
        username_error: '',
        password: '',
        password_errors: [],
      };
    },
    methods: {
      async checkUsername() {
        if (this.username === '') {
          this.username_error = '';
          return;
        }
        try {
          const response = await apiClient.get(`/check_username/?username=${this.username}`);
          if (!response.data.available) {
            this.username_error = this.$t('auth.error.auth.USER-001');
          } else {
            this.username_error = '';
          }
        } catch (error) {
          console.error('Ошибка при проверке имени пользователя:', error);
          this.username_error = 'Произошла ошибка при проверке.';
        }
      },
      async inputPassword() {
        try {
          if (this.password.trim() !== "") {
            this.password_errors = vp.validatePassword(this.password, this.$appSettings) || [];
          } else {
            this.password_errors = []; // Очистите ошибки, если поле пустое
          }
        } catch (error) {
          console.error(error);
        }
      },
      async register() {
        try {
          let response = await apiClient.post('/register', {
            username: this.username,
            password: this.password,
          });
          if (typeof localStorage !== 'undefined') {
            localStorage.setItem('token', response.data.access_token);
            this.$router.push('/');
          } else {
            console.error('localStorage is not available');
          }
        } catch (error) {
          this.password_errors = error.response.data.detail;
        }
      },
    },
    created() {
      this.debouncedCheckUsername = debounce(this.checkUsername, 1000);
      this.debouncedInputPassword = debounce(this.inputPassword, 1000);
    },
    computed: {
      isButtonDisabled() {
        return (
          this.username.trim() === '' || // Логин пустой
          this.password.trim() === '' || // Пароль пустой
          this.password_errors.length > 0 || // Есть ошибки в пароле
          this.username_error !== '' // Есть ошибки в логине
        );
      }
    }
  };
  </script>
  
<style lang="scss" src="@/assets/styles/auth.scss" scoped></style>