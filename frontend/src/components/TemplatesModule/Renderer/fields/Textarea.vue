<template>
  <div class="box-area">
    <label style="
    background: linear-gradient(0deg, #ffffff 50%, #00000000 50%);
    "
    >{{ label }}</label>

    <div class="area">

      <textarea :id="id" :placeholder="placeholder" :rows="rows" :maxlength="maxLength" :required="required"
        v-model="inputValue"></textarea>
    </div>
  </div>

</template>

<script>
export default {
  inject: ['mode'],
  props: {
    bgColor: {
      type: String,
      required: false,
      default: '#fff',
    },
    placeholder : String,
    id: String,
    rows: Number,
    maxLength: Number,
    required: Boolean,
    modelValue: String,
    label: String,
  },
  emits: ['update:modelValue'],
  computed: {
    inputValue: {
      get() { return this.modelValue },
      set(value) { this.$emit('update:modelValue', value)}
    }
  }
}
</script>

<style lang="scss">



$padding: 15;
$margin: 10px;
.box-area {
  position: relative;
  
  

  label {
    position: absolute;
    width: fit-content;
    left: $margin + $padding;
    
    padding-left: 5px;
    padding-right: 5px;
    
    
  }



  .area {
    margin: $margin;
    border: 3px solid #0898ff;
    @include border-radius(soft);
    @include padding($padding);
    background-color: white;
    max-height: 300px;
    height: 150px;


    textarea {
      width: 100%;
      height: 100%;
      border: none;
      mask-image: linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 5%, rgba(0,0,0,1) 95%, rgba(0,0,0,0) 100%);

      overflow-y: auto; /* Добавляем вертикальную полосу прокрутки */
      @include none;
      @include custom-scrollbar(#0898ff)
    }
    
    }
    
}
</style>