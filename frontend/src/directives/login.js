export default {
  update(el) {
      const filteredValue = el.value.replace(/[^a-zA-Z0-9]/g, ''); // Фильтруем значение
      el.value = filteredValue; // Обновляем значение элемента
      el.dispatchEvent(new Event('input')); // Отправляем событие input для реагирования на изменение
  }
};