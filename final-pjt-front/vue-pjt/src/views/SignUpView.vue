<template>
  <div>
    <h1 class="fw-bold">MOMM</h1>
    <div class="login">
      <h1 class="signup-title">회원가입</h1>
      <form @submit.prevent="signUp" class="signup-form">
        <div class="form-group">
          <label for="Username" class="label">Username</label>
          <input type="text" id="Username" v-model.trim="username" class="form-input">
        </div>
        <div class="form-group">
          <label for="password1" class="label">Password</label>
          <input type="password" id="password1" v-model.trim="password1" class="form-input">
        </div>
        <div class="form-group">
          <label for="password2" class="label">Confirm Password</label>
          <input type="password" id="password2" v-model.trim="password2" class="form-input">
        </div>
        <button type="submit" class="btn-submit">Sign Up</button>
      </form>
    </div>
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

<style scoped>


.login {
  width: 500px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f4f4f4;
  border: 2px solid #3498db;
  border-radius: 5px;
  text-align: center;
}

.signup-title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.signup-form {
  width: 300px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 15px;
}

.label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  box-sizing: border-box;
}

.btn-submit {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
  width: 100%;
}
</style>
