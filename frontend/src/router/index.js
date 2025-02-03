// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Signup from '@/components/Signup.vue';
import { isAuthenticated } from '@/services/AuthAPI'; // Импортируем функцию проверки аутентификации

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }, // Защищённая страница
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Глобальная навигационная гвардия
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next({ name: 'Login' }); // Редирект на страницу логина
  } else {
    next(); // Продолжить навигацию
  }
});

export default router;