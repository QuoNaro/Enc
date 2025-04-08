<template>
    <div
      class="blur"
      :style="{
        width: '100%',
        height: '100%',
        backdropFilter: `blur(${blurAmount}px)`, // Добавляем размытие
      }"
    ></div>
  </template>
  
  <script>
  export default {
    name: "Blur",
    props: {
      blurAmount: {
        type: Number,
        default: 5, // Значение по умолчанию для размытия
      },
    },
  };
  </script>
  