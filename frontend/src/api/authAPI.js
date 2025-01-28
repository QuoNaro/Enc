// src/api/authApi.js
import axios from 'axios';

const BASE_URL = 'http://localhost:8000'; // URL вашего FastAPI сервера

const authApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
});

// Экспортируйте экземпляр Axios
export default authApi;
