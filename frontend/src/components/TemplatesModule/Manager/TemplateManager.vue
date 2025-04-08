<template>
  <div class="template-creator">
    <!-- Боковая панель компонентов -->
    <div class="sidebar">
      <h3>Компоненты</h3>
      <draggable v-model="componentsList" :group="{ name: 'fields', pull: 'clone', put: false }" :clone="cloneField"
        item-key="type" class="field-list">
        <template #item="{ element }">
          <div :key="element.type" class="field-item-draggable">
            <span class="icon">{{ element.icon }}</span>
            {{ element.label }}
          </div>
        </template>
      </draggable>
    </div>



    <!-- Основной редактор -->
    <div class="editor">
      <div class="template-header">
        <input v-model="template.templateName" placeholder="Название шаблона" class="title-input" />
        <textarea v-model="template.description" placeholder="Описание шаблона" class="description-input" />
      </div>
      <draggable v-model="template.groups" handle=".group-header" :animation="300" ghost-class="sortable-ghost"
        chosen-class="sortable-chosen" drag-class="sortable-drag" item-key="id" class="group-container">
        <template #item="{ element, index }">

          <div :key="element.id" class="group">
            <div class="group-header">
              <span class="drag-handle">≡</span>
              <input v-model="element.title" placeholder="Название группы" class="group-title-input" />
              <button class="delete-group" @click="removeGroup(index)">×</button>
            </div>
            <div class="group-content">
              <draggable v-model="element.fieldIds" group="fields" :animation="250" ghost-class="sortable-ghost"
                chosen-class="sortable-chosen" drag-class="sortable-drag" item-key="id"
                @change="onFieldMove($event, element.id)">
                <template #item="{ element }">
                  <div :key="element.id" class="field-item">
                    <component :is="getFieldComponent(element.id)" :field="getFieldById(element.id)"
                      @delete="removeField(element.id)" @update="updateField(element.id, $event)" />
                  </div>
                </template>
              </draggable>
            </div>
          </div>
        </template>
      </draggable>
      <div class="actions">
        <button @click="addNewGroup">Добавить группу</button>
        <button @click="exportTemplateToJson">Создать шаблон</button>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import TextField from "./fields/TextField.vue";
import TextareaField from "./fields/TextareaField.vue";
import CheckboxField from "./fields/CheckboxField.vue";
import SelectField from "./fields/SelectField.vue";
import RadioField from "./fields/RadioField.vue";
import FileField from "./fields/FileField.vue";
import PasswordField from "./fields/PasswordField.vue";


export default {
  components: { draggable },
  data() {
    return {
      template: {
        templateName: "",
        description: "",
        groups: [],
        fields: [],
      },
      componentsList: [
        { type: "text", label: "Текст", icon: "Aa" },
        { type: "textarea", label: "Многострочный текст", icon: "Ab" },
        { type: "checkbox", label: "Чекбокс", icon: "✓" },
        { type: "select", label: "Выпадающий список", icon: "▼" },
        { type: "radio", label: "Радио-кнопки", icon: "○" },
        { type: "file", label: "Файл", icon: "↑" },
        { type: "password", label: "Пароль", icon: "•••" },
        { type: "login", label: "Логин", icon: "•••" },
        { type: "url", label: "URL", icon: "~" },
      ],
      nextFieldId: 1,
      nextGroupId: 1,
    };
  },

  methods: {
    cloneField(original) {

      const newField = {
        id: `field_${this.nextFieldId++}`,
        group_id: "",
        label: "",
        type: original.type,
        ...this.getDefaultFieldProps(original.type),
      };
      this.template.fields.push(newField);
      return { id: newField.id };
    },
    addNewGroup() {
      this.template.groups.push({
        id: `group_${this.nextGroupId++}`,
        title: "",
        fieldIds: [],
      });
    },
    getDefaultFieldProps(type) {
      switch (type) {
        case "text":
          return {
            placeholder: "Плейсхолдер для текствого поля",
            required: false,
            minLength: 0,
            maxLength: 50,
            validation: { regex: "", message: "" },
          };
        case "textarea":
          return {
            placeholder: "",
            required: false,
            rows: 3,
            maxLength: 500,
          };
        case "checkbox":
          return {
            defaultValue: false,
            options: [""],
            required: false,
          };
        case "select":
          return {
            options: [""],
            multiple: false,
            required: false,
          };
        case "radio":
          return {
            options: [""],
            required: false,
          };
        case "file":
          return {
            accept: "*",
            multiple: false,
            required: false,
          };
        case "password":
          return {
            placeholder: "",
            required: false,
            minLength: 6,
            maxLength: 50,
          };
        default:
          return {};
      }
    },
    getFieldById(id) {
      if (typeof(id) === 'object') {
        id = id.id
      }
    
      return this.template.fields.find(f => f.id === id);
    },
    getFieldComponent(fieldId) {
      const field = this.getFieldById(fieldId);
      if (!field) return null;
      switch (field.type) {
        case "text":
          return TextField;
        case "textarea":
          return TextareaField;
        case "checkbox":
          return CheckboxField;
        case "select":
          return SelectField;
        case "radio":
          return RadioField;
        case "file":
          return FileField;
        case "password":
          return PasswordField;
        default:
          return TextField;
      }
    },
    removeGroup(index) {
      this.template.groups.splice(index, 1);
    },
    removeField(fieldId) {
      const fieldIndex = this.template.fields.findIndex((f) => f.id === fieldId);
      if (fieldIndex !== -1) {
        this.template.fields.splice(fieldIndex, 1);
        this.template.groups.forEach((group) => {
          const idx = group.fieldIds.findIndex((item) => item.id === fieldId);
          if (idx !== -1) group.fieldIds.splice(idx, 1);
        });
      }
    },
    updateField(fieldId, updates) {

      const field = this.getFieldById(fieldId);
      Object.assign(field, updates);
    },
    getGroupByFieldId(fieldId) {
      return this.template.groups.find(group => group.fieldIds.includes(fieldId)) || null;
    },
    onFieldMove(event, groupId) {
      const { added, removed, moved } = event;

      if (added) {
        // Поле добавлено в группу
        const fieldId = added.element;
        this.updateFieldGroup(fieldId, groupId); // Обновляем связь поля с группой
        
      }

      if (removed) {
        // Поле удалено из группы
        const fieldId = removed.element;
      }


    },

    updateFieldGroup(fieldId, groupId) {
      const field = this.getFieldById(fieldId);
      if (field) {
        field.group_id = groupId;
      }
    },
    resetForm() {
      this.template = {
        templateName: "",
        description: "",
        groups: [],
        fields: [],
      };
      this.nextFieldId = 1;
      this.nextGroupId = 1;
    },
    exportTemplateToJson() {

      const templateData = {
        templateName: this.template.templateName,
        description: this.template.description,
        groups: this.template.groups.map(group => ({
          id: group.id,
          title: group.title,
          fields: group.fieldIds
            .map(fieldId => {
              const field = this.getFieldById(fieldId);
              if (!field) {
                console.warn(`Field with ID ${fieldId} not found. Skipping...`);
                return null;
              }
              return {
                id: field.id,
                type: field.type,
                label: field.value,
                ...this.getDefaultFieldProps(field.type),
                ...field
              };
            })
            .filter(field => field !== null) // Remove null entries
        }))
      };

      // Convert to JSON string
      const jsonString = JSON.stringify(templateData, null, 2);
      console.log(jsonString)
      return jsonString; // Return the JSON string
    }
  },
};
</script>

