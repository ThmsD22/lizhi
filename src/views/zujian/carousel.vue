<script setup>
import {ref} from "vue";

let images = [
  "https://tse2-mm.cn.bing.net/th/id/OIP-C.m6SRZGaewzZQjQDpEYRo3gHaE-?rs=1&pid=ImgDetMain\n",
    "https://etang.com/wp-content/uploads/2022/10/2022102908443766.jpg",
    "https://img-qn-1.51miz.com/preview/video/00/00/12/62/V-126241-F4DFBE7B.jpg",
    "https://img-u-3.51miz.com/Templet/00/19/52/19/195219_c3e8071348f03e0b00338825d8d4992d.jpg-0.jpg"

];

let image_index = 0;

let image_src = ref(images[0])

setInterval(() => {
  image_src.value = images[(image_index += 1) % 4]
}, 2000)
</script>

<template>
  <div class="images_box">
    <!--    <a @click="prevSlide" class="prev">&lt;</a>-->
    <a href="#">
      <img :src="image_src" class="images" alt="alt">
    </a>
    <!--    <a @click="nextSlide" class="next">&gt;</a>-->
  </div>
</template>

<style scoped>
.images_box {
  margin-top: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  width: 100%;
  height: 500px;
  background-color: rgba(255, 255, 255, 0.4);
}

.images_box img {
  width: 1170px;
  height: 500px;

}
.images {
  width: 800px;
  height: 400px;
}

</style>
