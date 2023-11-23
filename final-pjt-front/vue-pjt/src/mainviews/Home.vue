<template>
    <div v-if="store.isLogin">
      <h1 class="home-title">Home</h1>
      <div class="container">
        <RouterLink :to="{ name: 'products' }" class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/예적금.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">예적금 상품 정보</h5>
          </div>
        </RouterLink>
        <RouterLink :to="{ name: 'exchange' }" class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/환율.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">환율 정보</h5>
          </div>
        </RouterLink>
        <RouterLink :to="{ name: 'map' }" class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/지도.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">지도(map)</h5>
          </div>
        </RouterLink>
        <RouterLink :to="{ name: 'community' }" class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/커뮤니티.png" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Community</h5>
          </div>
        </RouterLink>
        <RouterLink :to="{ name: 'profile' }" class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/프로필.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">프로필</h5>
          </div>
        </RouterLink>
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" src="../그림/네이버증권.png" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">네이버 증권</h5>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="loginplz">
      로그인이 필요합니다!
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '../stores/counter'
  const store = useCounterStore()
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .card {
    border: 1px solid #3498db; /* Blue color */
    text-align: center;
    height: 300px;
    text-decoration-line: none;
    color: #3498db; /* Blue color */
  }
  
  .card:hover {
    background-color: #3498db; /* Blue color on hover */
    color: #fff; /* White text on hover */
  }
  
  .home-title {
    color: #3498db; /* Blue color */
  }
  
  img {
    height: 70%;
  }
  
  .audio-player {
    width: 100%;
    margin-top: 10px;
  }

  .loginplz{
    margin: 20px;
    font-size: xx-large;
    font-weight: bold;

  }
  </style>