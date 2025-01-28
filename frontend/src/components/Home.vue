<template>
    <div class="home">
      <h1>Добро пожаловать на главную страницу!</h1>
      <p>Это ваше приложение на Vue 3 с использованием Vue Router.</p>
      <p>Здесь вы можете добавлять свои компоненты и функционал.</p>
      <router-link to="/login">Перейти к логину</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  .home {
    text-align: center;
    margin-top: 50px;
  }
  
  h1 {
    font-size: 2.5em;
    color: #42b983;
  }
  
  p {
    font-size: 1.2em;
  }
  
  .router-link {
    margin-top: 20px;
    display: inline-block;
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  
  .router-link:hover {
    background-color: #369e74;
  }
  </style>
  