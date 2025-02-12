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
                    <input type="login" v-onlyEng id="username_up" v-model="username_up" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">{{ $t('auth.password') }}</label>
                    <input type="password" id="password_up" v-model="password_up" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        </div>
        
        <div v-else-if="currentHash === '#signin'">
            <h2>Login</h2>
            <form @submit.prevent="login">
                <div class="form-group">
                    <label for="username">{{ $t('auth.username') }}</label>
                    <input type="login" v-onlyEng id="username_in" v-model="username_in" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">{{ $t('auth.password') }}</label>
                    <input type="password" id="password_in" v-model="password_in" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
    </div>
</template>

<script>
import nt from '@/services/notificationService';


import axios from 'axios';
export default {
    name: 'UserAuth',
    data() {
        return {
            username_in: '',
            password_in: '',
            username_up: '',
            password_up: '',
            currentHash: window.location.hash || '#signin',
            hashChangeHandler: null,
        };
    },
    methods: {
        

        navigateTo(hash) {
            window.location.hash = hash;
            this.currentHash = hash;
        },
        async login() {
            try {
                const params = new URLSearchParams();
                params.append('username', this.username_in);
                params.append('password', this.password_in);

                const response = await axios.post('http://localhost:8000/token', params);
                if (typeof localStorage !== 'undefined') {
                    localStorage.setItem('token', response.data.access_token);
                }
            } catch (error) {
                nt.showNotification('error',this.$t('auth.error.auth.AUTH-001'), 2000);
            }
        },
        async register() {
            try {
                await axios.post('http://localhost:8000/register', {
                    username: this.username_up,
                    password: this.password_up,
                });
                
                this.navigateTo('#signin'); // Перенаправление на форму входа
            } catch (error) {
                let fk = Object.keys(error.response.data.detail)[0];
                let error_message = this.$t(`auth.error.password.${fk}`);
                
                
                 
                   
        
                nt.showNotification('error',error_message, 5000)
            }
        }
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
    }
};
</script>

<style scoped>

</style>