<template>
  <div class="main-container">

      <div class="img-container">
        <div class="img"></div>
        <div class="buttons">
          <a href="#signin">Логин</a>
          <a href="#signup">Регистрация</a>
        </div>
      </div>

      <transition name="expand">
      <div class="auth-container"> 
        <component :is="currentComponent" />
      </div>
    </transition>
      
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
  }


  .img {
    background-image: var(--picnic-url);
    border-radius: 1.2em;
    width: 100%;
    height:100%;
    object-position:center ;
    background-size: cover;
    object-fit: cover;
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

  .img-container {
    width: 100%;
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
    border: 2px solid var(--border-color); 
  
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
      border: none;
      border-radius: 25px;
      background-color: var(--secondary-color);
      color: #fff;
      font-size: 16px;
      cursor: pointer;
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
  </style>