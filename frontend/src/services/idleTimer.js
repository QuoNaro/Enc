import nt from '@/services/notificationService';
import i18n from './i18n';
import router from '@/router';

let idleTimeout = null;

function getTokenExpirationTime() {
    const token = localStorage.getItem('token');
    if (!token) return null;

    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
        atob(base64)
            .split('')
            .map(function (c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            })
            .join('')
    );

    const payload = JSON.parse(jsonPayload);
    const expirationTime = payload.exp * 1000; // Преобразуем секунды в миллисекунды
    return expirationTime;
}

// Функция для запуска или перезапуска таймера
export function resetIdleTimer() {
    if (idleTimeout) clearTimeout(idleTimeout); // Очистка предыдущего таймера
    startIdleTimer(); // Запускаем новый таймер
}

// Функция для старта таймера
function startIdleTimer() {
    const expirationTime = getTokenExpirationTime();
    if (!expirationTime) {
        console.warn('No token found or invalid token.');
        return;
    }

    const currentTime = Date.now();
    const remainingTime = expirationTime - currentTime;

    if (remainingTime <= 0) {
        handleTokenExpiration(); // Если токен уже истек, обрабатываем это сразу
        return;
    }

    idleTimeout = setTimeout(() => {
        handleTokenExpiration(); // Вызов функции обработки истечения токена
    }, remainingTime); // Установить таймер на оставшееся время до истечения токена
}

// Обработка истечения токена
function handleTokenExpiration() {
    localStorage.removeItem('token'); // Удаляем токен из localStorage
    router.push('/auth');
    nt.showNotification('info', `${i18n.t('auth.error.auth.TOKEN-001')}`, 0);
    
}

// Дебаунсинг функция
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        const context = this;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}

function debounceResetIdleTimer(delay_per_miliseconds = 60) {
    const debouncedResetIdleTimer = debounce(resetIdleTimer, delay_per_miliseconds * 1000); // 1 минута
    // Добавляем обработчики событий для отслеживания активности пользователя
    ['mousemove', 'mousedown', 'keydown', 'scroll'].forEach(event => {
        document.addEventListener(event, debouncedResetIdleTimer);
    });
    // Запускаем таймер при загрузке приложения
    resetIdleTimer();
}

export default {
    resetIdleTimer,
    handleTokenExpiration,
    debounceResetIdleTimer,
    init: () => {
        const token = localStorage.getItem('token');
        if (token) {
            debounceResetIdleTimer(); // Инициализация отслеживания активности
        } else {
            console.warn('No token found. Idle timer not started.');
        }
    },
};