<template>
    <div>
        <h1>Auth Page</h1>
        <button @click="navigateTo('#signin')">Sign In</button>
        <button @click="navigateTo('#signup')">Sign Up</button>

        <div v-if="currentHash === '#signup'">
            <h2>Register</h2>
            <form @submit.prevent="register">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username_up" v-model="username_up" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password_up" v-model="password_up" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Register</button>
            </form>
        </div>

        <div v-else-if="currentHash === '#signin'">
            <h2>Login</h2>
            <form @submit.prevent="login">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username_in" v-model="username_in" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password_in" v-model="password_in" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
    </div>
</template>

<script>
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
                } else {
                    console.warn('LocalStorage is not available');
                }
            } catch (error) {
                console.error(error);
            }
        },
        async register() {
            try {
                const response = await axios.post('http://localhost:8000/register', {
                    username: this.username_up,
                    password: this.password_up,
                }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
                this.navigateTo('#signin'); // Перенаправление на форму входа
            } catch (error) {
                console.error(error);
            }
        }
    },
    mounted() {
        this.hashChangeHandler = () => {
            this.currentHash = window.location.hash;
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
.form-group {
    margin-bottom: 1rem;
}

.form-control {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.btn {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.btn:hover {
    background-color: #0056b3;
}
</style>