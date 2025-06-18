<script setup>
import {onMounted, ref} from 'vue'
import axios from "axios";

let pro = defineProps(['product'])

// TODO: implement the function of add and decrease
let add = () => {
}
let decrease = () => {
}
</script>

<template>
  <div class="mainbox">
    <div class="cart">
      <div class="card_box" v-for="item of pro.product">
        <div class="card">
          <a href="/xiangqing">
            <h3 class="sign">店铺名称:
              <span class="sign-name">{{ item.storeName }}</span>
            </h3>
          </a>
          <a href="/xiangqing">
            <img :src="item.img" class="picture">
          </a>
          <div class="info">
            <a href="/xiangqing">
              <p class="p-info">{{ item.info }}</p>
            </a>
          </div>
          <div class="price">价格:
            <span class="price-info"> ￥{{ item.price }}</span>
            <button class="down" @click="decrease">--</button>
            <span class="count"> x{{ item.count }}</span>
            <button class="up" @click="add">+</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mainbox {
  margin-top: 70px;
}

.cart {
  padding: 20px;
  margin-top: 10px;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}
.sign {
  font-size: 25px;
  font-family: Aharoni, serif;
}

.info {
  margin: 0 0 10px;
  text-align: left;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  -webkit-line-clamp: 2;
}
.card_box {
  background-color: rgba(240, 240, 240, 0.9);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  padding-left: 10px;
  margin-top: 20px;
  margin-left: 18%;
  width: 60%;
  height: 150px;
}

.sign-name {
  font-size: 1.15em;
  font-family: Aharoni, serif;
  color: orange;
}

.picture {
  width: 110px;
  display: flex;
  float: left;
}

.p-info {
  font-size: 1.5em;
  font-family: Aharoni, serif;
  font-weight: 200;
  margin-left: 20px;
}

.count {
  color: #333333;
  position: relative;
  display: flex;
  right: -55%;
}

.price {
  display: flex;
  position: relative;
  bottom: -5px;
  font-size: 2em;
  margin-left: 130px;
}

.price .price-info {
  color: rgba(202, 38, 38, 0.9);
}

.down {
  width: 28px;
  height: 28px;
  position: relative;
  display: flex;
  right: -50%;
  margin-top: 5px;
  line-height: 100%;
}

.up {
  width: 28px;
  height: 28px;
  position: relative;
  display: flex;
  right: -60%;
  margin-top: 5px;
  line-height: 100%;
}
</style>
