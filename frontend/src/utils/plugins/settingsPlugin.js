// plugins/settingsPlugin.js
import apiClient from '@/utils/api';

export default {
  install(app) {
    // Функция для загрузки настроек
    async function loadSettings() {
      let appSettings = null;

      // Проверяем localStorage
      if (typeof window !== 'undefined') {
        const storedSettings = localStorage.getItem('appSettings');
        if (storedSettings) {
          try {
            appSettings = JSON.parse(storedSettings);
          } catch (e) {
            console.error('Ошибка при импорте настроек:', e);
          }
        }
      }

      // Если настроек нет в localStorage, загружаем с сервера
      if (!appSettings) {
        try {
          const response = await apiClient.get('/api/v1/get-password-settings');
          appSettings = response.data;

          // Сохраняем настройки в localStorage
          if (typeof window !== 'undefined') {
            localStorage.setItem('appSettings', JSON.stringify(appSettings));
          }
        } catch (error) {
          console.error('Не удалось получить настройки с сервера:', error);
        }
      }

      // Добавляем настройки в глобальные свойства Vue
      app.config.globalProperties.$appSettings = appSettings;
    }

    // Вызываем функцию загрузки настроек
    loadSettings();
  },
};