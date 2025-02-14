// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import i18n from '@/services/i18n';

// Стили
import './assets/colors.css';
import './assets/global.css';



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




new Vue({
  router,
  i18n, // Подключаем i18n к экземпляру Vue
  render: h => h(App),
}).$mount('#app');
