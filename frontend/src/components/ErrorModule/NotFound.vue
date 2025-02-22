<template>
    <div class="not-found">
      <h1>404 - Страница не найдена</h1>
      <p>Извините, но запрашиваемая страница не существует.</p>
      <router-link to="/auth">Вернуться на страницу входа</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NotFound'
  };
  </script>
  
  <style scoped>
  .not-found {
    text-align: center;
    margin-top: 50px;
  }
  </style>