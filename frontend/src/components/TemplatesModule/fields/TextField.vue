<template>
  <div class="text-field">
    <!-- Заголовок с возможностью редактирования -->
    <div class="field-header">
      <input 
        type="text" 
        :value="localField.label"
        @input="updateLabel"
        placeholder="Название поля"
        class="editable-label"
      />
      <button class="delete-field" @click="$emit('delete')">×</button>
    </div>

    <!-- Опции поля -->
   

    <!-- Текстовое поле -->
   
    
    <div class="field-options">
      <input 
      v-bind="field.attrs"
      :type="field.type"
      :id="field.id"
      :placeholder="field.placeholder"
      v-model="internalValue"
      @input="handleInput"
      :class="{ 'has-error': hasErrors }"
      class="field-input"
    />


      <div class="option-row">
        <label class="checkbox-label">
          <input 
            type="checkbox" 
            :checked="localField.required"
            @change="updateRequired"
            class="checkbox-input"
          >
          Обязательное поле
        </label>
      </div>
    </div>

    <!-- Сообщение об ошибке -->
    <div v-if="hasErrors" class="error-message">
      {{ errorMessages }}
    </div>
    
  </div>
</template>

<script>
import { defineComponent, ref, watch, computed } from 'vue';

export default defineComponent({
  name: 'TextField',
  methods: {
    updateRequired(e) {
      this.localField.required = e.target.checked;
      this.emitUpdate();
    },
  
    emitUpdate() {
        this.$emit('update', { ...this.localField });
    },


    
  },
  props: {
    field: {
      type: Object,
      required: true
    },
    modelValue: {
      type: [String, Number, Boolean],
      default: ''
    },
    validationErrors: {
      type: Object,
      default: () => ({})
    }
  },

  emits: ['update:modelValue', 'delete', 'update:label'],

  setup(props, { emit }) {
    const internalValue = ref(props.modelValue);
    const localField = ref({ ...props.field });

    // Watch for changes in the prop value
    watch(() => props.modelValue, (newVal) => {
      internalValue.value = newVal;
    });

    // Watch for changes in the field label
    watch(() => props.field.label, (newLabel) => {
      localField.value.label = newLabel;
    });

    // Computed property for errors
    const fieldErrors = computed(() => {
      return props.field?.id ? props.validationErrors[props.field.id] || [] : [];
    });

    // Check if there are any errors
    const hasErrors = computed(() => {
      return Array.isArray(fieldErrors.value) && fieldErrors.value.length > 0;
    });

    // Formatted error messages
    const errorMessages = computed(() => {
      return fieldErrors.value.join('. ');
    });

    // Input handler for the text field
    const handleInput = () => {
      emit('update:modelValue', internalValue.value);
    };

    // Update label handler
    const updateLabel = (e) => {
      localField.value.label = e.target.value;
      emit('update:label', e.target.value); // Emit the updated label to the parent
    };

    return {
      internalValue,
      localField,
      fieldErrors,
      hasErrors,
      errorMessages,
      handleInput,
      updateLabel
    };
  }
});
</script>

<style scoped>
.text-field {
  margin-bottom: 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.field-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.field-label {
  flex-grow: 1;
  font-size: 16px;
  border: none;
  outline: none;
  background: transparent;
  font-weight: 500;
  color: #333;
}

.editable-label {
  flex-grow: 1;
  font-size: 16px;
  font-weight: 500;
  color: #333;
  border: none;
  outline: none;
  background: transparent;
  transition: color 0.2s ease;
}

.editable-label::placeholder {
  color: #aaa;
}

.delete-field {
  background: none;
  border: none;
  color: #ff4d4f;
  font-size: 18px;
  cursor: pointer;
  transition: color 0.2s ease;
}

.delete-field:hover {
  color: #ff7875;
}

.field-input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.field-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.field-input:focus {
  border-color: #40a9ff;
  box-shadow: 0 0 4px rgba(64, 169, 255, 0.3);
}

.field-input.has-error {
  border-color: #ff4d4f;
  box-shadow: 0 0 4px rgba(255, 77, 79, 0.3);
}

.error-message {
  color: #ff4d4f;
  font-size: 12px;
  margin-top: 4px;
}

.checkbox-input {
  margin: 0;
  appearance: none;
  width: 16px;
  height: 16px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  cursor: pointer;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #333;
}

.checkbox-input:checked {
  background-color: #40a9ff;
  border-color: #40a9ff;
}

.checkbox-input:focus {
  border-color: #40a9ff;
  outline: none;
}
</style>