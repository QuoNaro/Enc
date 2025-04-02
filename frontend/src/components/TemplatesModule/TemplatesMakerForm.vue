<template>
    <div class="template-builder">
      <div class="form-group">
        <label>Название шаблона:</label>
        <input v-model="formTemplate.templateName" required>
      </div>
  
      <div class="form-group">
        <label>Описание:</label>
        <textarea v-model="formTemplate.description"></textarea>
      </div>
  
      <!-- Поля -->
      <div class="fields-section">
        <h3>Поля</h3>
        <div v-for="(field, index) in formTemplate.fields" :key="field.id" class="field-item">
          <div class="field-header">
            <span>Поле {{ index + 1 }}</span>
            <button @click="removeField(index)">Удалить</button>
          </div>
          
          <div class="form-group">
            <label>ID:</label>
            <input v-model="field.id" required>
          </div>
          
          <div class="form-group">
            <label>Тип:</label>
            <select v-model="field.type">
              <option value="text">Текст</option>
              <option value="checkbox">Чекбокс</option>
              <option value="slider">Слайдер</option>
            </select>
          </div>
  
          <!-- Общие параметры -->
          <div class="form-group">
            <label>Заголовок:</label>
            <input v-model="field.label" required>
          </div>
          <div class="form-group">
            <label>Обязательное:</label>
            <input type="checkbox" v-model="field.required">
          </div>
  
          <!-- Тип-зависимые параметры -->
          <div v-if="field.type === 'text'">
            <div class="form-group">
              <label>Placeholder:</label>
              <input v-model="field.placeholder">
            </div>
            <div class="form-group">
              <label>Мин. длина:</label>
              <input type="number" v-model.number="field.minLength">
            </div>
            <div class="form-group">
              <label>Макс. длина:</label>
              <input type="number" v-model.number="field.maxLength">
            </div>
            <div class="form-group">
              <label>Регулярное выражение:</label>
              <input v-model="field.validation.regex">
            </div>
            <div class="form-group">
              <label>Сообщение об ошибке:</label>
              <input v-model="field.validation.message">
            </div>
          </div>
  
          <div v-if="field.type === 'checkbox'">
            <div class="form-group">
              <label>Значение по умолчанию:</label>
              <input type="checkbox" v-model="field.defaultValue">
            </div>
          </div>
  
          <div v-if="field.type === 'slider'">
            <div class="form-group">
              <label>Минимальное значение:</label>
              <input type="number" v-model.number="field.min">
            </div>
            <div class="form-group">
              <label>Максимальное значение:</label>
              <input type="number" v-model.number="field.max">
            </div>
            <div class="form-group">
              <label>Шаг:</label>
              <input type="number" v-model.number="field.step">
            </div>
            <div class="form-group">
              <label>Значение по умолчанию:</label>
              <input type="number" v-model.number="field.defaultValue">
            </div>
          </div>
        </div>
        <button @click="addField">Добавить поле</button>
      </div>
  
      <!-- Группы -->
      <div class="groups-section">
        <h3>Группы</h3>
        <div v-for="(group, index) in formTemplate.groups" :key="group.id" class="group-item">
          <div class="group-header">
            <span>Группа {{ index + 1 }}</span>
            <button @click="removeGroup(index)">Удалить</button>
          </div>
          
          <div class="form-group">
            <label>ID группы:</label>
            <input v-model="group.id" required>
          </div>
          <div class="form-group">
            <label>Заголовок:</label>
            <input v-model="group.title" required>
          </div>
          <div class="form-group">
            <label>Описание группы:</label>
            <textarea v-model="group.description"></textarea>
          </div>
          <div class="form-group">
            <label>Поля в группе:</label>
            <select v-model="group.fieldIds" multiple>
              <option 
                v-for="field in formTemplate.fields" 
                :key="field.id"
                :value="field.id"
              >
                {{ field.label }} ({{ field.id }})
              </option>
            </select>
          </div>
        </div>
        <button @click="addGroup">Добавить группу</button>
      </div>
  
      <button @click="generateJSON">Сгенерировать JSON</button>
      <pre v-if="generatedJSON">{{ generatedJSON }}</pre>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const formTemplate = ref({
    templateName: '',
    description: '',
    fields: [],
    groups: []
  });
  
  const generatedJSON = ref(null);
  
  function addField() {
    formTemplate.value.fields.push({
      id: '',
      label: '',
      type: 'text',
      required: false,
      placeholder: '',
      minLength: null,
      maxLength: null,
      validation: {
        regex: '',
        message: ''
      },
      defaultValue: null,
      min: null,
      max: null,
      step: null
    });
  }
  
  function removeField(index) {
    formTemplate.value.fields.splice(index, 1);
  }
  
  function addGroup() {
    formTemplate.value.groups.push({
      id: '',
      title: '',
      description: '',
      fieldIds: []
    });
  }
  
  function removeGroup(index) {
    formTemplate.value.groups.splice(index, 1);
  }
  
  function generateJSON() {
    // Очистка пустых значений
    const cleanObj = (obj) => {
      Object.keys(obj).forEach(key => {
        if (obj[key] === null || obj[key] === '' || (Array.isArray(obj[key]) && obj[key].length === 0)) {
          delete obj[key];
        }
      });
      return obj;
    };
  
    const cleanedTemplate = {
      ...formTemplate.value,
      fields: formTemplate.value.fields.map(field => cleanObj({ ...field })),
      groups: formTemplate.value.groups.map(group => cleanObj({ ...group }))
    };
  
    generatedJSON.value = JSON.stringify(cleanedTemplate, null, 2);
  }
  </script>
  
  <style>
  .template-builder {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
  }
  
  input, select, textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
  }
  
  .fields-section, .groups-section {
    margin-bottom: 2rem;
  }
  
  .field-item, .group-item {
    border: 1px solid #ccc;
    padding: 1rem;
    margin-bottom: 1rem;
  }
  
  .field-header, .group-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  button {
    background: #4CAF50;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background: #45a049;
  }
  
  pre {
    background: #f4f4f4;
    padding: 1rem;
    overflow-x: auto;
  }
  </style>