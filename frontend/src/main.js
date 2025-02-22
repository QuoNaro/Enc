// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import i18n from '@/services/i18n';
import { gsap } from "gsap";

// Стили
import './assets/styles/global.css';
import './assets/styles/fonts.css';


Vue.config.productionTip = false;

// Директивы
import onlyEng from '@/directives/login';
import password from '@/directives/password';
Vue.directive('onlyEng', onlyEng);
Vue.directive('password', password);


// Плагины
import formatPlugin from '@/plugins/format'
import settingsPlugin from '@/plugins/settingsPlugin';
Vue.use(settingsPlugin)
Vue.use(formatPlugin)

// Добавление модуля анимаций
Vue.prototype.$gsap = gsap;

new Vue({
  router,
  i18n, // Подключаем i18n к экземпляру Vue
  render: h => h(App),
}).$mount('#app');
