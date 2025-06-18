<script setup>
let card = defineProps(['info'])
// console.log("12356",card.info.title)
</script>

<template>
  <div class="mainbox">
    <div class="card">
      <img :src="card.info.img" class="picture">
      <h4>{{ card.info.title }}</h4>
      <div class="author">
        <img src="/favicon.ico" class="avatar">
         <span>发布者:{{ card.info.author }}</span></div>
      <div class="title">商品名称: <span>{{ card.info.date }}</span></div>
      <div class="click">浏览量: <span>{{ card.info.text }}</span></div>
      <div  class="price">价格￥: <span>{{ card.info.type }}</span></div>
    </div>
  </div>
</template>

<style scoped>
.card {
  width: 250px;
  height: 450px;
  margin: 15px; /* 调整卡片之间的垂直间距 */
  background-color: rgba(240, 240, 240, 0.9);
  border-radius: 10px;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  float: left;
}

.mainbox {
  margin-top: 75px;
}

.author img{
  width:40px;
}
.picture {
  width: 100%;
  height: 60%;
  border-radius: 5px;
  margin-bottom: 5px;
}

.avatar {
  width: 30%;
  border-radius: 50%;
  margin-right: 10px;
}

.card h4 {
  margin: 0 0 10px;
  text-align: left;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  -webkit-line-clamp: 2;
}

.card p {
  margin: 0 0 10px;
}

.title {
  margin: 10px 0;
  text-align: left;
  color: black;
}

.author {
  margin: 10px 0;
  text-align: left;
  color: #4caf50;
  font-size: 15px;
  display: flex;
  flex-wrap: nowrap;
  justify-content: flex-start;
}

.click {
  margin: 10px 0;
  text-align: left;
  color: blue;
}

.price {
  margin: 10px 0;
  font-style: italic;
  text-align: left;
  color: red;
  font-weight: bold;
  font-size: 20px;
}
.author span{
  line-height: 40px;
}
</style>
