import Vue from "vue";
import AppNotification from "@/components/AppNotification.vue";

export default {
  notificationQueue: [], // Список активных уведомлений

  showNotification(type, message, delay = 5000) {
    if (!["error", "warn", "info"].includes(type)) {
      console.error(`Unknown notification type: ${type}`);
      return;
    }

    // Создаем новый экземпляр компонента
    const newNotificationInstance = new Vue({
      render: (h) =>
        h(AppNotification, { props: { type, messageText: message } }),
    }).$mount();

    // Добавляем элемент в DOM
    document.body.appendChild(newNotificationInstance.$el);

    // Убедимся, что DOM обновлен перед началом анимации
    newNotificationInstance.$nextTick(() => {
      // Удаляем класс hidden, чтобы подготовить элемент к анимации
      newNotificationInstance.$el.classList.remove("hidden");

      // Используем двойной requestAnimationFrame для гарантии анимации
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          // Добавляем класс visible для запуска анимации
          newNotificationInstance.$el.classList.add("visible");
        });
      });
    });

    // Добавляем новое уведомление в очередь
    this.notificationQueue.push(newNotificationInstance);

    // Запускаем таймер для автоматического скрытия нового уведомления
    this.scheduleHideNotification(newNotificationInstance, delay);
  },

  hideNotification(instance) {
    if (instance && instance.$el) {
      // Убираем класс visible и добавляем класс hidden для анимации исчезновения
      instance.$el.classList.remove("visible");
      instance.$el.classList.add("hidden");

      // После завершения анимации удаляем компонент из DOM
      setTimeout(() => {
        if (instance && instance.$el && instance.$el.parentNode) {
          instance.$el.parentNode.removeChild(instance.$el);
          instance.$destroy(); // Уничтожаем Vue-компонент

          // Удаляем уведомление из очереди
          this.notificationQueue = this.notificationQueue.filter(
            (item) => item !== instance
          );
        }
      }, 300); // Время анимации transition
    }
  },

  scheduleHideNotification(instance, delay = 5000) {
    // Устанавливаем таймер для автоматического скрытия уведомления
    setTimeout(() => {
      if (instance) {
        this.hideNotification(instance);
      }
    }, delay);
  },
};