<template>
  <Nav/>
  <div class="product-detail">
    <div class="product-header">商品详情</div>
    <div class="product-content">
      <div class="product-images">
        <!-- 商品图片展示区域 -->
        <img class="product-image1" src="https://pic1.zhimg.com/v2-7a4cd2d5c54deba8df8be116bc6e6d6d_r.jpg?source=1940ef5c">
        <img class="product-image2" src="https://gfs17.gomein.net.cn/T1glWhBbDv1RCvBVdK_800.jpg">
        <img class="product-image3" src="https://tse1-mm.cn.bing.net/th/id/OIP-C.TUJrWGX6Ve75FRVkGOWJdgHaFj?w=216&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7">
      </div>
      <div class="product-info">
        <!-- 商品信息展示区域 -->
        <h2>iphone 15 pro</h2>
        <p class="jieshao">256G，98%新买来不到一个月，买到就是赚到</p>
        <div class="price">￥8199</div>
        <button class="add-to-cart">
          商品详情选购
        </button>
      </div>
    </div>
    <div class="product-footer">©恐龙集市——成都理工大学专门的二手交易市场</div>
  </div>
  <Recommendations :goods="recommendationgoods"/>
  <jiaoyibang :jiaoyibangs="jiaoyibangList"></jiaoyibang>
  <Hot :hots="hotList"></Hot>
</template>

<script setup>
import Nav from "@/views/zujian/nav.vue";
import Hot from "@/views/zujian/hot.vue";
import Recommendations from "@/views/zujian/recommend.vue";
import jiaoyibang from "@/views/zujian/jiaoyibang.vue";

import axios from "axios";
import {onMounted, ref} from "vue";

let jiaoyibangList = ref()
let recommendationgoods = ref()
let hotList = ref()

onMounted(() => {
  axios.get('http://127.0.0.1:55555/home').then((res) => {
    recommendationgoods.value = res.data.tuijian
    jiaoyibangList.value = res.data.jiaoyi
    hotList.value = res.data.redu
  })
})

</script>

<style scoped>
.product-detail {
  width: 1170px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-header {
  padding: 15px;
  background-color: #87ca9a;
  color: white;
  text-align: center;
  font-size: 24px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.product-content {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
}

.product-images {
  display: flex;
}

.product-image1,
.product-image2,
.product-image3 {
  width: 300px;
  height: 300px;
  margin-bottom: 10px; /* 统一设置图片的 margin-bottom */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-image1:hover,
.product-image2:hover,
.product-image3:hover {
  transform: scale(1.1);
}

.product-info {
  flex: 1;
  padding: 20px; /* 减小商品详情的 padding */
}

.product-info h2 {
  font-size: 30px;
  margin-top: 30px;
  margin-bottom: 20px;
  color: black;
}

.product-info .jieshao{
  font-size: 20px;
  color: purple;
  margin-bottom: 20px;
}

.price {
  font-size: 30px;
  color: red;
  margin-bottom: 20px;
}

.add-to-cart {
  background: #5FB878;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  border-radius: 4px;
}

.product-footer {
  padding: 15px;
  background-color: #87ca9a;
  color: white;
  text-align: center;
  font-size: 16px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
}
.product-detail {
  margin-top: 80px;
}
</style>
