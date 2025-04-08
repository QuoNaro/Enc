<template>
    <input
      :id="id"
      type="file"
      :accept="accept"
      :multiple="multiple"
      :required="required"
      @change="handleFileChange"
    />
  </template>
  
  <script>
  export default {
    props: ['id', 'accept', 'multiple', 'required', 'modelValue'],
    emits: ['update:modelValue'],
    methods: {
      handleFileChange(event) {
        const files = Array.from(event.target.files)
        this.$emit('update:modelValue', this.multiple ? files : files[0])
      }
    }
  }
  </script>