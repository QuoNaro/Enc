<template>
  <div class="noiser">
    <div class="blur" :style="{
        backdropFilter: `blur(2px)`,
        position: `absolute`,
        width: `110%`,
        height: `110%`,
        background: `transparent`,
      }"></div>
    <div
      class="noise"
      :style="{
        width: `100%`,
        height: `100%`,
        background: `repeating-conic-gradient(${Color}, ${bgColor} ${Depth}%)`,
      }"
    ></div>
  </div>
  
  </template>
  
  <script>
  export default {
    name: "Noise",
    props: {
      // Цвет фона
      bgColor: {
        type: String,
        default: "black",
      },
      // Цвет шума
      Color: {
        type: String,
        default: "white",
      },
      Depth: {
        type: String,
        default: "0.00005",
      },
    },
  };
  </script>
  
  <style lang="scss" scoped>
  .noise {
    margin: auto;
    animation: back 500s linear infinite;
  }
  

  .noiser {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  @keyframes back {
    from {
      background-size: 10000% 10000%;
    }
    to {
      background-size: 100000% 100000%; /* Увеличенный диапазон анимации */
    }
  }
  </style>