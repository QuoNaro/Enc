<template>
  <div class="radio-field">
    <div class="field-header">
      <span class="drag-handle">≡</span>
      <input 
        :value="localField.label"
        @input="updateLabel"
        placeholder="Название поля"
        class="field-label"
      >
      <button class="delete-field" @click="$emit('delete')">×</button>
    </div>
    <div class="field-options">
      <div class="options-list">
        <div v-for="(option, index) in localField.options" :key="index" class="option-item">
          <input 
            :value="option"
            @input="updateOption(index, $event)"
            placeholder="Вариант"
            class="option-input"
          >
          <button class="remove-option" @click="removeOption(index)">×</button>
        </div>
        <button class="add-option" @click="addOption">
          + Добавить вариант
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['field'],
  data() {
    return {
      localField: { ...this.field, options: [...this.field.options] }
    }
  },
  watch: {
    field: {
      deep: true,
      handler(newVal) {
        this.localField = { 
          ...newVal,
          options: [...newVal.options]
        }
      }
    }
  },
  methods: {
    updateLabel(e) {
      this.localField.label = e.target.value
      this.emitUpdate()
    },
    updateOption(index, e) {
      this.localField.options[index] = e.target.value
      this.emitUpdate()
    },
    addOption() {
      this.localField.options.push('')
      this.emitUpdate()
    },
    removeOption(index) {
      this.localField.options.splice(index, 1)
      this.emitUpdate()
    },
    emitUpdate() {
      this.$emit('update', { 
        ...this.localField,
        options: [...this.localField.options]
      })
    }
  }
}
</script>

<style scoped>
.radio-field {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.field-header {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
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

.field-options {
  margin-top: 8px;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.option-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.option-input {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s ease;
}

.option-input:focus {
  border-color: #40a9ff;
}

.remove-option {
  background: none;
  border: none;
  color: #ff4d4f;
  font-size: 16px;
  cursor: pointer;
  transition: color 0.2s ease;
}

.remove-option:hover {
  color: #ff7875;
}

.add-option {
  background-color: #40a9ff;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.add-option:hover {
  background-color: #1890ff;
}
</style>