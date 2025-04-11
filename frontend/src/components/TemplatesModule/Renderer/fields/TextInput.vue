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
    inject: ['mode'],
    emits: ['update:modelValue'],
    computed: {
      inputValue: {
        get() { return this.modelValue },
        set(value) { this.$emit('update:modelValue', value) }
      }
    }
  }
  </script>

<style scoped lang="scss">
input {
  margin: 10px;
  @include padding(8);
  border: 3px solid #0898ff;
  @include border-radius(soft);
  font-size: 16px;
  outline: none;
  
}


</style>