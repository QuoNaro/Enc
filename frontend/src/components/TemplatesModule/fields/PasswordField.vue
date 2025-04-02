<template>
  <div class="password-field">
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
        Мин. длина:
        <input 
          type="number" 
          :value="localField.minLength"
          @input="updateMinLength"
        >
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
    updateMinLength(e) {
      this.localField.minLength = parseInt(e.target.value)
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