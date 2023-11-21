<template>
    <div>
      <h1>Signup</h1>
      <form @submit.prevent="signUp">
        <div>
            <label for="Username">Username</label>
            <input type="text" id="Username" v-model.trim="username">
        </div>
        <div>
            <label for="password1">Password</label>
            <input type="password" id="password1" v-model.trim="password1">
        </div>
        <div>
            <label for="Confirm Password">Confirm Password</label>
            <input type="password" id="Confirm Password" v-model.trim="password2">
        </div>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  
  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signUp(payload)
  }
  
  
  </script>
  
  <style>
  
  </style>
  