// format.js

// Добавляем метод format к прототипу String
function install(app) {
    String.prototype.format = function () {
      let str = this.toString();
      for (let i = 0; i < arguments.length; i++) {
        const regex = new RegExp(`\\{${i}\\}`, 'g');
        str = str.replace(regex, arguments[i]);
      }
      return str;
    };
  }
  
  export default {
    install,
  };