// i18n.js
import { createI18n } from 'vue-i18n';

// Импортируем файлы локалей
import en from '../locales/en.json';
import ru from '../locales/ru.json';

// Определение поддерживаемых локалей
const supportedLocales = ['en', 'ru'];

// Определение локали пользователя
const userLocale = navigator.language || navigator.userLanguage; // Например, "en-US" или "ru-RU"
const localeCode = userLocale.split('-')[0]; // Извлекаем только код языка ("en", "ru")

// Установка локали по умолчанию (если локаль пользователя не поддерживается)
const defaultLocale = supportedLocales.includes(localeCode) ? localeCode : 'en';

// Создаем экземпляр i18n
const i18n = createI18n({
  legacy: false, // Отключаем режим совместимости с Vue 2
  locale: defaultLocale, // Локаль пользователя или локаль по умолчанию
  fallbackLocale: 'en', // Локаль, если перевод не найден
  messages: {
    en,
    ru,
  },
});

export default i18n;