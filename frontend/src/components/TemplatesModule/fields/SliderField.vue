<template>
  <div class="slider-field">
    <div class="field-header">
      <span class="drag-handle">≡</span>
      <input 
        v-model="field.label"
        placeholder="Название поля"
        class="field-label"
      >
      <button class="delete-field" @click="$emit('delete')">×</button>
    </div>
    <div class="field-options">
      <div class="range-option">
        <label>Min:</label>
        <input type="number" v-model.number="field.min">
      </div>
      <div class="range-option">
        <label>Max:</label>
        <input type="number" v-model.number="field.max">
      </div>
      <div class="range-option">
        <label>Step:</label>
        <input type="number" v-model.number="field.step">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['field']
}
</script>