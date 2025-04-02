<template>
    <div class="text-field">
      <label :for="field.id">{{ field.label }}</label>
      <input 
        :type="field.type"
        :id="field.id"
        :placeholder="field.placeholder"
        v-model="internalValue"
        @input="handleInput"
      >
      <div v-if="errors" class="error-message">
        {{ errors.join('. ') }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      field: Object,
      value: [String, Number, Boolean]
    },
    data() {
      return {
        internalValue: this.value
      }
    },
    watch: {
      value(newVal) {
        this.internalValue = newVal
      }
    },
    computed: {
      errors() {
        return this.$parent.errors[this.field.id]
      }
    },
    methods: {
      handleInput() {
        this.$emit('input', this.internalValue)
      }
    }
  }
  </script>