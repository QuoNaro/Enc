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




<style lang="scss" scoped>
// Определение переменных для цветов
$color-error: #f44336; // Красный цвет для ошибок
$color-warn: #ff9800;  // Оранжевый цвет для предупреждений
$color-info: #2196f3;  // Синий цвет для информационных сообщений

.notification {
  
  // Общие стили для всех уведомлений
  position: fixed;
  top: 20px;
  left: 50%;
  font-family: 'Arimo';
  transform: translateX(-50%) translateY(-20px);
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  z-index: 1000;
  color: white;
  opacity: 0;
  transition: all 0.3s ease;

  // Стили для разных типов уведомлений
  &.error {
    background-color: $color-error;
  }

  &.warn {
    background-color: $color-warn;
  }

  &.info {
    background-color: $color-info;
  }

  // Анимация появления и исчезновения
  &.visible {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }

  &.hidden {
    opacity: 0;
    transform: translateX(-50%) translateY(-20px);
  }
}


</style>