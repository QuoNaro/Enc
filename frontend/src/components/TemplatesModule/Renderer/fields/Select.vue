<template>
    <select
      :id="id"
      :multiple="multiple"
      :required="required"
      v-model="selectedValue"
      @change="handleChange"
    >
      <option v-for="(option, index) in options" :key="index" :value="option">
        {{ option || 'Пустой вариант' }}
      </option>
    </select>
  </template>
  
  <script>
  export default {
    props: ['id', 'multiple', 'required', 'options', 'modelValue'],
    emits: ['update:modelValue'],
    data() {
      return {
        selectedValue: this.multiple ? [] : ''
      }
    },
    watch: {
      modelValue(newVal) {
        this.selectedValue = newVal
      }
    },
    methods: {
      handleChange() {
        this.$emit('update:modelValue', this.selectedValue)
      }
    }
  }
  </script>