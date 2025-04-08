<template>
    <div class="logo-container">
      <img v-if="imageSrc" :src="imageSrc" :alt="altText" class="logo-image" />
    </div>
  </template>
  
  <script>
  export default {
    name: 'Logo',
    props: {
      // Путь к изображению (если используется)
      imageSrc: {
        type: String,
        default: ''
      },
      // Альтернативный текст для изображения
      altText: {
        type: String,
        default: 'Логотип'
      }
    }
  }

  </script>
  
  <style lang="scss" scoped>
  

  .logo-container {
    display: inline-block;
    cursor: pointer;
  }
  
  .logo-container:not(.clickable) {
    cursor: default;
  }
  
  .logo-image {
    @include unselectable;
    max-width: 100%;
    height: auto;
  }
  
  .logo-svg {
    width: 100px;
    height: 100px;
  }
  </style>