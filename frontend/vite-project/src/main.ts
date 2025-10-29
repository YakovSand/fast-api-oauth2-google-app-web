import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Create and mount the Vue application with the router
createApp(App)
  .use(router)
  .mount('#app')