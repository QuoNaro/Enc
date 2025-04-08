export default {
  update(el) {
    // Сохраняем исходное значение элемента
    const originalValue = el.value;

    // Фильтруем значение, оставляя только разрешенные символы (буквы и цифры)
    const filteredValue = originalValue.replace(/[^a-zA-Z0-9]/g, '');

    // Если значение изменилось после фильтрации
    if (filteredValue !== originalValue) {
      // Обновляем значение элемента
      el.value = filteredValue;

      // Отправляем событие input, чтобы компонент мог реагировать на изменения
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }
  }
};