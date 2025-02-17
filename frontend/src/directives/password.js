export default {
  update(el) {
    // Сохраняем текущее значение элемента
    const originalValue = el.value;

    // Фильтруем значение, оставляя только разрешенные символы
    const filteredValue = originalValue.replace(/[^a-zA-Z0-9!@#$%^&*()\-_=+[\]{}|;:',.<>?/`~]/g, '');

    // Если значение изменилось, обновляем его
    if (filteredValue !== originalValue) {
      el.value = filteredValue;

      // Отправляем событие input только если значение действительно изменилось
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }
  }
};