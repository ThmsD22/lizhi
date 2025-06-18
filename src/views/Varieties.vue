<template>
  <div class="varieties-container">
    <h1 class="page-title">品种文化</h1>

    <!-- 品种展示区 -->
    <el-section class="variety-display-section">
      <h2 class="section-title">粤西荔枝品种</h2>
      <el-row :gutter="20">
        <el-col :span="8" v-for="variety in varieties" :key="variety.id">
          <el-card class="variety-card" :body-style="{ padding: '0px' }">
            <img :src="variety.image" class="variety-image">
            <div class="variety-info">
              <h3>{{ variety.name }}</h3>
              <p class="description">{{ variety.description }}</p>
              <el-divider />
              <p class="story">{{ variety.story }}</p>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-section>

    <!-- 文化长廊区 -->
    <el-section class="cultural-corridor-section">
      <h2 class="section-title">荔枝文化长廊</h2>
      <el-timeline>
        <el-timeline-item
          v-for="(activity, index) in culturalEvents"
          :key="index"
          :timestamp="activity.timestamp"
          placement="top"
        >
          <el-card>
            <h4>{{ activity.title }}</h4>
            <p>{{ activity.content }}</p>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </el-section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const varieties = ref([
  {
    id: 1,
    name: '妃子笑',
    description: '果大核小，果皮鲜红，肉质晶莹剔透，清甜多汁，是早熟荔枝中的佳品。\n因唐代杨贵妃喜食而得名。',
    story: '“一骑红尘妃子笑，无人知是荔枝来。”这句诗描绘了妃子笑荔枝与杨贵妃的传说，流传至今。',
    image: '/images/varieties/feizixiao.jpg'
  },
  {
    id: 2,
    name: '桂味',
    description: '果实中等大小，果皮薄且脆，肉质细嫩爽脆，带有独特的桂花香味，因此得名。',
    story: '桂味荔枝以其独特的清香和卓越的口感，深受食客喜爱，是送礼佳品。',
    image: '/images/varieties/guiwei.jpg'
  },
  {
    id: 3,
    name: '糯米糍',
    description: '果形扁圆，果肉厚实，核小，味道极甜，口感软糯如糯米糍。',
    story: '糯米糍因其软糯香甜的特点而闻名，是荔枝中的极品，产量稀少。',
    image: '/images/varieties/nuomicix.jpg'
  }
])

const culturalEvents = ref([
  {
    timestamp: '公元前2世纪',
    title: '荔枝南迁',
    content: '西汉时期，荔枝开始从岭南地区向中原移植，但因气候不适未能成功。'
  },
  {
    timestamp: '唐朝',
    title: '贵妃嗜荔',
    content: '唐玄宗为杨贵妃从岭南运送荔枝，成就了"一骑红尘妃子笑"的典故。'
  },
  {
    timestamp: '宋朝',
    title: '荔枝诗词繁盛',
    content: '苏轼、欧阳修等文人墨客留下大量咏荔诗篇，将荔枝文化推向高峰。'
  },
  {
    timestamp: '明清时期',
    title: '荔枝种植普及',
    content: '荔枝种植技术和品种不断改良，各地荔枝园规模扩大，成为重要经济作物。'
  },
  {
    timestamp: '当代',
    title: '粤西荔枝产业发展',
    content: '现代农业技术引入，粤西荔枝产业蓬勃发展，成为国家地理标志产品，并举办荔枝文化节。'
  }
])
</script>

<style scoped>
.varieties-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  text-align: center;
  margin-bottom: 40px;
  color: var(--el-text-color-primary);
  font-size: 36px;
}

.section-title {
  text-align: center;
  margin: 40px 0 30px;
  color: var(--el-text-color-primary);
  font-size: 28px;
}

.variety-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.variety-card:hover {
  transform: translateY(-5px);
}

.variety-image {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.variety-info {
  padding: 20px;
}

.variety-info h3 {
  margin: 0 0 10px;
  font-size: 22px;
  color: var(--el-color-primary);
}

.variety-info .description {
  color: var(--el-text-color-regular);
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 15px;
  white-space: pre-wrap; /* 保持换行符 */
}

.variety-info .story {
  color: var(--el-text-color-secondary);
  font-style: italic;
  font-size: 14px;
}

.cultural-corridor-section {
  margin-top: 60px;
}

.el-timeline {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px 0;
}

.el-timeline-item {
  padding-bottom: 30px;
}

.el-timeline-item__timestamp {
  font-size: 16px;
  color: var(--el-text-color-primary);
}

.el-card {
  background-color: var(--el-fill-color-light);
  border: none;
  box-shadow: var(--el-box-shadow-light);
}

.el-card h4 {
  margin-top: 0;
  font-size: 18px;
  color: var(--el-color-success);
}

.el-card p {
  color: var(--el-text-color-regular);
  line-height: 1.6;
}
</style> 