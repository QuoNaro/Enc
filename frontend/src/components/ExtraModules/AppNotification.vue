<template>
  <div
    class="notification"
    :class="[type, { visible: isVisible, hidden: isHidden }]"
  >
    {{ messageText }}
  </div>
</template>

<script>
export default {
  name: "AppNotification",
  props: {
    type: {
      type: String,
      required: true,
      validator: (value) => ["error", "warn", "info"].includes(value),
    },
    messageText: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      isVisible: false,
      isHidden: true,
    };
  },
};
</script>




<style scoped>
/* Общие стили для всех уведомлений */
.notification {
  position: fixed; /* Фиксированное позиционирование */
  top: 20px; /* Расположение сверху */
  left: 50%; /* Центрирование по горизонтали */
  transform: translateX(-50%) translateY(-20px); /* Центрирование и начальная позиция */
  padding: 10px 20px; /* Внутренние отступы */
  border-radius: 5px; /* Скругление углов */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Тень */
  z-index: 1000; /* Повышенный уровень отображения */
  color: white; /* Белый текст */
  opacity: 0; /* Начальное состояние - невидимый */
  transition: all 0.3s ease; /* Плавная анимация */
}

/* Стили для разных типов уведомлений */
.notification.error {
  background-color: #f44336; /* Красный цвет для ошибок */
}
.notification.warn {
  background-color: #ff9800; /* Оранжевый цвет для предупреждений */
}
.notification.info {
  background-color: #2196f3; /* Синий цвет для информационных сообщений */
}

/* Анимация появления и исчезновения */
.visible {
  opacity: 1; /* Полная видимость */
  transform: translateX(-50%) translateY(0); /* Возвращаем на место */
}
.hidden {
  opacity: 0; /* Снова делаем невидимым */
  transform: translateX(-50%) translateY(-20px); /* Убираем выше экрана */
}
</style>