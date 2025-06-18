<script setup>
import Nav from "@/views/zujian/nav.vue";
import Shop from "@/views/zujian/shop.vue";
import {onMounted, ref} from "vue";
import axios from "axios";

let product = ref()

onMounted(() => {
  axios.get('http://127.0.0.1:55555/cart_data').then((res) => {
    product.value = res.data.data
  })
});
</script>

<template>

  <Nav></Nav>
  <Shop :product="product"></Shop>

</template>

<style scoped>

</style>
