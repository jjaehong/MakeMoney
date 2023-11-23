<template>
    <div>
      <h1>게시글 페이지</h1>
      <RouterLink :to="{ name: 'CreateView' }" class="create">
        [CREATE]
      </RouterLink>
      <ArticleList />
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink } from 'vue-router'
  import ArticleList from '@/components/ArticleList.vue'
  
  const store = useCounterStore()
  
  // console.log(store.UserDetail)


  onMounted(() => {
    store.getArticles()
    store.getUserDetail()
  })

  
  </script>
  
  <style scoped>
  h1 {
    margin: 20px;
  }

  .create {
    margin: 30px;
  }


  </style>