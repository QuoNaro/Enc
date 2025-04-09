<template>
    <input
      :id="id"
      type="url"
      :placeholder="placeholder"
      :required="required"
      v-model="inputValue"
    />
  </template>
  
  <script>
  export default {
    inject: ['mode'],
    props: ['id', 'placeholder', 'required', 'modelValue'],
    emits: ['update:modelValue'],
    computed: {
      inputValue: {
        get() { return this.modelValue },
        set(value) { this.$emit('update:modelValue', value) }
      }
    }
  }
  </script>