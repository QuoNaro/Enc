<template>
  <div class="language-switcher">
    <!-- Плавающая кнопка -->
    <button class="switcher-button" @click="toggleDropdown" :class="{ active: isDropdownOpen }">
      <span>{{ currentLanguage }}</span>
    </button>

    <!-- Выпадающее меню -->
    <transition name="fade">
      <ul v-if="isDropdownOpen" class="dropdown-menu">
        <li v-for="locale in availableLocales" :key="locale.code" @click="changeLanguage(locale.code)">
          {{ locale.name }}
        </li>
      </ul>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'LanguageSwitcher',
  data() {
    return {
      isDropdownOpen: false, // Состояние выпадающего меню
    };
  },
  computed: {
    // Текущий язык
    currentLanguage() {
      return this.$i18n.locale === 'en' ? 'EN' : 'RU';
    },
    // Доступные языки
    availableLocales() {
      return [
        { code: 'en', name: 'English' },
        { code: 'ru', name: 'Русский' },
      ];
    },
  },
  methods: {
    // Переключение языка
    changeLanguage(locale) {
      if (this.$i18n.locale !== locale) {
        this.$i18n.locale = locale;
      }
      this.isDropdownOpen = false; // Закрываем меню после выбора
    },
    // Открытие/закрытие выпадающего меню
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
  },
};
</script>

<style scoped>
.language-switcher {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

.switcher-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  background-color: #42b983;
  color: white;
  border: none;
  @include border-radius();
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.switcher-button.active {
  transform: scale(1.1);
}

.switcher-button span {
  font-size: 16px;
  font-weight: bold;
}

.dropdown-menu {
  position: absolute;
  top: -60px;
  right: 0;
  background-color: white;
  border: 1px solid #ddd;
  @include border-radius();
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
  padding: 0;
  margin: 0;
  width: 120px;
}

.dropdown-menu li {
  padding: 10px 15px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.dropdown-menu li:hover {
  background-color: #f0f0f0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>