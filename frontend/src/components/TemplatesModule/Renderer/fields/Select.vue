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
    inheritAttrs: false,
    inject: ['mode'],
    props: ['id', 'multiple', 'required', 'options', 'modelValue'],

    emits: ['update:modelValue'],
    
    computed: {
  selectedValue: {
    get() {
      return this.modelValue;
    },
    set(value) {
      this.$emit('update:modelValue', value);
    }
  }
},
    methods: {
      handleChange() {
        this.$emit('update:modelValue', this.selectedValue)
      }
    }
  }
  </script>