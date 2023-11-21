<template>
    <div>
        <header>
            <nav class="nav d-flex justify-content-center align-items-center bg-dark text-white gap-10 ">
                <RouterLink :to="{name : 'home'}">HOME</RouterLink> 
                <RouterLink :to="{name : 'products'}">PRODUCTS</RouterLink> 
                <RouterLink :to="{name : 'exchange'}">EXCHANGE</RouterLink> 
                <RouterLink :to="{name : 'map'}">MAP</RouterLink> 
                <RouterLink :to="{name : 'community'}">COMMUNITY</RouterLink> 
                <RouterLink :to="{name : 'profile'}">PROFILE</RouterLink> 
                <RouterLink :to="{name : 'test'}">TEST</RouterLink> 
                <!-- <RouterLink :to="{name : 'stock'}">STOCK</RouterLink>  -->
                
            </nav>
        </header>
        <RouterView/>
        
    </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';




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

}

</style>