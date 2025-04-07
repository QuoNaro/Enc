import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  server: {
    port: 8080,
  },
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      "@@" : fileURLToPath(new URL('./', import.meta.url))
    },
  },
});