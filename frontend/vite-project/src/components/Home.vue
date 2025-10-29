<template>
  <div>
    <h1>{{ message }}</h1>
    <button class="google-btn" @click="loginWithGoogle">
      <img src="../assets/google.png" width="32" />
      <span class="google-text">Login with Google</span>
    </button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const message = ref<string>('Hello from Vue!')

// Google OAuth login
function loginWithGoogle() {
  // Redirect to your backend OAuth endpoint
  window.location.href = 'http://localhost:8000/auth/google/url'
}
</script>


