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
          <button @click="removeOption(index)">×</button>
        </div>
        <button @click="addOption">Добавить вариант</button>
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