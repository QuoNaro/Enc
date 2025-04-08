// notificationService.js
import { createApp } from "vue";
import AppNotification from "@/components/ExtraModules/AppNotification.vue";

export default {
  notificationQueue: [], // Список активных уведомлений

  showNotification(type, message, delay = 5000) {
    if (!["error", "warn", "info"].includes(type)) {
      console.error(`Unknown notification type: ${type}`);
      return;
    }

    // Создаем новый экземпляр компонента
    const app = createApp(AppNotification, { type, messageText: message });
    const container = document.createElement("div"); // Создаем контейнер для уведомления
    document.body.appendChild(container); // Добавляем контейнер в DOM
    const instance = app.mount(container); // Монтируем компонент в контейнер

    // Удаляем класс hidden после рендера
    setTimeout(() => {
      instance.$el.classList.remove("hidden");
      instance.$el.classList.add("visible");
    }, 10);

    // Добавляем обработчик клика для удаления уведомления
    instance.$el.addEventListener("click", () => {
      this.hideNotification(instance, container);
    });

    // Добавляем новое уведомление в очередь
    this.notificationQueue.push({ instance, container });

    // Запускаем таймер для автоматического скрытия только если delay > 0
    if (delay > 0) {
      this.scheduleHideNotification(instance, container, delay);
    }
  },

  hideNotification(instance, container) {
    if (instance && instance.$el) {
      // Убираем класс visible и добавляем класс hidden для анимации исчезновения
      instance.$el.classList.remove("visible");
      instance.$el.classList.add("hidden");

      // После завершения анимации удаляем компонент из DOM
      setTimeout(() => {
        if (instance && container && container.parentNode) {
          container.parentNode.removeChild(container);
          instance.$destroy?.(); // Уничтожаем Vue-компонент (если метод доступен)
          // Удаляем уведомление из очереди
          this.notificationQueue = this.notificationQueue.filter(
            (item) => item.instance !== instance
          );
        }
      }, 300); // Время анимации transition
    }
  },

  scheduleHideNotification(instance, container, delay = 5000) {
    // Устанавливаем таймер для автоматического скрытия уведомления
    setTimeout(() => {
      if (instance) {
        this.hideNotification(instance, container);
      }
    }, delay);
  },
};