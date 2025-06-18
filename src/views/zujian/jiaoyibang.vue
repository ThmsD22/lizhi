<script setup>
let jiaoyibanglist = defineProps(['jiaoyibangs'])
</script>

<template>
  <div class="jiaoyibangs">
    <div class="jiaoyibang-list">
      <h2>交易榜</h2>
      <ul v-for="(jiaoyibang, index) in jiaoyibanglist.jiaoyibangs" :key="jiaoyibang.id" class="jiaoyibang">
        <li class="jiaoyibang-item">
          {{index+=1}}.
          <a href="/xiangqing">{{ jiaoyibang.title }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.jiaoyibangs {
  border-radius: 5px;
  background-color: rgb(245, 245, 245);
  width: 25%;
  display: flex;
  float: left;
  margin-top: 20px ;

}

.jiaoyibang-list h2{
  font-family: Arial, sans-serif;
}

.jiaoyibang {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
  margin: 0;
}

.jiaoyibang-item {
  font-family: fantasy;
  font-weight: 300;
  flex: 1; /* 设置 li 元素的宽度平均分配，可以根据需要调整 */
  margin: 0 10px 10px 0; /* 设置 li 元素之间的间距，可以根据需要调整 */
}
.jiaoyibang-item a {
  text-decoration: none;
}
</style>
