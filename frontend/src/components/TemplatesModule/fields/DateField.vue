<template>
  <div class="date-field">
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
        Формат даты:
        <select :value="localField.format" @change="updateFormat">
          <option value="YYYY-MM-DD">ГГГГ-ММ-ДД</option>
          <option value="DD/MM/YYYY">ДД/ММ/ГГГГ</option>
          <option value="MM/DD/YYYY">ММ/ДД/ГГГГ</option>
        </select>
      </label>
      <label>
        <input type="checkbox" :checked="localField.required" @change="updateRequired">
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
    updateFormat(e) {
      this.localField.format = e.target.value
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