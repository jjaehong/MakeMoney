<template>
  <div class="container">
    <h3>게시글 목록</h3>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
// console.log(store.articles)
</script>

<style scoped >
.container {
  margin: 20px;
}
</style>
