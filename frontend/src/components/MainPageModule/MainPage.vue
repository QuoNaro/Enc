<script setup>
import Logo from '@/components/Logo.vue';
import { assets } from '@/config';
import { ref, onMounted, onBeforeUnmount, watch, markRaw } from 'vue';
import i18n from '@/utils/i18n';


// Реактивные данные
const currentHash = ref(window.location.hash || '#password');
const currentComponent = ref(null);
const componentsMap = ref({});
const buttons = ref([]);


// Загрузка компонентов
const importComponents = async (order = {}) => {
  // Импортируем модули из основной папки и дочерних папок
  const modules = import.meta.glob([
    '@/components/MainPageModule/Buttons/*.vue', // Основная папка
    '@/components/MainPageModule/Buttons/*/*.vue' // Дочерние папки
  ]);

  // Временный массив для хранения загруженных компонентов
  const loadedComponents = [];

  for (const path in modules) {
    // Разбиваем путь на части для анализа
    const pathParts = path.split('/');
    const fileName = pathParts[pathParts.length - 1].replace('.vue', ''); // Название файла без расширения

    // Проверяем, что файл начинается с заглавной буквы
    if (/^[A-Z]/.test(fileName)) {
      const module = await modules[path]();

      // Имя компонента: всегда используем только название файла (fileName)
      const componentName = fileName;

      // Генерируем ключ для перевода
      const translationKey = componentName.replace(/([A-Z])/g, '$1').toLowerCase();

      // Находим порядковый номер из словаря order
      const orderIndex = Object.values(order).indexOf(componentName);
      const componentOrder = orderIndex !== -1 ? Object.keys(order)[orderIndex] : Infinity;

      // Сохраняем информацию о кнопке во временном массиве
      loadedComponents.push({
        name: componentName,
        label: i18n.global.t(`buttons.${translationKey}`),
        link: componentName.replace(/([A-Z])/g, ' $1').trim().toLowerCase(),
        order: Number(componentOrder) // Преобразуем ключ в число
      });

      // Добавляем компонент в карту
      componentsMap.value[componentName.replace(/([A-Z])/g, ' $1').trim().toLowerCase()] = markRaw(module.default);
    }
  }

  // Сортируем компоненты по указанному порядку
  loadedComponents.sort((a, b) => a.order - b.order);

  // Добавляем отсортированные компоненты в массив buttons
  buttons.value = loadedComponents.map(({ name, label, link }) => ({ name, label, link }));
};

// Выбор компонента по хэшу
const selectComponent = () => {
  const componentName = currentHash.value.replace('#', '');
  currentComponent.value = componentsMap.value[componentName];
};

// Обновление хэша
const updateHash = (newHash) => {
  currentHash.value = `#${newHash}`;
  window.location.hash = newHash;
};

// Обработчик изменения хэша
const onHashChange = () => {
  currentHash.value = window.location.hash || '#password';
};

// Жизненный цикл
onMounted(async () => {
  await importComponents({0:'Vault',1: "Templates"});
  selectComponent();
  window.addEventListener('hashchange', onHashChange);
});

watch(currentHash, () => {
  selectComponent();
});
</script>

<template>
  <div class="main-container">
      <nav class="sidebar">
        <Logo :imageSrc="assets.logo" altText="Мой логотип" />
        <div v-for="button in buttons" :key="button.link" :href="`#${button.link}`"
          @click.prevent="updateHash(button.link)" :class="{
            link: true,
            active: currentHash === `#${button.link}`,
          }">
          <img :src="`${assets.icons}/${button.link}.svg`" alt="">
          <div class="text">{{ button.label }}</div>
        </div>
      </nav>

    <div class="content">
      <component :is="currentComponent" />
    </div>
  </div>
</template>


<style lang="scss" scoped>
$shadow: var(--shadow);
$accent: var(--accent-color);
$secondary: var(--secondary-color);

.main-container {
  background-color: white;
  overflow: hidden;
  @include border-radius(soft);
  display: flex;
  width: calc(100% - 50px); // Корректируем ширину с учетом margin
  height: calc(100% - 50px); // Корректируем высоту с учетом margin
  box-shadow: $shadow 0px 0px 30px;

  @mixin unselectable {
    user-select: none;
    -webkit-user-select: none; // Для Safari и старых версий Chrome
    -moz-user-select: none; // Для Firefox
    -ms-user-select: none; // Для Internet Explorer и Edge (старые версии)
  }

  .sidebar {
    width: 25%;
    max-width: 250px;
    min-width: 200px;
    gap:  15px;
    box-sizing: border-box;
    padding: 15px;
    display: flex;
    z-index: 1;
    flex-direction: column;
    height: 100%;
    background-color: $secondary;

    .link {
      @include unselectable;
      display: flex;
      font-family: 'Arimo';
      font-weight: 900;
      width: 100%;
      padding: 5px;
      height: 40px;
      gap: 5px;
      box-sizing: border-box;
      text-decoration: none;
      color: $secondary;
      background-color: #d1d1d1;
      color: $secondary;
      overflow: hidden;

      transform: translateX(0);
      @include border-radius();
      justify-content: center;
      align-items: center;
      transition: .8s ease-in-out;
      transition: .3s ease-in-out background-color;

      .text {
        justify-content: center;
        align-items: center;
        display: flex;
        transition: .4s ease-in-out;
      }


      

      
    }

    .link img {
      display: flex;
      height: 70%;
      position: absolute;
      left: 5px;


      

    }

    .link:hover {
      background-color: #fff;
    }
    .link:not(.active) {
        cursor: pointer;
      }

      .link.active>.text {
        transform: translateX(50%);
      }

      .link.active {

        background-color: #fff;
      }

  }

  .content {
    width: 100%;
    background-color: white;
    height: 100%;


    .header {
      display: flex;
      width: 100%;
      height: 120px;
      background-color: var(--accent-color);
    }

  }
}
</style>