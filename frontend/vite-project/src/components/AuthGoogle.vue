<template>
  <div class="auth-page">
    <RouterLink to="/" class="back-link">← Back to Home</RouterLink>

    <div class="container">
      <h1 v-if="!userName && !message" class="loading-text">Loading...</h1>
      <div v-if="message" class="message">{{ message }}</div>

      <div v-if="userName" class="welcome-text">
        Welcome, {{ userName }}!
      </div>

      <img v-if="picUrl" :src="picUrl" alt="Profile picture" class="avatar" />
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthGoogle",
  data() {
    return {
      message: "",
      userName: "",
      picUrl: "",
      accessToken: "",
    };
  },
  async mounted() {
    try {
      const queryParams = new URLSearchParams(window.location.search);
      const code = queryParams.get("code");

      if (!code) {
        this.message = "⚠ Missing 'code' parameter in URL";
        return;
      }

    //   const response = await fetch(`http://localhost:8000/auth/google/callback?code=${code}`, {
    //     credentials: "include",
    // });

      const response = await fetch("http://localhost:8000/auth/google/callback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code }),
        credentials: "include", // allow cookies/sessions if backend sets them
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      // Adjust according to your backend response structure
      const user = data.user_data || data.user || data;

      this.userName = user.name || "Unknown";
      this.picUrl = user.picture || "";
      this.accessToken = data.access_token || "";
    } catch (err) {
      console.error("Auth error:", err);
      this.message = "⚠ Authentication failed. Please try again.";
    }
  },
};
</script>

<style scoped>
.auth-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

.back-link {
  align-self: flex-start;
  margin-left: 20px;
  text-decoration: none;
  color: #007bff;
}

.container {
  text-align: center;
}

.loading-text {
  font-size: 1.5em;
  color: #666;
}

.message {
  color: red;
  font-weight: bold;
}

.welcome-text {
  font-size: 1.8em;
  margin-top: 20px;
  font-weight: 500;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-top: 20px;
  object-fit: cover;
  box-shadow: 0 0 8px rgba(0,0,0,0.3);
}
</style>