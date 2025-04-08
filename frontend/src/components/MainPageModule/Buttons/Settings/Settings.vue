<template>
  <div class="settings-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <h2>{{ $t('buttons.settings') }}</h2>
      <ul>
        <li 
          v-for="(section, index) in sections" 
          :key="index" 
          :class="{ active: activeSection === section }" 
          @click="setActiveSection(section)"
        >
          {{ section }}
        </li>
      </ul>
    </div>

    <!-- Content -->
    <div class="content">
      
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Список разделов настроек
const sections = ['Профиль', 'Уведомления', 'Безопасность'];

// Активный раздел
const activeSection = ref(sections[0]);

// Функция для установки активного раздела
const setActiveSection = (section) => {
  activeSection.value = section;
};
</script>

<style lang="scss" scoped>


.settings-container {
  display: flex;
  height: 100vh;
  font-family: 'Montserrat';
}


/* Стили для боковой панели */
.sidebar {
  width: 30%;
  max-width: 300px;
  height: 100%;
  background: linear-gradient(135deg, #2c3e50, #34495e);
  color: white;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 1;
}

.sidebar h2 {
  margin-bottom: 20px;
  text-align: center;
  border: 1px #ffffff solid;
  padding: 5px;
  box-sizing: border-box;
  @include border-radius();
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar ul li {
  margin: 10px 0;
  cursor: pointer;
  transition: color 0.3s ease;
}

.sidebar ul li:hover {
  color: #1abc9c;
}

.sidebar ul li.active {
  color: #1abc9c;
  font-weight: bold;
}

/* Стили для основного контента */
.content {
  flex: 1;
  background: #ffffff;
  padding: 20px;
  overflow-y: auto;
}

.content h1 {
  margin-top: 0;
}
</style>