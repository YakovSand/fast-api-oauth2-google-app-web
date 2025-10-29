  import { createRouter, createWebHistory } from 'vue-router'
  import Home from '@/components/Home.vue'
  import AuthGoogle from '@/components/AuthGoogle.vue'


  // Define application routes
  // Home route and Google authentication route
  // Each route is associated with a specific component
  const routes = [
    { path: '/', component: Home },
    { path: '/auth/google', component: AuthGoogle }
  ]

  // Create and configure the Vue Router instance which is used for navigation
  const router = createRouter({
    history: createWebHistory(),
    routes
  })

  export default router

