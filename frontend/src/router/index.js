import Vue from 'vue';
import Router from 'vue-router';
import UserAuth from '@/components/UserAuth.vue';
import NotFound from '@/components/Error/NotFound.vue';
import nt from '@/services/notificationService'
import i18n from '@/services/i18n';

Vue.use(Router);

const routes = [
  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuth,
    children: [
      { path: '#signin' },
      { path: '#signup' }
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
  const token = localStorage.getItem('token');
  if (!token) return false;

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    const expirationTime = payload.exp; // Время истечения токена (в секундах)

    if (expirationTime && Date.now() / 1000 > expirationTime) {
      return false;
    }

    return true; // Токен действителен
  } catch (error) {
    return false; // Ошибка при разборе токена
  }
}

// Глобальный гвард для защиты маршрутов
router.beforeEach((to, from, next) => {
  // Проверяем, авторизован ли пользователь
  if (to.path !== '/auth' && !isAuthenticated()) {
    // Если токен истёк, показываем уведомление
    if (localStorage.getItem('token')) {
      nt.showNotification('info', i18n.t('auth.error.auth.TOKEN-001'), 15000); // Показываем уведомление
    }
    next('/auth'); // Перенаправляем на страницу аутентификации
    localStorage.removeItem('token')
    return;
  }

  // Обновляем заголовок страницы
  document.title = to.meta.title || 'Encryption';

  next(); // Разрешаем переход
});

export default router;