import Vue from 'vue';
import Router from 'vue-router';
import UserAuth from '@/components/UserAuth.vue';
import NotFound from '@/components/Error/NotFound.vue';
import MyProfile from '@/components/User.vue';
import handleTokenExpiration from '@/services/idleTimer'

Vue.use(Router);

const routes = [
  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuth,
    children: [
      { path: '#signin'},
      { path: '#signup'}
    ]
  },
  {
    path: '/my',
    name: 'MyProfile',
    component: MyProfile,
  },
  {
    path: '*',
    name: 'NotFound',
    component: NotFound // Компонент для 404 страницы
  }
];

const router = new Router({
  mode: 'history',
  routes
});

function isAuthenticated() {
  const token = localStorage.getItem('token');
  if (!token) return false;

  try {
    // Попытка декодировать токен (без валидации подписи)
    const payload = JSON.parse(atob(token.split('.')[1]));
    const expirationTime = payload.exp; // Время истечения токена (в секундах)

    if (expirationTime && Date.now() / 1000 > expirationTime) {
      return false; // Токен истёк
    }

    return true; // Токен действителен
  } catch (error) {
    return false;
  }
}




// Глобальный гвард для защиты маршрутов
router.beforeEach((to, from, next) => {
  if (to.path !== '/auth' && !isAuthenticated()) {
    // Если токен отсутствует или истёк, выполняем специфические действия
    handleTokenExpiration();
    next('/auth'); // Перенаправляем на страницу входа
  } else {
    next(); // Разрешаем переход
  }
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Encryption';
  next();
});

export default router;
