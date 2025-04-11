<template>
  {{ label }}
  <div class="custom-select" :class="{ open: isOpen }" @click.stop="toggleDropdown">
    <div class="selected-item">
      {{ selectedValue || placeholder }}
    </div>
    <ul class="options" v-if="isOpen">
      <li
        v-for="(option, index) in options"
        :key="index"
        :value="option"
        @click="selectOption(option)"
      >
        {{ option || $t('empty_var') }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted, inject } from 'vue';
import i18n from '@/utils/i18n'

const props = defineProps({
  id: String,
  multiple: Boolean,
  required: Boolean,
  label: {
    type: String,
    required: true,
  },
  options: Array,
  modelValue: [String, Array],
  placeholder: {
    type: String,
    default: i18n.global.t('select_placeholder')
  }
});

const emit = defineEmits(['update:modelValue']);

const mode = inject('mode');

const isOpen = ref(false);
const selectedValue = ref(props.modelValue || null);

watch(() => props.modelValue, (newValue) => {
  selectedValue.value = newValue;
});

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const selectOption = (option) => {
  selectedValue.value = option;
  emit('update:modelValue', option);
};

const closeDropdown = () => {
  isOpen.value = false;
};

const handleClickOutside = (event) => {
  const dropdown = document.querySelector('.dropdown'); // Добавьте соответствующий селектор
  if (dropdown && !dropdown.contains(event.target)) {
    closeDropdown();
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style lang="scss" scoped>
.custom-select {
  position: relative;
  width: 100%px;
  margin: 10px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;

  .selected-item {
    height: 40px;
    padding: 0 10px;
    border: 3px solid #0898ff;
    @include border-radius(soft);
    background-color: #fff;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;

    &::after {
      content: '▼';
      font-size: 12px;
      color: #666;
    }
  }

  .options {
  display: block; // Убедитесь, что элемент не скрыт
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  z-index: 10;
  list-style: none;
  padding: 0;
  margin: 0;
  overflow-y: auto;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  
  @include custom-scrollbar(#0898ff);
  height: 40px*4;
    


    li {
      padding: 10px;
      cursor: pointer;
      transition: background-color 0.3s;

      &:hover {
        background-color: #f0f0f0;
      }
    }
  }

  &.open {
    .selected-item {
      border-bottom-left-radius: 0;
      border-bottom-color: #fff;
      border-bottom-right-radius: 0;
    }
  }
}
</style>