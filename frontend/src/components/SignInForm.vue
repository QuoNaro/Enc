<template>
    <div>
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
</template>

<script>
import nt from '@/services/notificationService';
import apiClient from '@/services/api';

export default {
    name: 'SignInForm',
    data() {
        return {
            username_in: '',
            password_in: '',
        };
    },
    methods: {
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
                nt.showNotification('error', this.$t('auth.error.auth.AUTH-001'), 2000);
            }
        },
    },
};
</script>

<style scoped>
</style>