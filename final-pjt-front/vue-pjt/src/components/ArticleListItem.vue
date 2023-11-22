<template>
    <div style="border: 1px solid lightgrey; margin-bottom: 15px;">
    <h5 class="article-id">게시물 번호: {{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <p>좋아요 갯수</p>
    <p> 댓글 {{ article.comment_count }}</p>
    <hr class="separator">
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    
    <hr>
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