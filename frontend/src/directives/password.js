export default {
  update(el) {
      // Разрешаем буквы (a-zA-Z), цифры (0-9), специальные символы и пробелы
      const filteredValue = el.value.replace(/[^a-zA-Z0-9!@#$%^&*()\-_=+[\]{}|;:',.<>?/`~]/g, '');
      el.value = filteredValue; // Обновляем значение элемента
      el.dispatchEvent(new Event('input')); // Отправляем событие input для реагирования на изменение
  }
};