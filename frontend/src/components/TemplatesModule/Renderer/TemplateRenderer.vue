<template>
  <div class="template-renderer">
    <div v-if="mode === 'edit'">
      <h1>{{ templateData.templateName }}</h1>
      <p>{{ templateData.description }}</p>

      <form @submit.prevent="handleSubmit" autocomplete="off">
        <div v-for="group in templateData.groups" :key="group.id" class="group">
          <h2>{{ group.title || 'Без названия' }}</h2>

          <div v-for="field in group.fields" :key="field.id" class="field">
            <!-- <label :for="field.id">{{ field.label || 'Без метки' }}</label> -->

            <component :is="getFieldComponent(field.type)" v-bind="field" v-model="formValues[field.id]" />
          </div>
        </div>
        
        <button type="submit">Сохранить</button>
      </form>
    </div>

    
    <div v-else>
    
    </div>
    
  </div>
  
</template>

<script>
import TextInput from './fields/TextInput.vue'
import Textarea from './fields/Textarea.vue'
import Select from './fields/Select.vue'
import PasswordInput from './fields/PasswordInput.vue'
import RadioGroup from './fields/RadioGroup.vue'
import CheckboxGroup from './fields/CheckboxGroup.vue'
import FileInput from './fields/FileInput.vue'
import UrlInput from './fields/UrlInput.vue'

export default {
  
  props: {
    templateData: {
      type: Object,
      required: true,
    },
    mode: {
      type: String,
      default: 'edit',
      validator: (value) => ['edit', 'view'].includes(value), // Валидация допустимых значений
    },
  },
  components: {
    TextInput,
    Textarea,
    Select,
    PasswordInput,
    RadioGroup,
    CheckboxGroup,
    FileInput,
    UrlInput
  },

  data() {
    return {
      formValues: {}
    }
    
  },
  provide() {
    return {
      mode: this.mode, // Передаем mode в дочерние компоненты
    }},
  methods: {
    getFieldComponent(type) {
      const componentMap = {
        text: 'TextInput',
        textarea: 'Textarea',
        password: 'PasswordInput',
        select: 'Select',
        radio: 'RadioGroup',
        checkbox: 'CheckboxGroup',
        file: 'FileInput',
        url: 'UrlInput'
      }
      return componentMap[type] || 'div'
    },
    handleSubmit() {
      console.log('Отправленные данные:', this.formValues)
    }
  }
}
</script>

<style lang="scss" scoped>
.group {
  font-family: "Montserrat";
  padding: 5px;
  box-sizing: border-box;

  .field {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;

  }


}
</style>