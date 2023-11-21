<template>
    <div>
        <header>
          <div v-if="store.isLogin">
            <nav class="nav d-flex justify-content-center align-items-center bg-dark text-white gap-10 ">
              <RouterLink :to="{name : 'home'}">HOME</RouterLink> 
              <RouterLink :to="{name : 'products'}">PRODUCTS</RouterLink> 
              <RouterLink :to="{name : 'exchange'}">EXCHANGE</RouterLink> 
              <RouterLink :to="{name : 'map'}">MAP</RouterLink> 
              <RouterLink :to="{name : 'community'}">COMMUNITY</RouterLink> 
              <RouterLink :to="{name : 'profile'}">PROFILE</RouterLink> 
              <!-- <RouterLink :to="{name : 'stock'}">STOCK</RouterLink>  -->
              <form @submit.prevent="store.logOut">
                <input type="submit" value="LogOut">
              </form>
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
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>
nav {
  /* background-color: black; */
  /* color: white; */
  height: 50px;
  /* text-align: center; */
  display: flex;
  /* justify-content: center; */
  /* align-items: center; */
  gap: 15px;
}

nav > a {
  color: white;
  text-decoration-line: none;
}

nav > form > input{
  background-color: rgba(0, 0, 0, 0);
  color: white;
  padding: 0;
  border: none;
  background: none;
}
</style>