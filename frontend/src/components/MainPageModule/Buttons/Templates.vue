<template>
      <div :class="{sidebar : true, hide: isHide}">
        
      </div>
      
      <div class="content">
        
      </div>
  </template>


<script>
import apiClient from '@/utils/api';

export default {
  data() {
    return {
      isHide: true,
      templates: [] // Добавляем поле для хранения данных шаблонов
    };
  },

  async beforeMount( ) {
    const response = await apiClient.get('/api/v1/get-templates');
      console.log(response)
      // Сохраняем полученные данные в поле templates
      this.templates = response.data;
  },
  async mounted() {
      setTimeout(() => {
        this.isHide = false;
      }, 200);
    }
};
</script>

  <style scoped>

  .sidebar {
    width: 30%;
    height: 100%;
    max-width: 300px;
    background: linear-gradient(135deg, #2c3e50, #34495e);
    color: white;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0,0,0,0.1);
    transition: .4s ease-in-out;
    position: relative;
    z-index: 0;
  }

  .sidebar.hide{
    transition: .4s ease-in-out;
    transform: translateX(-100%);
  }

  .content {
    width: 100%;
    height: 100%;
    background: #ffffff;
  }

  </style>