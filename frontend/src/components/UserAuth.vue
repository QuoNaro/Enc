<template>
    <div>
        <h1>Auth Page</h1>
        <button @click="navigateTo('#signin')">Sign In</button>
        <button @click="navigateTo('#signup')">Sign Up</button>
        <div v-if="currentHash === '#signup'">
            <h2>Register</h2>
            <form @submit.prevent="register">
                <div class="form-group">
                    <label for="username">{{ $t('auth.username') }}</label>
                    <input @input="debouncedCheckUsername" required type="login" v-onlyEng id="username_up" v-model="username_up" class="form-control">
                    <div>
                        

                    </div>
                </div>
                <div class="form-group">
                    <label for="password">{{ $t('auth.password') }}</label>
                    <input @input="debouncedValidatePassword" required type="password" id="password_up" v-model="password_up" class="form-control">
                </div>
                <template v-if="password_errors">
                    <li v-for="(item, index) in password_errors" :key="index">
                        {{ index + 1 }}. {{ item }}
                    </li>
                </template>
                <button :disabled="hasPasswordErrors" type="submit" class="btn btn-primary">Register</button>
            </form>
        </div>
        
        <div v-else-if="currentHash === '#signin'">
            <h2>Login</h2>
            <form @submit.prevent="login">
                <div class="form-group">
                    <label for="username">{{ $t('auth.username') }}</label>
                    
                    <input required type="login" v-onlyEng id="username_in" v-model="username_in" class="form-control">
                    
                </div>
                <div class="form-group">
                    <label for="password">{{ $t('auth.password') }}</label>
                    <input required type="password" id="password_in" v-model="password_in" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
    </div>
</template>

<script>
import nt from '@/services/notificationService';
import apiClient from '@/services/api';
import debounce from '@/services/debounce';

export default {
    name: 'UserAuth',
    
    data() {
        return {
            username_in: '',
            password_in: '',
            username_up: '',
            username_up_error: '',
            password_up: '',
            password_errors: {},
            currentHash: window.location.hash || '#signin',
            hashChangeHandler: null,
        };
    },
    methods: {
       
        async checkUsername() {
            if (this.username_up === '') {
                this.username_up_error = ''; // Очищаем ошибку, если поле пустое
                return;
            }

            try {
                const response = await apiClient.get(`/check_username/?username=${this.username_up}`);
                if (!response.data.available) {
                this.username_up_error = this.$t('auth.error.auth.USER-001');
                } else {
                this.username_up_error = '';
                }
            } 
            catch (error) {
                console.error('Ошибка при проверке имени пользователя:', error);
                this.username_up_error = 'Произошла ошибка при проверке.';
            }
        },


        async validatePassword() {

            try {
                const response = await apiClient.post(`/api/validate-password`,{
                    password : this.password_up
                });
                console.log(response)
            } 
            catch (error) {
                console.log('respo')
               
            }
        },

        
        
        navigateTo(hash) {
            window.location.hash = hash;
            this.currentHash = hash;
        },
        async login() {
            try {
                const params = new URLSearchParams();
                params.append('username', this.username_in);
                params.append('password', this.password_in);

                const response = await apiClient.post('/token', params);
                if (typeof localStorage !== 'undefined') {
                    localStorage.setItem('token', response.data.access_token);
                    
                }
            } catch (error) {
                nt.showNotification('error',this.$t('auth.error.auth.AUTH-001'), 2000);
            }
        },
        async register() {
            try {
                let response = await apiClient.post('/register', {
                    username: this.username_up,
                    password: this.password_up,
                });
                
                if (typeof localStorage !== 'undefined') {
                    localStorage.setItem('token', response.data.access_token);
                    
                }
                
            } catch (error) {
                // Обработка ошибок
                this.password_errors = error.response.data.detail

            }
        },
    },
    mounted() {
        this.changeTitle = () => {
            switch (this.currentHash) {
                case "#signin":
                    document.title = 'Авторизация'; break;    
                case "#signup":
                    document.title = 'Регистрация'; break;
            }
        };

        this.hashChangeHandler = () => {
            this.currentHash = window.location.hash;
            this.changeTitle()
        };

        window.addEventListener('hashchange', this.hashChangeHandler);
    },
    beforeUnmount() {
        if (this.hashChangeHandler) {
            window.removeEventListener('hashchange', this.hashChangeHandler);
        }
    },
    computed: {
        debouncedCheckUsername() {
        return debounce(this.checkUsername, 600); // Задержка 400 мс
        },
        
        debouncedValidatePassword() {
            return debounce(this.validatePassword,500)
        },

        hasPasswordErrors() {
        // Проверяем, что объект не пустой
        return Object.keys(this.password_errors).length > 0;
        },
  }
};
</script>

<style scoped>

</style>