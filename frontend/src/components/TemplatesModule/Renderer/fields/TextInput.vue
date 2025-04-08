<!-- components/fields/TextInput.vue -->
<template>
    <input
      :id="id"
      type="text"
      :placeholder="placeholder"
      :minlength="minLength"
      :maxlength="maxLength"
      :required="required"
      v-model="inputValue"
    />
  </template>
  
  <script>
  export default {
    props: ['id', 'placeholder', 'minLength', 'maxLength', 'required', 'modelValue'],
    emits: ['update:modelValue'],
    computed: {
      inputValue: {
        get() { return this.modelValue },
        set(value) { this.$emit('update:modelValue', value) }
      }
    }
  }
  </script>