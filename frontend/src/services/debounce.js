export default function debounce(func, delay) {
    let timeoutId;
    return function (...args) {
        clearTimeout(timeoutId); // Очищаем предыдущий таймер
        timeoutId = setTimeout(() => func.apply(this, args), delay); // Устанавливаем новый таймер
    };
}