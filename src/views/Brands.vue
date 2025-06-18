<template>
  <div class="brands-container">
    <h1 class="page-title">品牌农户信息</h1>

    <!-- 品牌展示区 -->
    <el-section class="brand-display-section">
      <h2 class="section-title">粤西荔枝品牌</h2>
      <el-row :gutter="20" justify="center">
        <el-col :span="6" v-for="brand in brands" :key="brand.id">
          <el-card class="brand-card" :body-style="{ padding: '20px' }">
            <img :src="brand.logo" class="brand-logo" :alt="brand.name + ' Logo'">
            <h3>{{ brand.name }}</h3>
            <p class="brand-story">{{ brand.story }}</p>
            <el-divider />
            <div class="brand-advantages">
              <h4>品牌优势</h4>
              <ul>
                <li v-for="advantage in brand.advantages" :key="advantage">{{ advantage }}</li>
              </ul>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-section>

    <!-- 农户信息卡片区 -->
    <el-section class="farmer-info-section">
      <h2 class="section-title">优质荔枝农户</h2>
      <el-row :gutter="20">
        <el-col :span="8" v-for="farmer in farmers" :key="farmer.id">
          <el-card class="farmer-card">
            <div class="farmer-header">
              <el-avatar :size="60" :src="farmer.avatar" class="farmer-avatar" />
              <div class="farmer-name-badges">
                <h3>{{ farmer.name }}</h3>
                <div class="badges">
                  <el-tag type="success" size="small" v-if="farmer.certified">认证农户</el-tag>
                  <el-tag type="info" size="small" v-if="farmer.topFarmer">明星农户</el-tag>
                </div>
              </div>
            </div>
            <p class="farmer-description">{{ farmer.description }}</p>
            <el-divider />
            <div class="farmer-details">
              <p><el-icon><Location /></el-icon> 产区：{{ farmer.region }}</p>
              <p><el-icon><Fruits /></el-icon> 主营品种：{{ farmer.mainVariety }}</p>
              <p><el-icon><Star /></el-icon> 用户评价：
                <el-rate
                  v-model="farmer.rating"
                  disabled
                  show-score
                  text-color="#ff9900"
                  score-template="{value} 分"
                />
              </p>
            </div>
            <el-button type="primary" plain class="view-more-button">查看详情</el-button>
          </el-card>
        </el-col>
      </el-row>
    </el-section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Location, Fruits, Star } from '@element-plus/icons-vue'

const brands = ref([
  {
    id: 1,
    name: '粤荔优品',
    logo: '/images/brands/brand_a.png',
    story: '专注于粤西荔枝的精选品牌，秉承传统种植工艺与现代技术相结合，致力于提供最优质的荔枝。',
    advantages: ['源头直采', '绿色有机', '新鲜速达', '品质保证']
  },
  {
    id: 2,
    name: '岭南果臻',
    logo: '/images/brands/brand_b.png',
    story: '深耕岭南水果市场多年，以荔枝为核心产品，致力于将粤西地道的风味传播至全国。',
    advantages: ['历史悠久', '品种丰富', '匠心种植', '口碑良好']
  },
  {
    id: 3,
    name: '荔园之星',
    logo: '/images/brands/brand_c.png',
    story: '新锐荔枝品牌，注重科技创新和品牌建设，旨在打造年轻化、时尚化的荔枝消费体验。',
    advantages: ['科技赋能', '创新包装', '定制服务', '年轻活力']
  }
])

const farmers = ref([
  {
    id: 1,
    name: '张大爷',
    avatar: '/images/farmers/farmer_1.png',
    description: '高州石硖龙眼、妃子笑荔枝种植专家，拥有30年果园管理经验。',
    region: '茂名高州',
    mainVariety: '妃子笑、白糖罂',
    rating: 4.8,
    certified: true,
    topFarmer: true
  },
  {
    id: 2,
    name: '李阿姨',
    avatar: '/images/farmers/farmer_2.png',
    description: '廉江红江橙、雷州青荔枝种植能手，坚持绿色生态种植。',
    region: '湛江廉江',
    mainVariety: '雷州青、大红',
    rating: 4.5,
    certified: true,
    topFarmer: false
  },
  {
    id: 3,
    name: '王小哥',
    avatar: '/images/farmers/farmer_3.png',
    description: '阳西黑叶荔枝新农人，积极学习新技术，致力于提升荔枝品质。',
    region: '阳江阳西',
    mainVariety: '黑叶、怀枝',
    rating: 4.2,
    certified: false,
    topFarmer: false
  }
])
</script>

<style scoped>
.brands-container {
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

.brand-display-section,
.farmer-info-section {
  margin-bottom: 40px;
  background-color: var(--el-bg-color);
  padding: 30px;
  border-radius: 8px;
  box-shadow: var(--el-box-shadow-light);
}

.brand-card {
  margin-bottom: 20px;
  text-align: center;
  transition: transform 0.3s;
}

.brand-card:hover {
  transform: translateY(-5px);
}

.brand-logo {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin-bottom: 15px;
}

.brand-card h3 {
  margin: 0 0 10px;
  font-size: 22px;
  color: var(--el-color-primary);
}

.brand-story {
  color: var(--el-text-color-regular);
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 15px;
}

.brand-advantages h4 {
  margin-top: 0;
  margin-bottom: 10px;
  color: var(--el-color-success);
}

.brand-advantages ul {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
}

.brand-advantages li {
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 5px;
}

.farmer-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.farmer-card:hover {
  transform: translateY(-5px);
}

.farmer-header {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.farmer-avatar {
  margin-right: 15px;
  flex-shrink: 0;
}

.farmer-name-badges h3 {
  margin: 0 0 5px;
  font-size: 20px;
  color: var(--el-color-primary);
}

.badges .el-tag {
  margin-right: 5px;
}

.farmer-description {
  color: var(--el-text-color-regular);
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 15px;
}

.farmer-details p {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  color: var(--el-text-color-secondary);
  font-size: 14px;
}

.farmer-details .el-icon {
  margin-right: 8px;
  color: var(--el-color-info);
}

.view-more-button {
  width: 100%;
  margin-top: 15px;
}
</style> 