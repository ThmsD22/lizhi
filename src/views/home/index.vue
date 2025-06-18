<template>
    <Nav/>
    <Carousel/>
    <Recommendations :goods="recommendationgoods"/>
    <jiaoyibang :jiaoyibangs="jiaoyibangList"></jiaoyibang>
    <Hot :hots="hotList"></Hot>
</template>


<script setup>
import Nav from "@/views/zujian/nav.vue";
import Carousel from "@/views/zujian/carousel.vue";
import Recommendations from "@/views/zujian/recommend.vue"
import Hot from "@/views/zujian/hot.vue";
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

  console.log(jiaoyibangList)
})

</script>


<style scoped>

</style>
