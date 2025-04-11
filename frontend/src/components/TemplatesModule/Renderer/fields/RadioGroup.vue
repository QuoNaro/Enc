<template>
  <div 
    class="radio-group"
    :style="{
      gridTemplateColumns: `repeat(${gridSize}, 1fr)`,
      gridTemplateRows: `repeat(${gridSize}, 1fr)`
    }"
  >
    <label
      v-for="(option, index) in optionsWithPlaceholders"
      :key="index"
      class="radio-item"
      :class="{ 'placeholder': option.isPlaceholder }"
      :style="{
        maxWidth: itemSize,
        maxHeight: itemSize
      }"
    >
      <input
        v-if="!option.isPlaceholder"
        type="radio"
        :id="`${id}_${index}`"
        :value="option"
        :name="id"
        :checked="modelValue === option"
        @change="$emit('update:modelValue', option)"
        class="radio-input"
      />
      <span class="radio-label">{{ option }}</span>
    </label>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  id: { type: String, required: true },
  options: { 
    type: Array,
    required: true,
  },
  modelValue: {
    required: true
  }
});

defineEmits(['update:modelValue']);

const GAP = 1; // Значение gap в rem
const MIN_ITEM_SIZE = 8; // Минимальный размер элемента в rem

const gridSize = computed(() => {
  return Math.ceil(Math.sqrt(props.options.length));
});

const itemSize = computed(() => {
  const containerWidth = 100 / gridSize.value;
  const gapTotal = (gridSize.value - 1) * GAP;
  const calculatedSize = (100 - gapTotal) / gridSize.value;
  
  return `calc(${calculatedSize}rem - ${GAP}rem)`;
});

const optionsWithPlaceholders = computed(() => {
  const total = gridSize.value ** 2;
  const placeholders = Array.from(
    { length: total - props.options.length },
    () => ({ isPlaceholder: true })
  );
  return [...props.options, ...placeholders];
});
</script>

<style lang="scss" scoped>
.radio-group {
  border: 3px #0898ff solid;
  display: grid;
  gap: 1.5rem;
  @include padding(10);
  @include border-radius(soft);
  margin: 10px;
  background: #f5f5f5;
}

.radio-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  @include border-radius(soft);
  cursor: pointer;
  transition: .5s;
  box-sizing: border-box;
}

.radio-item:not(.placeholder):hover {
  box-shadow: #7a7a7a63 0 0 10px;
}

.radio-input {
  margin-right: 0.75rem;
  cursor: pointer;
  flex-shrink: 0;
}

.radio-label {
  font-size: 0.875rem;
  color: #333;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.placeholder {
  visibility: hidden;
  opacity: 0;
  pointer-events: none;
}

@media (max-width: 768px) {
  .radio-item {
    padding: 0.75rem;
  }
  
  .radio-label {
    font-size: 0.75rem;
  }
}

</style>