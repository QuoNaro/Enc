// main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './assets/colors.css';
import './assets/global.css';
import onlyEng from '@/directives/onlyEng';
import settingsPlugin from '@/plugins/settingsPlugin';
import i18n from '@/services/i18n';
import formatPlugin from '@/plugins/format'


Vue.config.productionTip = false;

// Директивы
Vue.directive('onlyEng', onlyEng);

// Плагины
Vue.use(settingsPlugin)
Vue.use(formatPlugin)


new Vue({
  router,
  i18n, // Подключаем i18n к экземпляру Vue
  render: h => h(App),
}).$mount('#app');
