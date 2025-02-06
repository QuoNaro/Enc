import Vue from 'vue';
import Router from 'vue-router';
import UserAuth from '@/components/UserAuth.vue';
import NotFound from '@/components/Error/NotFound.vue';

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
    path: '*',
    name: 'NotFound',
    component: NotFound // Компонент для 404 страницы
  }
];

const router = new Router({
  mode: 'history',
  routes
});

// Функция для проверки аутентификации
function isAuthenticated() {
  return localStorage.getItem('token') !== null; // Пример проверки
}

// Глобальный гвард для защиты маршрутов
router.beforeEach((to, from, next) => {
  // Если маршрут не является страницей входа и пользователь не авторизован
  if (to.path !== '/auth' && !isAuthenticated()) {
    next('/auth'); // Перенаправляем на страницу входа
  } else {
    next(); // Разрешаем переход
  }
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Хранилище Encryption';
  next();
});

export default router;
