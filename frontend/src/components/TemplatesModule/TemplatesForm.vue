<template>
    <div class="dynamic-form">
      <form @submit.prevent="handleSubmit">
        <div v-for="group in groupedFields" :key="group.id" class="form-group">
          <h3>{{ group.title }}</h3>
          <p v-if="group.description" class="group-description">{{ group.description }}</p>
          
          <div v-for="field in group.fields" :key="field.id" class="form-field">
            <!-- Text Input -->
            <template v-if="field.type === 'text'">
              <label :for="field.id">
                {{ field.label }} 
                <span v-if="field.required" class="required">*</span>
              </label>
              <input 
                :id="field.id"
                v-model="formData[field.id]"
                type="text"
                :placeholder="field.placeholder"
                @input="validateField(field)"
                :class="{ 'error': errors[field.id] }"
              >
              <div v-if="errors[field.id]" class="error-message">
                {{ errors[field.id] }}
              </div>
            </template>
  
            <!-- Checkbox -->
            <template v-if="field.type === 'checkbox'">
              <label :for="field.id" class="checkbox-label">
                <input 
                  :id="field.id"
                  v-model="formData[field.id]"
                  type="checkbox"
                >
                {{ field.label }}
              </label>
            </template>
  
            <!-- Slider -->
            <template v-if="field.type === 'slider'">
              <label :for="field.id">{{ field.label }}</label>
              <input 
                :id="field.id"
                v-model.number="formData[field.id]"
                type="range"
                :min="field.min"
                :max="field.max"
                :step="field.step"
              >
              <div class="slider-value">{{ formData[field.id] }}</div>
            </template>
          </div>
        </div>
        
        <button type="submit" :disabled="hasErrors">Сохранить</button>
      </form>
    </div>
</template>
  
<script>
  export default {
    props: {
      templateData: {
        type: Object,
        required: true
      }
    },
    
    data() {
      return {
        formData: {},
        errors: {}
      }
    },
    
    computed: {
      groupedFields() {
        return this.templateData.groups.map(group => ({
          ...group,
          fields: group.fieldIds.map(id => 
            this.templateData.fields.find(f => f.id === id)
          )
        }))
      },
      
      hasErrors() {
        return Object.keys(this.errors).length > 0
      }
    },
    
    created() {
      this.initializeFormData()
    },
    
    methods: {
      initializeFormData() {
        this.templateData.fields.forEach(field => {
          this.$set(this.formData, field.id, 
            field.hasOwnProperty('defaultValue') 
              ? field.defaultValue 
              : this.getDefaultValue(field.type)
          )
        })
      },
      
      getDefaultValue(type) {
        switch(type) {
          case 'checkbox': return false
          case 'slider': return 0
          default: return ''
        }
      },
      
      validateField(field) {
        if (!this.formData[field.id]) {
          this.errors[field.id] = 'Поле обязательно для заполнения'
          return
        }
        
        if (field.minLength && this.formData[field.id].length < field.minLength) {
          this.errors[field.id] = `Минимум ${field.minLength} символов`
          return
        }
        
        if (field.maxLength && this.formData[field.id].length > field.maxLength) {
          this.errors[field.id] = `Максимум ${field.maxLength} символов`
          return
        }
        
        if (field.validation?.regex) {
          const regex = new RegExp(field.validation.regex)
          if (!regex.test(this.formData[field.id])) {
            this.errors[field.id] = field.validation.message
            return
          }
        }
        
        this.errors[field.id] = ''
      },
      
      handleSubmit() {
        this.templateData.fields.forEach(field => {
          if (field.required) {
            this.validateField(field)
          }
        })
        
        if (!this.hasErrors) {
          this.$emit('submit', this.formData)
        }
      }
    }
  }
</script>
  
<style scoped>
  .dynamic-form {
    max-width: 600px;
    margin: 0 auto;
  }
  
  .form-group {
    margin-bottom: 2rem;
  }
  
  .form-field {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }
  
  input[type="text"] {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .checkbox-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .slider-value {
    text-align: right;
    margin-top: 0.5rem;
  }
  
  .error {
    border-color: red;
  }
  
  .error-message {
    color: red;
    font-size: 0.875rem;
    margin-top: 0.25rem;
  }
  
  .required {
    color: red;
    margin-left: 0.25rem;
  }
</style>