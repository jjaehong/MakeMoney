<template>
  <div class="container">
    <h3>게시글 목록</h3>
    <div v-for="article in store.articles" :key="article.id" style="border: 1px solid lightgrey; margin-bottom: 15px;">
      <div class="d-flex justify-content-between">
        <p> 작성자 : {{ computedName1 }} </p>
        <p>{{ article.updated_at }}</p>
      </div>
      <div>
        <h4 class="article-title">{{ article.title }}</h4>
        <p>{{ article.content }}</p>
      </div>
      <div class="d-flex gap-3" >
        <p>좋아요 {{ article.like_users.length }} </p>
        <p> 댓글 {{ article.comment_count }}</p>
      </div>
      <hr class="separator">
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
        [Detail]
      </RouterLink>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import axios from 'axios';

const store = useCounterStore();

// Ensure the computed property is accessible in the template
const computedName1 = ref(store.uu.username);

onMounted(() => {
  store.getArticles();
  store.getUserDetail();
  axios()
});
</script>

<style scoped>
.container {
  margin: 20px;
}
.article-title {
  color: #3498db;
}
.article-content {
  color: #2c3e50;
}

.detail-link {
  color: #3498db;
  text-decoration: none;
  margin-top: 10px;
  display: inline-block;
}

.separator {
  border-color: #3498db;
  margin-top: 15px;
}
</style>
