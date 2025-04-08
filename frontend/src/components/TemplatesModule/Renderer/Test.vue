<template>
    <div>
      <TemplateRenderer :templateData="templateJson" />
    </div>
  </template>
  
  <script>
  import TemplateRenderer from "./TemplateRenderer.vue";
  
  export default {
    components: { TemplateRenderer },
    data() {
      return {
        templateJson: {
  "templateName": "Тестовый шаблон",
  "description": "Это тестовый шаблон для проверки функционала конструктора форм.",
  "groups": [
    {
      "id": "group_1",
      "title": "Основная информация",
      "fields": [
        {
          "id": "field_1",
          "type": "text",
          "label": "Имя пользователя",
          "placeholder": "Введите ваше имя",
          "required": true,
          "minLength": 2,
          "maxLength": 50
        },
        {
          "id": "field_2",
          "type": "password",
          "label": "Пароль",
          "placeholder": "Введите пароль",
          "required": true,
          "minLength": 6,
          "maxLength": 50
        }
      ]
    },
    {
      "id": "group_2",
      "title": "Дополнительная информация",
      "fields": [
        {
          "id": "field_3",
          "type": "textarea",
          "label": "О себе",
          "placeholder": "Расскажите немного о себе",
          "required": false,
          "rows": 5,
          "maxLength": 500
        },
        {
          "id": "field_10",
          "type": "textarea",
          "label": "вффывыфв себе",
          "placeholder": "Расскажите немного о себе",
          "required": true,
          "rows": 5,
          "maxLength": 500
        },
        {
          "id": "field_4",
          "type": "checkbox",
          "label": "Согласие на обработку данных",
          "defaultValue": false,
          "options": ["Я согласен на обработку персональных данных"],
          "required": true
        }
      ]
    },
    {
      "id": "group_3",
      "title": "Выбор предпочтений",
      "fields": [
        {
          "id": "field_5",
          "type": "select",
          "label": "Выберите город",
          "options": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"],
          "multiple": false,
          "required": true
        },
        {
          "id": "field_6",
          "type": "radio",
          "label": "Выберите пол",
          "options": ["Мужской", "Женский"],
          "required": true
        }
      ]
    },
    {
      "id": "group_4",
      "title": "Загрузка файлов",
      "fields": [
        {
          "id": "field_7",
          "type": "file",
          "label": "Загрузите ваше фото",
          "accept": "image/*",
          "multiple": false,
          "required": false
        }
      ]
    }
  ]
}
  };}}
  </script>