import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './assets/colors.css';
import VueI18n from 'vue-i18n';

Vue.config.productionTip = false;

// Импортируйте ваши файлы локалей
import en from './locales/en.json';
import ru from './locales/ru.json';

Vue.use(VueI18n);

const i18n = new VueI18n({
  locale: 'ru', // Локаль по умолчанию
  fallbackLocale: 'en', // Локаль, если перевод не найден
  messages: {
    en: en,
    ru: ru
  }
});

new Vue({
  router,
  i18n, // Подключаем i18n к экземпляру Vue
  render: h => h(App)
}).$mount('#app');
