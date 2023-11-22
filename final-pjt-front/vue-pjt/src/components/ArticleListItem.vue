<template>
  <div style="border: 1px solid lightgrey; margin-bottom: 15px;">
    <h5 class="article-id">게시물 번호: {{ article.id }}</h5>
    <p class="article-title">제목 : {{ article.title }}</p>
    <p class="article-content">내용 : {{ article.content }}</p>
    <hr class="separator">
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}" class="detail-link">
      [Detail]
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

<style scoped>
/* Blue theme styles */
.article-id {
  color: #3498db; /* Blue color */
}

.article-title,
.article-content {
  color: #2c3e50; /* Darker text color for better readability */
}

.detail-link {
  color: #3498db; /* Blue color for the link */
  text-decoration: none;
  margin-top: 10px; /* Adjust as needed */
  display: inline-block;
}

.separator {
  border-color: #3498db; /* Blue color for the separator line */
  margin-top: 15px; /* Adjust as needed */
}
</style>