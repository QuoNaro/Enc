<template>
    <div>
        <!-- Отображение формы в зависимости от хэша -->
        <component :is="currentComponent" />
    </div>
</template>

<script>
import SignInForm from './SignInForm.vue';
import SignUpForm from './SignUpForm.vue';

export default {
    name: 'UserAuth',
    components: {
        SignInForm,
        SignUpForm,
    },
    data() {
        return {
            currentHash: window.location.hash || '#signin',
            hashChangeHandler: null,
        };
    },
    computed: {
        currentComponent() {
            // Возвращаем компонент в зависимости от хэша
            return this.currentHash === '#signup' ? 'SignUpForm' : 'SignInForm';
        },
    },
    methods: {
        navigateTo(hash) {
            window.location.hash = hash;
            this.currentHash = hash;
        },
    },
    mounted() {
        this.changeTitle = () => {
            switch (this.currentHash) {
                case "#signin":
                    document.title = 'Авторизация';
                    break;
                case "#signup":
                    document.title = 'Регистрация';
                    break;
            }
        };

        this.hashChangeHandler = () => {
            this.currentHash = window.location.hash;
            this.changeTitle();
        };

        window.addEventListener('hashchange', this.hashChangeHandler);
    },
    beforeUnmount() {
        if (this.hashChangeHandler) {
            window.removeEventListener('hashchange', this.hashChangeHandler);
        }
    },
};
</script>

<style scoped>
</style>