<template>
    <div>
        <h1>Home</h1>
        <div class="container"> 
            <div class="card">예적금 상품 정보</div>    
            <div class="card">환율 정보</div>    
            <div class="card">지도(map)</div>    
            <div class="card">Community</div>    
            <div class="card">프로필</div>    
            <div class="card">네이버 증권</div>    
        </div>

    </div>
</template>

<script setup>

</script>

<style scoped>
.container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.card {
    width: 30%;
    height: 100px;
    border: 1px solid black;
}



</style>