<!-- <template>
    <div>
      <button @click="toggleLike()" :class="{'liked': isLiked}">{{ likeCount }} 좋아요</button>
      <input type="hidden" v-model="csrfToken" name="csrfmiddlewaretoken">
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue';
  import axios from 'axios';
  import { useCounterStore } from '../stores/counter';

  const store = useCounterStore()
  const props = defineProps({
    article: Object,
    user: Object,  // 사용자 정보를 받아올 prop 추가
  });
  
  const articleId = ref(props.article.id);
  const isLiked = ref(props.user ? props.user.id in props.article.like_users : false);
  const likeCount = ref(props.article.like_users.count);
  const csrfToken = ref(document.getElementsByName('csrfmiddlewaretoken')[0].value);
  
  const toggleLike = function() {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/${articleId.value}/likes/`,
      data: {
        articleId: articleId.value,
        isLiked: isLiked.value,
        likeCount: likeCount.value,
        csrfToken: csrfToken.value,
      },
    })
      .then((res) => {
        console.log(res);
        isLiked.value = !isLiked.value;
        likeCount.value = res.data.like_count;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  </script>
  
  <style scoped>
  /* 스타일 작성 */
  </style>
   -->
<template>
    <div>
        <p>like</p>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>