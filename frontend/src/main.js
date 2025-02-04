// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Импортируем маршрутизатор
import { createPinia } from 'pinia'; // Импортируем Pinia

const app = createApp(App);

// Инициализируем Pinia
const pinia = createPinia();
app.use(pinia);

// Инициализируем Vue Router
app.use(router);

app.mount('#app');