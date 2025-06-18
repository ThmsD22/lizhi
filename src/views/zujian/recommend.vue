<script setup>
let rec = defineProps(['goods'])
</script>

<template>
  <div class="recommend">
    <div class="recommendations">
      <h2>推荐榜</h2>
      <ul v-for="(goods, index) in rec.goods" :key="goods.id" class="goods-list">
        <li class="goods-item">
          {{index+=1}}.
          <a href="/xiangqing">{{ goods.title }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.recommend {
    border-radius: 5px;
  background-color: rgb(245, 245, 245);
  width: 25%;
  display: flex;
  float: left;
  margin-top: 20px ;
  margin-left: 170px;
  margin-right: 15px;
}

.recommendations h2{
  font-family: Arial;
}

.goods-list {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
  margin: 0;
}

.goods-item {
  font-family: fantasy;
  font-weight: 300;
  flex: 1; /* 设置 li 元素的宽度平均分配，可以根据需要调整 */
  margin: 0 10px 10px 0; /* 设置 li 元素之间的间距，可以根据需要调整 */
}
.goods-item a{
  text-decoration: none;
}
</style>
