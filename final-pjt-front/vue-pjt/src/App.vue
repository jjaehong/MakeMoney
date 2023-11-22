<template>
  <div>
    <header>
      <div v-if="store.isLogin">
        <form @submit.prevent="store.logOut">
            <input type="submit" value="LogOut">
          </form>
        <!-- <h3>{{ user.username }}님 환영합니다!</h3>  -->
        <nav class="nav d-flex justify-content-center align-items-center bg-blue text-white gap-10">
          <RouterLink :to="{ name: 'home' }">HOME</RouterLink>
          <RouterLink :to="{ name: 'products' }">PRODUCTS</RouterLink>
          <RouterLink :to="{ name: 'exchange' }">EXCHANGE</RouterLink>
          <RouterLink :to="{ name: 'map' }">MAP</RouterLink>
          <RouterLink :to="{ name: 'community' }">COMMUNITY</RouterLink>
          <RouterLink :to="{ name: 'profile' }">PROFILE</RouterLink>
          <!-- <RouterLink :to="{ name : 'stock' }">STOCK</RouterLink>  -->
        </nav>
        <audio controls class="audio-player">
          <source src="./메이플스토리-헤네시스.mp3" type="audio/mp3">
          Your browser does not support the audio element.
        </audio>
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

// Uncomment and modify the code according to your needs
// onMounted(() => {
//   axios({
//     method: 'get',
//     url: `accounts/`
//   })
//     .then((res) => {
//       console.log(res)
//     })
//     .catch((err) => {
//       console.log(err)
//     })
// })
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

.audio-player {
  width: 100%;
  margin-top: 10px;
}

/* Added Styles */
header {
  background-color: #3498db; /* Blue color */
  padding: 10px;
}

/* Style for navigation links on hover */
nav > a:hover {
  color: #fff; /* White color on hover */
}

/* Style for the audio player */
.audio-player {
  width: 100%;
  margin-top: 10px;
  background-color: #3498db; /* Blue color */
  color: #fff; /* White color */
  border: 1px solid #3498db; /* Blue border */
}

/* Style for the audio player controls on hover */
.audio-player:hover {
  background-color: #2980b9; /* Darker blue color on hover */
  border: 1px solid #2980b9; /* Darker blue border on hover */
}
</style>