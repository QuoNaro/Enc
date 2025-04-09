<template>
    <div>
      <label v-for="(option, index) in options" :key="index">
        <input
          type="radio"
          :id="`${id}_${index}`"
          :value="option"
          :name="id"
          :required="required"
          @change="$emit('update:modelValue', option)"
        />
        {{ option || 'Пустой вариант' }}
      </label>
    </div>
  </template>
  
  <script>
  export default {
    inject: ['mode'],
    props: ['id', 'options', 'required', 'modelValue'],
    emits: ['update:modelValue']
  }
  </script>