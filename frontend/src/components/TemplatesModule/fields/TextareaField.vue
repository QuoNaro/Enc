<template>
  <div class="textarea-field">
    <div class="field-header">
      <span class="drag-handle">≡</span>
      <input 
        :value="localField.label"
        @input="updateLabel"
        placeholder="Название поля"
        class="field-label"
      />
      <button class="delete-field" @click="$emit('delete')">×</button>
    </div>
    <textarea 
      :value="localField.placeholder"
      @input="updatePlaceholder"
      placeholder=""
      class="field-input"
    />
    <div class="field-options">
      <label class="checkbox-label">
        <input 
          type="checkbox" 
          :checked="localField.required"
          @change="updateRequired"
          class="checkbox-input"
        />
        Обязательное поле
      </label>
      <div class="max-length-option">
        <label>Макс. длина:</label>
        <input 
          type="number" 
          :value="localField.maxLength"
          @input="updateMaxLength"
          class="number-input"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['field'],
  data() {
    return {
      localField: { ...this.field }
    };
  },
  watch: {
    field: {
      deep: true,
      handler(newVal) {
        this.localField = { ...newVal };
      }
    }
  },
  methods: {
    updateLabel(e) {
      this.localField.label = e.target.value;
      this.emitUpdate();
    },
    updatePlaceholder(e) {
      this.localField.placeholder = e.target.value;
      this.emitUpdate();
    },
    updateRequired(e) {
      this.localField.required = e.target.checked;
      this.emitUpdate();
    },
    updateMaxLength(e) {
      const value = e.target.value ? parseInt(e.target.value) : null;
      this.localField.maxLength = value;
      this.emitUpdate();
    },
    emitUpdate() {
      this.$emit('update', { ...this.localField });
    }
  }
};
</script>

<style scoped>
.textarea-field {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 16px;
}

.field-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.drag-handle {
  font-size: 18px;
  color: #999;
  cursor: grab;
  margin-right: 8px;
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

.field-label::placeholder {
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
  min-height: 80px;
  padding: 8px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  resize: vertical;
  transition: border-color 0.2s ease;
}

.field-input:focus {
  border-color: #40a9ff;
}

.field-options {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #333;
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

.checkbox-input:checked {
  background-color: #40a9ff;
  border-color: #40a9ff;
}

.checkbox-input:focus {
  outline: none;
  border-color: #40a9ff;
}

.max-length-option {
  display: flex;
  align-items: center;
  gap: 8px;
}

.max-length-option label {
  font-size: 14px;
  color: #333;
}

.number-input {
  width: 80px;
  padding: 4px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s ease;
}

.number-input:focus {
  border-color: #40a9ff;
}
</style>