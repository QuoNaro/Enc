// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Signup from '@/components/Signup.vue';
import { useAuthStore } from '@/stores/authStore';

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true },
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

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore(); // Получаем экземпляр хранилища
  if (to.meta.requiresAuth && !authStore.isAuthenticated()) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;