<template>
    <div>
      <label v-for="(option, index) in options" :key="index">
        <input
          type="checkbox"
          :id="`${id}_${index}`"
          :value="option"
          @change="handleCheckboxChange"
        />
        {{ option || 'Пустой вариант' }}
      </label>
    </div>
  </template>
  
  <script>
  export default {
    props: ['id', 'options', 'required', 'modelValue'],
    emits: ['update:modelValue'],
    data() {
      return {
        selectedValues: this.modelValue || []
      }
    },
    watch: {
      modelValue(newVal) {
        this.selectedValues = newVal
      }
    },
    methods: {
      handleCheckboxChange(event) {
        const value = event.target.value
        const index = this.selectedValues.indexOf(value)
        
        if (index === -1) {
          this.selectedValues.push(value)
        } else {
          this.selectedValues.splice(index, 1)
        }
        
        this.$emit('update:modelValue', this.selectedValues)
      }
    }
  }
  </script>