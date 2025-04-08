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
  props: {
    bgColor: {
      type: String,
      required: false,
      default: '#fff',
    },
    placeholder : String,
    id: String,
    rows: Object,
    maxLength: Int32Array,
    required: Boolean,
    modelValue: Object,
    label: String,
  },
  emits: ['update:modelValue'],
  computed: {
    inputValue: {
      get() { return this.modelValue },
      set(value) { this.$emit('update:modelValue', value) }
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


    textarea {
      width: 100%;
      height: 100%;
      border: none;
      @include none;
      resize: none;
    }
  }
}
</style>