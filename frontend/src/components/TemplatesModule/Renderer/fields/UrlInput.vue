<template>
  <div class="url-input-wrapper">
    <input
      :id="id"
      type="text"
      :placeholder="placeholder"
      :required="required"
      :pattern="urlOrIpPattern"
      :class="{ 'is-valid': isValid, 'is-invalid': isInvalid }"
      @input="validateInput"
      @blur="showValidation = true"
      v-model="inputValue"
      aria-describedby="input-help"
    />
    
    <div v-if="showValidation" class="validation-message">
      <span v-if="isValid" class="valid-icon">✓</span>
      <span v-else-if="isInvalid" class="invalid-icon">✗</span>
      <span class="message-text">{{ validationMessage }}</span>
    </div>
  </div>
</template>

<script>
export default {
  inject: ['mode'],
  props: {
    id: String,
    placeholder: String,
    required: Boolean,
    modelValue: String
  },
  emits: ['update:modelValue'],
  data() {
    return {
      showValidation: false,
      validationMessage: '',
      isValid: false,
      isInvalid: false
    }
  },
  computed: {
    inputValue: {
      get() { return this.modelValue },
      set(value) { 
        this.$emit('update:modelValue', value)
        this.validateInput(value)
      }
    },
    urlOrIpPattern() {
      // Улучшенное регулярное выражение с проверкой диапазонов IP
      return "^" +
        "(https?:\/\/)?" +
        "(" +
          "([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}" + 
        "|" +
          "(" +
            "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" +
            "\\.){3}" +
            "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" +
          ")" +
        ")" +
        "(\\:\\d+)?" +
        "(\\/[^\\s]*)?" +
        "$";
    }
  },
  methods: {
    validateInput(value) {
      const pattern = new RegExp(this.urlOrIpPattern);
      this.isValid = pattern.test(value);
      this.isInvalid = value.length > 0 && !this.isValid;
      
      if (this.isValid) {
        this.validationMessage = 'Адрес корректен';
      } else if (value.length === 0) {
        this.validationMessage = 'Поле обязательно для заполнения';
      } else {
        this.validationMessage = 'Введите корректный URL или IP-адрес';
      }
    }
  }
}
</script>

<style scoped>
.url-input-wrapper {
  position: relative;
  margin: 1rem 0;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #ced4da;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus {
  border-color: #80bdff;
  outline: 0;
  box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
}

.validation-message {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  padding: 0.5rem;
  background: #fff3cd;
  border: 1px solid #ffeeba;
  border-radius: 4px;
  margin-top: 0.25rem;
  display: flex;
  align-items: center;
  font-size: 0.875rem;
}

.valid-icon {
  color: #28a745;
  margin-right: 0.5rem;
}

.invalid-icon {
  color: #dc3545;
  margin-right: 0.5rem;
}

.is-valid {
  border-color: #28a745 !important;
}

.is-invalid {
  border-color: #dc3545 !important;
}

.message-text {
  flex: 1;
}
</style>