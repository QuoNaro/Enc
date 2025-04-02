<template>
  <div class="textarea-field">
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
    <textarea 
      :value="localField.placeholder"
      @input="updatePlaceholder"
      placeholder="Placeholder"
      class="field-input"
    />
    <div class="field-options">
      <label>
        <input 
          type="checkbox" 
          :checked="localField.required"
          @change="updateRequired"
        >
        Обязательное поле
      </label>
      <div>
        <label>Макс. длина:</label>
        <input 
          type="number" 
          :value="localField.maxLength"
          @input="updateMaxLength"
        >
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
    updatePlaceholder(e) {
      this.localField.placeholder = e.target.value
      this.emitUpdate()
    },
    updateRequired(e) {
      this.localField.required = e.target.checked
      this.emitUpdate()
    },
    updateMaxLength(e) {
      this.localField.maxLength = parseInt(e.target.value)
      this.emitUpdate()
    },
    emitUpdate() {
      this.$emit('update', { ...this.localField })
    }
  }
}
</script>