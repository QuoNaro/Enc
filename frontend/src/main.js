// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import i18n from '@/services/i18n';

// Стили
import './assets/styles/global.css';
import './assets/styles/fonts.css';

// Директивы
import onlyEng from '@/directives/login';
import password from '@/directives/password';

// Плагины
import formatPlugin from '@/plugins/format';
import settingsPlugin from '@/plugins/settingsPlugin';

// Анимации
import gsap from 'gsap';

// Создание экземпляра приложения
const app = createApp(App);

// Глобальные директивы
app.directive('onlyEng', onlyEng);
app.directive('password', password);

// Глобальные плагины
app.use(settingsPlugin);
app.use(formatPlugin);

// Подключение роутера и i18n
app.use(router);
app.use(i18n);

// Добавление глобальных свойств
app.config.globalProperties.$gsap = gsap;

// Отключение предупреждений о производстве (в Vue 3 это делается автоматически)
app.config.productionTip = false;

// Монтирование приложения
app.mount('#app');