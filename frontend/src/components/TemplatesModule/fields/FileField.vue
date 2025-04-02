<template>
  <div class="file-field">
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
      <label>
        Типы файлов:
        <input 
          :value="localField.accept"
          @input="updateAccept"
          placeholder="Например: image/*, .pdf"
        >
      </label>
      <label>
        <input 
          type="checkbox" 
          :checked="localField.multiple"
          @change="updateMultiple"
        >
        Множественный выбор
      </label>
      <label>
        <input 
          type="checkbox" 
          :checked="localField.required"
          @change="updateRequired"
        >
        Обязательное поле
      </label>
    </div>
  </div>
</template>

<script>
export default {
  props: ['field'],
  data() {
    return {
      localField: { ...this.field }
    }
  },
  watch: {
    field: {
      deep: true,
      handler(newVal) {
        this.localField = { ...newVal }
      }
    }
  },
  methods: {
    updateLabel(e) {
      this.localField.label = e.target.value
      this.emitUpdate()
    },
    updateAccept(e) {
      this.localField.accept = e.target.value
      this.emitUpdate()
    },
    updateMultiple(e) {
      this.localField.multiple = e.target.checked
      this.emitUpdate()
    },
    updateRequired(e) {
      this.localField.required = e.target.checked
      this.emitUpdate()
    },
    emitUpdate() {
      this.$emit('update', { ...this.localField })
    }
  }
}
</script>