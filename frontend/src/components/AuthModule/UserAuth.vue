<template>
 
    <div class="main-container">

      <div class="img-container">
          <img src="@/assets/wave1.svg" alt="Wave 1" class="wave wave-1">
          <img src="@/assets/wave2.svg" alt="Wave 2" class="wave wave-2">
          <img src="@/assets/wave3.svg" alt="Wave 3" class="wave wave-3">
      </div>
        



      <div class="auth-container"> 
        <component :is="currentComponent" />
      </div>

        
      </div>

  
</template>
  
<script>
  import SignInForm from './SignInForm.vue';
  import SignUpForm from './SignUpForm.vue';
 

  
  export default {
    name: 'UserAuth',
    components: {
      SignInForm,
      SignUpForm,
    },
    data() {
      return {
        currentHash: window.location.hash || '#signin',
        hashChangeHandler: null,
      };
    },
    computed: {
      currentComponent() {
        // Возвращаем компонент в зависимости от хэша
        return this.currentHash === '#signup' ? 'SignUpForm' : 'SignInForm';
      },
    },
    methods: {
      navigateTo(hash) {
        window.location.hash = hash;
        this.currentHash = hash;
      },
    },
    mounted() {
      this.changeTitle = () => {
        switch (this.currentHash) {
          case '#signin':
            document.title = 'Авторизация';
            break;
          case '#signup':
            document.title = 'Регистрация';
            break;
        }
      };
      this.hashChangeHandler = () => {
        this.currentHash = window.location.hash;
        this.changeTitle();
      };
      window.addEventListener('hashchange', this.hashChangeHandler);
    },
    beforeUnmount() {
      if (this.hashChangeHandler) {
        window.removeEventListener('hashchange', this.hashChangeHandler);
      }
    },
  };
</script>
<style lang="scss" scoped>
// Переменные для повторяющихся значений
$border-color: var(--border-color);
$shadow: var(--shadow);

// Миксин для отключения выделения текста
@mixin no-select {
  user-select: none; // Стандартное свойство
  -webkit-user-select: none; // Для старых версий Safari
  -moz-user-select: none; // Для Firefox
  -ms-user-select: none; // Для Internet Explorer
}

// Миксин для центрирования элементов
@mixin centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

// Анимация волн
@keyframes wavy {
  0%, 100% {
    transform: translateY(0%) rotate(2deg);
  }
  50% {
    transform: translateY(15%) rotate(-2deg);
  }
}

// Главный контейнер
.main-container {
  font-family: 'Arimo';
  display: flex;
  flex-direction: row;
  width: 65%;
  padding: 40px;
  box-sizing: border-box;
  background-color: white;
  height: 85%;
  border-radius: 2em;
  box-shadow: $shadow 0px 0px 30px;
  gap: 20px;

  // Общие стили для auth-container и img-container
  .auth-container,
  .img-container {
    position: relative;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    height: 100%;
  }

  // Блок авторизации
  .auth-container {
    width: 100%;

    h1 {
      width: 100%;
    }

    form {
      @include centered; // Центрирование формы
      width: 100%;
    }

    button {
      width: 75%;
    }
  }

  // Контейнер изображения
  .img-container {
    width: 100%;
    border: 1px solid $border-color;
    box-shadow: $shadow 0 0 20px;
    border-radius: 20px;
    overflow: hidden;

    .wave {
      display: block;
      position: absolute;
      left: -20%;
      width: 150%;
      bottom: -5%;
      transform-origin: center;
      animation: wavy ease-in-out 10s infinite;

      // Добавляем классы для задержки анимации
      &.wave-1 {
        animation-delay: 0s;
      }

      &.wave-2 {
        animation-delay: 0.5s;
      }

      &.wave-3 {
        animation-delay: 1s;
      }
    }
  }
}
</style>