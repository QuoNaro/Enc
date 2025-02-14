<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="register">
            <div class="form-group">
                <label for="username">{{ $t('auth.username') }}</label>
                <input @input="debouncedCheckUsername" required type="login" v-onlyEng id="username_up" v-model="username_up" class="form-control">
                <div>{{ username_up_error }}</div>
            </div>
            <div class="form-group">
                <label for="password">{{ $t('auth.password') }}</label>
                <input @input="debouncedValidatePassword" required type="password" id="password_up" v-onlyEng v-model="password_up" class="form-control">
            </div>
            <template v-if="password_errors">
                <li v-for="(item) in password_errors" :key="item">
                    {{ item }}
                </li>
            </template>
            <button :disabled="hasPasswordErrors" type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</template>

<script>

import apiClient from '@/services/api';
import debounce from '@/services/debounce';

export default {
    name: 'SignUpForm',
    data() {
        return {
            username_up: '',
            username_up_error: '',
            password_up: '',
            password_errors: {},
        };
    },
    methods: {
        async checkUsername() {
            if (this.username_up === '') {
                this.username_up_error = '';
                return;
            }
            try {
                const response = await apiClient.get(`/check_username/?username=${this.username_up}`);
                if (!response.data.available) {
                    this.username_up_error = this.$t('auth.error.auth.USER-001');
                } else {
                    this.username_up_error = '';
                }
            } catch (error) {
                console.error('Ошибка при проверке имени пользователя:', error);
                this.username_up_error = 'Произошла ошибка при проверке.';
            }
        },
        
        async validatePassword() {
            try {
                if (this.password_up.trim() != "") {
                    const response = await apiClient.post(`/api/validate-password`, {password: this.password_up});
                    if (!response.data.is_valid) {
                        this.password_errors = Object.values(response.data.errors)
                    }
                }
                
            } catch (error) {
                console.error(error)
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
                this.password_errors = error.response.data.detail;
            }
        },
    },
    computed: {
        debouncedCheckUsername() {
            return debounce(this.checkUsername, 1000);
        },
        debouncedValidatePassword() {
            return debounce(this.validatePassword, 1000);
        },
        hasPasswordErrors() {
            return Object.keys(this.password_errors).length > 0;
        },
    },
};
</script>

<style scoped>
</style>