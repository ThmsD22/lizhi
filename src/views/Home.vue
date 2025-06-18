<template>
  <div class="home-container">
    <!-- 搜索区域 -->
    <div class="search-section">
      <el-input
        v-model="searchQuery"
        placeholder="搜索荔枝品种、产区、活动..."
        class="search-input"
        :prefix-icon="Search"
      >
        <template #append>
          <el-button type="primary">搜索</el-button>
        </template>
      </el-input>
    </div>

    <!-- 轮播图区域 -->
    <div class="carousel-section">
      <el-carousel height="400px">
        <el-carousel-item v-for="item in carouselItems" :key="item.id">
          <div class="carousel-content" :style="{ backgroundImage: `url(${item.image})` }">
            <div class="carousel-text">
              <h2>{{ item.title }}</h2>
              <p>{{ item.description }}</p>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>

    <!-- 活动推荐区 -->
    <div class="activities-section">
      <h2 class="section-title">精彩活动</h2>
      <el-row :gutter="20">
        <el-col :span="8" v-for="activity in activities" :key="activity.id">
          <el-card class="activity-card" :body-style="{ padding: '0px' }">
            <img :src="activity.image" class="activity-image">
            <div class="activity-info">
              <h3>{{ activity.title }}</h3>
              <p>{{ activity.description }}</p>
              <el-button type="primary" plain>了解详情</el-button>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'

const searchQuery = ref('')

const carouselItems = ref([
  {
    id: 1,
    title: '粤西荔枝果园美景',
    description: '探索荔枝之乡的自然风光',
    image: '/images/carousel/orchard.jpg'
  },
  {
    id: 2,
    title: '特色品种展示',
    description: '品味不同品种的独特风味',
    image: '/images/carousel/varieties.jpg'
  },
  {
    id: 3,
    title: '荔枝文化节',
    description: '感受传统与现代的完美融合',
    image: '/images/carousel/festival.jpg'
  }
])

const activities = ref([
  {
    id: 1,
    title: '新品种试吃会',
    description: '体验最新培育的荔枝品种，感受科技与自然的完美结合',
    image: '/images/activities/tasting.jpg'
  },
  {
    id: 2,
    title: '荔枝采摘节',
    description: '亲手采摘新鲜荔枝，体验农家乐趣',
    image: '/images/activities/picking.jpg'
  },
  {
    id: 3,
    title: '荔枝文化讲座',
    description: '深入了解荔枝文化，探索历史渊源',
    image: '/images/activities/lecture.jpg'
  }
])
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
}

.search-section {
  margin: 20px 0;
}

.search-input {
  max-width: 600px;
  margin: 0 auto;
  display: block;
}

.carousel-section {
  margin: 20px 0;
}

.carousel-content {
  height: 100%;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
}

.carousel-text {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 20px;
  width: 100%;
}

.carousel-text h2 {
  margin: 0;
  font-size: 24px;
}

.carousel-text p {
  margin: 10px 0 0;
  font-size: 16px;
}

.section-title {
  text-align: center;
  margin: 40px 0 20px;
  color: var(--el-text-color-primary);
}

.activity-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.activity-card:hover {
  transform: translateY(-5px);
}

.activity-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.activity-info {
  padding: 20px;
}

.activity-info h3 {
  margin: 0 0 10px;
  font-size: 18px;
}

.activity-info p {
  margin: 0 0 15px;
  color: var(--el-text-color-secondary);
  font-size: 14px;
}
</style> 