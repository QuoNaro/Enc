// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './assets/colors.css';
import './assets/global.css';
import onlyEng from '@/directives/onlyEng';
import i18n from '@/services/i18n'; // Импортируем i18n
import idleTimer from './services/idleTimer';

Vue.config.productionTip = false;

// Директивы
Vue.directive('onlyEng', onlyEng);



new Vue({
  router,
  i18n, // Подключаем i18n к экземпляру Vue
  render: h => h(App),
}).$mount('#app');

// Время простоя пользователя
idleTimer.init();