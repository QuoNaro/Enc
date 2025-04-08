<template>
  <div :class="{ sidebar: true, hide: isHide }">
    <h2>Проверка пароля</h2>
    <form @submit.prevent="checkPassword">
      <label for="password">Введите пароль:</label>
      <input
        type="password"
        id="password"
        v-model="password"
        placeholder="Пароль"
        required
      />
      <button type="submit">Проверить</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>

  <div class="content">
    <h1>Основной контент</h1>
    <p>Здесь будет основная информация после успешной авторизации.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isHide: true,
      password: "",
      errorMessage: "",
      successMessage: "",
    };
  },
  mounted() {
    setTimeout(() => {
      this.isHide = false;
    }, 200);
  },
  methods: {
    checkPassword() {
      // Пример правильного пароля (можно заменить на динамическую проверку)
      const correctPassword = "secure123";

      if (this.password === correctPassword) {
        this.errorMessage = "";
        this.successMessage = "Пароль верный! Доступ разрешен.";
        // Можно добавить дополнительную логику, например, показать контент
      } else {
        this.errorMessage = "Неверный пароль. Попробуйте снова.";
        this.successMessage = "";
      }
    },
  },
};
</script>

<style scoped>
.sidebar {
  width: 30%;
  height: 100%;
  max-width: 300px;
  background: linear-gradient(135deg, #2c3e50, #34495e);
  color: white;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  transition: 0.4s ease-in-out;
  position: relative;
  z-index: 0;
}

.sidebar.hide {
  transition: 0.4s ease-in-out;
  transform: translateX(-100%);
}

.content {
  width: 100%;
  height: 100%;
  background: #ffffff;
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input {
  padding: 10px;
  border: none;
  @include border-radius();
  font-size: 16px;
}

button {
  padding: 10px;
  background-color: #1abc9c;
  color: white;
  border: none;
  @include border-radius();
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #16a085;
}

.error {
  color: #e74c3c;
  font-weight: bold;
}

.success {
  color: #2ecc71;
  font-weight: bold;
}
</style>