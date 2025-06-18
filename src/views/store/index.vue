<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import Nav from "@/views/zujian/nav.vue";
import Product from "@/views/zujian/product.vue";

let product_data = ref()

onMounted(() => {
  axios.get('http://127.0.0.1:55555/product').then((res) => {
    product_data.value = res.data.data
  })
})


</script>

<template>
  <Nav/>
  <div class="card_container">
    <div class="card_list">
      <Product v-for="(item, index) of product_data" :info="item" :key="index"></Product>
    </div>
  </div>
</template>

<style scoped>
.card_container {
  height: 100vh;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.card_list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  width: 100%; /* 让 .card_list 的宽度占据整个屏幕 */
  box-sizing: border-box; /* 防止边框和填充增加元素的宽度 */
}
</style>
