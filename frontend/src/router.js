import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import Signup from '@/components/Signup.vue';

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta : {requiresAuth : true},
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    
  },
  {
    path: '/signup', 
    component: Signup,
    name: 'Signup', 
  },
];



const router = createRouter({
  history: createWebHistory(),
  routes,
});

const isAuthenticated = false; // Здесь должна быть ваша логика проверки аутентификации

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' }); // Редирект на страницу логина
  } else {
    next(); // Продолжить навигацию
  }
});

export default router;

