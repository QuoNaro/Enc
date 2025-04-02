<template>
  <div class="checkbox-field">
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
        <input 
          type="checkbox" 
          :checked="localField.defaultValue"
          @change="updateDefaultValue"
        >
        Включено по умолчанию
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
    updateDefaultValue(e) {
      this.localField.defaultValue = e.target.checked
      this.emitUpdate()
    },
    emitUpdate() {
      this.$emit('update', { ...this.localField })
    }
  }
}
</script>