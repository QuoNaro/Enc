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
  import '@/assets/auth.css';

  
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
  
<style lang="scss">


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
    box-shadow: var(--shadow) 0px 0px 30px ;
    gap: 20px;

  }

  .buttons {
    display: flex;
    position: absolute;
    height: 20%;
    right: 0%; /* Центрирование по горизонтали */
    flex-direction: column;
    justify-content: space-between;

    * {
      background-color: white;
      color: black;
      padding: 10px;
      box-sizing: border-box;
      text-decoration: none;
      font-family: 'Arimo';
      font-weight: 900;
      text-transform: uppercase;
      justify-content: center;
      align-items: center;
      font-size: 1.6em;
      border-radius: 15px 0 0px 15px;
      text-align: center;
    }


  }


  
  .auth-container {

    width: 65%;

    h1 {
      width: 100%;
      
    }

    form {
      width: 100%;
      position: absolute; /* Абсолютное позиционирование */
      top: 50%; /* Центрирование по вертикали */
      left: 50%; /* Центрирование по горизонтали */
      transform: translate(-50%, -50%); /* Точное центрирование */

    }
    button {
      width: 75%;
    }
  }

 

  .auth-container,.img-container {
    position: relative;
    flex-direction: column;
    box-sizing: border-box;
    display:flex;
    height: 100%;
  }

  .auth-form {
    display: flex;
    transition: ease-in-out;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background-color: #fff;
    border-radius: 20px;
    
    border: 1px solid var(--border-color); 


    .form-group {
      margin-bottom: 20px;
      width: 100%;
      max-width: 500px;
  
      label {
        display: block;
        margin-bottom: 5px;
        font-size: 14px;
        color: #666;
      }
  
      input[type="text"],
      input[type="password"] {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        transition: border-color 0.3s ease;
  
        &:focus {
          border-color: var(--hover-color);
          outline: none;
        }
      }
      

      

      .error-message,
      .error-list {
        margin-top: 5px;
        color: var(--error-color);
        font-size: 12px;
  
        .error-item {
          list-style-type: none;
        }
      }
    }
  
    .submit-button {
      margin-top: 20px;
      padding: 10px 20px;
      overflow: hidden;
      border: none;
      border-radius: 25px;
      font-weight: 900;
      text-align: center;
      text-transform: uppercase;
      background-color: var(--secondary-color);
      color: #fff;
      font-size: 14px;
      cursor: pointer;
      justify-content: center;
      align-items: center;
      display: flex;
      transition: background-color 0.3s ease;
  
      &:hover {
        background-color: var(--primary-color);
      }
  
      &:disabled {
        background-color: #ccc;
        cursor: not-allowed;
      }
    }
  }

 
  @keyframes wavy {
    0% {
      transform: translateY(0%);
      rotate: 1deg;
    }
    25% {
      transform: translateY(10%);
      rotate: -1deg;
    }


    50% {
     
      transform: translateY(0%);
      rotate: 1deg;

    }

    75% {
      transform: translateY(10%);
      rotate: -1deg;
    }

    100%  {
      transform: translateY(0%);
      rotate: 1deg;

    } 
  }

  
  
  @mixin no-select {
  user-select: none; // Стандартное свойство
  -webkit-user-select: none; // Для старых версий Safari
  -moz-user-select: none; // Для Firefox
  -ms-user-select: none; // Для Internet Explorer

  pointer-events: none; // Опционально: отключает все события мыши
}


  .img-container {
    width: 100%;
    border: 1px solid var(--border-color);
    
    box-shadow: var(--shadow) 0 0 20px;
    height: 100%;
    
    border-radius: 20px;
    overflow: hidden;
  }

  .wave { 
    display: flex;
    transform-origin: center;
    @include no-select;
    position: absolute;
    left: -20%;
    width: 150%;
    bottom: -5%;


  }

  
  .wave-3{ animation: wavy ease-in-out 10s infinite; animation-delay: 1s;}
  .wave-2{ animation: wavy ease-in-out 10s infinite; animation-delay: 0.5s;}
  .wave-1{ animation: wavy ease-in-out 10s infinite}

  
  
</style>