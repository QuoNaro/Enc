<template>
  <label>{{ label || 'Без метки' }}</label>
  <div class="password-container">
    <noise class="noise" :class="{ visible: isVisible }" @click="toggleNoise" Color="#fff" bgColor="#00a8ff"
      Depth="0.00004"></noise>
    <input :id="id" :type="inputType" :placeholder="placeholder" :minlength="minLength" :maxlength="maxLength"
      :required="required" v-model="inputValue" />
    <img  :class="{ hide: isVisible }" :src="`${assets.icons}/hide.svg`" @click="toggleNoise" alt="">
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import noise from '@/components/_micro/noise.vue';

import { assets } from '@/config';

// Props
const props = defineProps({
  id: String,
  label: {
    type: String,
    required: true,
  },
  placeholder: String,
  minLength: Number,
  maxLength: Number,
  required: Boolean,
  modelValue: String,
});

// Emits
const emit = defineEmits(['update:modelValue']);

// Reactive state
const isVisible = ref(true);

// Computed properties
const inputType = computed(() => (isVisible.value ? 'fake-password' : 'text'));

const inputValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

// Methods
const toggleNoise = () => {
  isVisible.value = !isVisible.value;
};
</script>

<style lang="scss" scoped>
.password-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  max-height: 40px;
  overflow: hidden;
  @include border-radius(hard);
  border: 3px #0898ff solid;

  input {
    @include padding(7);
    @include none;
    @include border-radius();
    width: 100%;
    font-size: 16px;
    transition: opacity 0.3s ease;
    background: white;
  }



  img {
    position: absolute;
    display: flex;
    width: auto;
    height: 60%;
    z-index: 3;
    right: 5px;

    &:hover {
      cursor: pointer;
    }

    &.hide {
      opacity: 0;
      @include unselectable;
    }
  }



  .noise {
    position: absolute;
    display: none;
    width: 100%;
    height: 100%;
    z-index: 2;

    &.visible {
      display: flex;
      opacity: 1;
      cursor: pointer;
    }

  }
}
</style>