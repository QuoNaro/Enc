<template>
    <div>
      <select v-model="$i18n.locale">
        <option value="en">English</option>
        <option value="ru">Русский</option>
      </select>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LanguageSwitcher'
  }
  </script>
  