<style lang="scss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

.list-move {
  transition: transform 0.3s ease;
}

.list-enter-active {
  transition: all 0.3s ease-out;
}

.list-leave-active {
  transition: all 0.2s ease-in;
  position: absolute;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px) scale(0.9);
}

.group {
  transition: all 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
  transform-origin: top left;
}

.group.sortable-ghost {
  opacity: 0.8;
  transform: scale(0.95);
  border: 2px dashed #42b883;
  background: #f0f9eb;
}

.group.sortable-chosen {
  transform: scale(1.02);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.field-item {
  transition: all 0.2s ease-out;
}

.field-item-draggable:active {
  cursor: grabbing;
  cursor: -webkit-grabbing;
  /* Для Safari */
}

.field-item.sortable-ghost {
  opacity: 0.5;
  background: #e8f4ff;
  border: 2px dashed #409eff;
  transform: translateX(10px);
}

.sortable-drag {
  opacity: 0.9;
  transform: rotate(2deg);
}

.sortable-fallback {
  animation: shake 0.3s ease-in-out;
}

@keyframes shake {
  0% {
    transform: translateX(0);
  }

  25% {
    transform: translateX(-5px);
  }

  50% {
    transform: translateX(5px);
  }

  75% {
    transform: translateX(-5px);
  }

  100% {
    transform: translateX(0);
  }
}

.template-creator {
  display: flex;
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.sidebar {
  width: 280px;
  background: #f8f9fa;
  @include border-radius();
  padding: 1.5rem;
}

.field-list {
  min-height: 200px;
  display: grid;
  gap: 10px;
}

.field-item-draggable {
  border: 1px solid #ddd;
  padding: 12px;
  @include border-radius();
  background: white;
  cursor: grab;
}

.field-item-draggable:hover {
  transform: scale(1.02);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.field-item-draggable .icon {
  font-weight: bold;
  color: #666;
}

.editor {
  flex: 1;
}

.template-header {
  margin-bottom: 2rem;
}

.title-input {
  width: 100%;
  padding: 12px;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  @include border-radius();
}

.description-input {
  width: 100%;
  height: 100px;
  padding: 8px;
  border: 1px solid #ccc;
  @include border-radius();
  resize: vertical;
}

.group {
  background: #f5f5f5;
  @include border-radius();
  padding: 15px;
  margin-bottom: 15px;
}

.group-header {
  display: flex;
  align-items: center;
  padding: 10px;
  background: #e0e0e0;
  @include border-radius();
  margin-bottom: 15px;
}

.drag-handle {
  cursor: grab;
  margin-right: 10px;
}

.group-title-input {
  flex: 1;
  padding: 8px;
  border: none;
  background: transparent;
  font-weight: bold;
}

.delete-group {
  background: transparent;
  border: none;
  color: red;
  cursor: pointer;
  margin-left: 10px;
}

.add-field {
  margin-top: 1rem;
  display: flex;
  gap: 10px;
}

.actions {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
}

button {
  padding: 0.8rem 1.5rem;
  @include border-radius();
  cursor: pointer;
  transition: all 0.2s;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.group-content {
  min-height: 100px;
  border: 2px dashed #e0e0e0;
  @include border-radius();
  padding: 1rem;
  margin: 1rem 0;
}

.group-content:hover {
  border-color: #42b883;
}

.sortable-ghost {
  opacity: 0.5;
  background: #e8f4ff;
  border-style: dashed;
}

.sortable-chosen {
  transform: scale(1.01);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.sortable-drag {
  opacity: 0.9;
  transform: rotate(2deg);
}
</style>