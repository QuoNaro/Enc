<template>
  <label>{{ label || 'Без метки' }}</label>
  <div class="password-container" v-if="mode==='view'">
    <noise " class="noise" :class="{ hide: isHiding, visible: isVisible }" @click="toggleNoise" Color="#fff"
      bgColor="#00a8ff" Depth="0.00004">
    </noise>
    <p>{{ $t('show') }}</p>
    <input v-bind="$attrs" :id="id" :type="inputType" :placeholder="placeholder" :minlength="minLength"
      :maxlength="maxLength" :required="required" v-model="inputValue" />
    <img :class="{ hide: !isHiding }" :src="`${assets.icons}/hide.svg`" @click="toggleNoise" alt="">
  </div>

  <div v-else class="password-container">
    <input v-bind="$attrs" :id="id" :type="inputType" :placeholder="placeholder" :minlength="minLength"
      :maxlength="maxLength" :required="required" v-model="inputValue" />
    <img :class="{ hide: !isHiding }" :src="`${assets.icons}/hide.svg`" @click="toggleNoise" alt="">
  </div>
</template>

<script setup>

import { ref, computed, inject } from 'vue';
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

const isHiding = ref(false);
const isVisible = ref(true);

const mode = inject('mode')

// Computed properties
const inputType = computed(() => (isHiding.value ? 'fake-password' : 'text'));

const inputValue = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

// Асинхронная функция для скрытия элемента
const toggleNoise = async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  if (isVisible.value === true) {
    isVisible.value = false
    await delay(200)
    isHiding.value = true
  }

  else {
    isHiding.value = false
    await delay(200)
    isVisible.value = true

  }

};
</script>

<style lang="scss" scoped>
.password-container {
  display: flex;
  margin: 10px;
  justify-content: center;
  align-items: center;
  position: relative;
  max-height: 40px;
  overflow: hidden;
  @include border-radius(soft);
  border: 3px #0898ff solid;
  background-color: #fff;

  input {
    display: flex;
    height: 100%;
    @include padding(8);
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
    right: 5px;
    transition: .4s ease-in-out;

    &:hover {
      cursor: pointer;

    }

    &.hide {
      opacity: 0;
      transition: .4s ease-in-out;
      @include unselectable;
    }
  }

  p {
    position: absolute;
    right: 0;
    font-weight: 500;
    color: #6e6e6e;
    transform: translateX(100%);
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    padding-left: 10px;
    padding-right: 10px;

    border-radius: 15px 0 0 15px;
    z-index: 6;
    transition: .4s ease-in-out;
  }

  .noiser:hover+p {
    transform: translateX(0%);
    transition: .4s ease-in-out;
    @include unselectable
  }

  .noise {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 2;
    opacity: 0;
    transition: .2s ease-in-out;


    &.visible {
      cursor: pointer;
      opacity: 100;
      transition: .2s ease-in-out;
    }

    &.hide {
      display: none;
      opacity: 0;

    }
  }
}
</style>