import Vue from 'vue';
import VueI18n from 'vue-i18n';

// Импортируйте ваши файлы локалей
import en from '../locales/en.json';
import ru from '../locales/ru.json';


// Установите плагин VueI18n
Vue.use(VueI18n);

// Определение поддерживаемых локалей
const supportedLocales = ['en', 'ru'];

// Определение локали пользователя
const userLocale = navigator.language || navigator.userLanguage; // Например, "en-US" или "ru-RU"
const localeCode = userLocale.split('-')[0]; // Извлекаем только код языка ("en", "ru")

// Установка локали по умолчанию (если локаль пользователя не поддерживается)
const defaultLocale = supportedLocales.includes(localeCode) ? localeCode : 'en';

// Создаем экземпляр i18n
const i18n = new VueI18n({
  locale: defaultLocale, // Локаль пользователя или локаль по умолчанию
  fallbackLocale: 'en', // Локаль, если перевод не найден
  messages: {
    en,
    ru,
  },
});

export default i18n;