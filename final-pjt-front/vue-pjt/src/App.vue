<template>
  <div>
    <header>
      <div v-if="store.isLogin">
        <div class="user-info">
          <div class="d-flex user-section">
            <audio controls class="audio-player" style="margin-right: auto;">
              <source src="./메이플스토리-헤네시스.mp3" type="audio/mp3">
              Your browser does not support the audio element.
            </audio>
              <div class="username">{{ store.UserDetail.username }}님 환영합니다!</div>
              <form @submit.prevent="store.logOut" class="logout-form">
                <input type="submit" value="Logout" style="background-color: #3498db;">
              </form>
          </div>
        </div>
        <nav class="nav d-flex justify-content-center align-items-center bg-blue text-white gap-10">
          <RouterLink :to="{ name: 'home' }">HOME</RouterLink>
          <RouterLink :to="{ name: 'products' }">PRODUCTS</RouterLink>
          <RouterLink :to="{ name: 'exchange' }">EXCHANGE</RouterLink>
          <RouterLink :to="{ name: 'map' }">MAP</RouterLink>
          <RouterLink :to="{ name: 'community' }">COMMUNITY</RouterLink>
          <RouterLink :to="{ name: 'profile' }">PROFILE</RouterLink>
        </nav>
      </div>
      <nav v-else>
        <RouterLink :to="{ name: 'SignUpView' }" style="color: black;">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'LogInView' }" style="color: black;">LogIn</RouterLink>
      </nav>
    </header>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';
import axios from 'axios';

const store = useCounterStore();


onMounted(() => {
  store.getUserDetail()
})
</script>

<style scoped>
nav {
  height: 50px;
  display: flex;
  gap: 15px;
}

nav > a {
  color: white;
  text-decoration-line: none;
}

nav > form > input {
  background-color: rgba(0, 0, 0, 0);
  color: white;
  padding: 0;
  border: none;
  background: none;
}


/* Added Styles */
header {
  background-color: #3498db; /* Blue color for the header */
}

.nav {
  background-color: #3498db; /* Blue color for the navigation */
  height: 50px;
  display: flex;
  justify-content: center; /* Center the content horizontally */
  align-items: center; /* Center the content vertically */
  gap: 10px;
}

.nav > a {
  color: white;
  text-decoration-line: none;
}

.nav > a:hover {
  color: #fff; /* White color on hover */
}

.nav > form > input {
  background-color: rgba(0, 0, 0, 0);
  color: white;
  padding: 0;
  border: none;
  background: none;
}

/* Styles for User Info Section */
.user-info {
  background-color: white; /* White color for the user info section */
  padding: 10px;
}

.user-section {
  display: flex;
  justify-content: flex-end;
  height: 50px;
  align-items: center;
}

.username {
  margin-right: 10px;
}

.logout-form {
  margin: 0; /* Remove default form margin */
}

.audio-player {
  width: 300px; /* Adjust the width as needed */
  margin-left: 0px; /* Move the audio player to the right */ /* Blue color for the audio player background */
  color: #fff; /* White color for the audio player text */ /* Blue border for the audio player */
}
</style>