import { createRouter, createWebHistory } from "vue-router";
import nt from "@/utils/notificationService";
import i18n from "@/utils/i18n";

// Components
import NotFound from "@/components/ErrorModule/NotFound.vue";
import UserAuth from "@/components/AuthModule/UserAuth.vue";
import MainPage from "@/components/MainPageModule/MainPage.vue";
import NewTemplate from "@/components/TemplatesModule/Manager/TemplateManager.vue";
import T from "@/components/TemplatesModule/Renderer/Test.vue";


// Определение маршрутов
const routes = [
  {
    path: "/auth",
    name: "UserAuth",
    component: UserAuth,
    children: [{ path: "#signin" }, { path: "#signup" }],
  },
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/new-template",
    name: "NewTemplate",
    component: NewTemplate,
  },
  {
    path: "/test",
    name: "Test",
    component: T,
  },
  {
    path: "/:pathMatch(.*)*", // Новый синтаксис для обработки несуществующих маршрутов
    name: "NotFound",
    component: NotFound, // Компонент для 404 страницы
  },
];

// Создание экземпляра роутера
const router = createRouter({
  history: createWebHistory(), // Используем HTML5 History Mode
  routes,
});

// Функция для проверки аутентификации
function isAuthenticated() {
  const token = localStorage.getItem("token");
  if (!token) return false;

  try {
    const payload = JSON.parse(atob(token.split(".")[1]));
    const expirationTime = payload.exp; // Время истечения токена (в секундах)

    if (expirationTime && Date.now() / 1000 > expirationTime) {
      return false;
    }

    return true; // Токен действителен
  } catch (error) {
    return false; // Ошибка при разборе токена
  }
}

// Глобальный навигационный гвард
router.beforeEach((to, from, next) => {
  // Проверяем, авторизован ли пользователь
  if (to.path !== "/auth" && !isAuthenticated()) {
    // Если токен истёк, показываем уведомление
    if (localStorage.getItem("token")) {
      const message = i18n.global.t("auth.error.auth.TOKEN-001"); // Используем i18n.global.t
      nt.showNotification("info", message, 15000); // Показываем уведомление
    }
    next("/auth"); // Перенаправляем на страницу аутентификации
    localStorage.removeItem("token");
    return;
  }

  // Обновляем заголовок страницы
  document.title = to.meta.title || "Encryption";

  next(); // Разрешаем переход
});

export default router;  