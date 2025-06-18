<template>
  <div class="map-container">
    <h1 class="page-title">产区地图</h1>

    <!-- 地图展示区 -->
    <el-section class="map-display-section">
      <h2 class="section-title">粤西荔枝产区分布</h2>
      <div id="lychee-map" style="width: 100%; height: 600px;"></div>
    </el-section>

    <!-- 产区对比分析区 -->
    <el-section class="comparison-analysis-section">
      <h2 class="section-title">产区产量与品质对比</h2>
      <el-row :gutter="20">
        <el-col :span="12">
          <el-card class="chart-card">
            <h3>各产区产量（吨）</h3>
            <div id="yield-chart" style="width: 100%; height: 300px;"></div>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card class="table-card">
            <h3>产区品质特色对比</h3>
            <el-table :data="qualityData" style="width: 100%">
              <el-table-column prop="area" label="产区" width="120" />
              <el-table-column prop="mainVariety" label="主要品种" width="150" />
              <el-table-column prop="qualityFeature" label="品质特色" />
            </el-table>
          </el-card>
        </el-col>
      </el-row>
    </el-section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const qualityData = ref([
  {
    area: '茂名高州',
    mainVariety: '妃子笑、白糖罂',
    qualityFeature: '果大肉厚，清甜多汁，口感极佳'
  },
  {
    area: '湛江廉江',
    mainVariety: '雷州青、大红',
    qualityFeature: '肉质细嫩，风味浓郁，甜度高'
  },
  {
    area: '阳江阳西',
    mainVariety: '黑叶、怀枝',
    qualityFeature: '皮薄核小，汁多味甜，耐储存'
  }
])

onMounted(() => {
  initMapChart()
  initYieldChart()
})

const initMapChart = () => {
  const mapChart = echarts.init(document.getElementById('lychee-map'))
  // 这里需要加载广东地图的 geoJSON 数据
  // 为了演示，我们先使用一个简单的散点图代替，或者如果您有geoJSON数据，可以加载进来
  // 实际项目中，您需要从echarts-gl或geoJSON数据源获取并注册地图
  // 例如: echarts.registerMap('guangdong', yourGuangdongGeoJSON)

  const mapOption = {
    title: {
      text: '粤西荔枝产区示意图',
      left: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}<br/>产区面积: {c} 平方公里'
    },
    visualMap: {
      min: 0,
      max: 1000,
      left: 'left',
      top: 'bottom',
      text: ['高', '低'],
      calculable: true,
      inRange: {
        color: ['#e0ffff', '#006edd']
      }
    },
    series: [
      {
        name: '产区面积',
        type: 'map',
        map: 'china', // 暂时使用中国地图，实际应为guangdong
        roam: true,
        label: {
          show: true
        },
        data: [
          { name: '广东省', value: 800 }, // 示例数据
          { name: '广西省', value: 200 }, // 示例数据
          // 实际应为粤西各产区数据
        ]
      }
    ]
  }

  mapChart.setOption(mapOption)
}

const initYieldChart = () => {
  const yieldChart = echarts.init(document.getElementById('yield-chart'))
  const yieldOption = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: {
      type: 'category',
      data: ['茂名高州', '湛江廉江', '阳江阳西']
    },
    yAxis: {
      type: 'value',
      name: '产量 (吨)'
    },
    series: [
      {
        name: '产量',
        type: 'bar',
        data: [750, 600, 450],
        itemStyle: {
          color: new echarts.graphic.LinearGradient(
            0, 0, 0, 1,
            [
              { offset: 0, color: '#83bff6' },
              { offset: 0.5, color: '#188df0' },
              { offset: 1, color: '#188df0' }
            ]
          )
        },
        emphasis: {
          itemStyle: {
            color: new echarts.graphic.LinearGradient(
              0, 0, 0, 1,
              [
                { offset: 0, color: '#2378f7' },
                { offset: 0.7, color: '#2378f7' },
                { offset: 1, color: '#83bff6' }
              ]
            )
          }
        }
      }
    ]
  }
  yieldChart.setOption(yieldOption)
}
</script>

<style scoped>
.map-container {
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

.map-display-section,
.comparison-analysis-section {
  margin-bottom: 40px;
  background-color: var(--el-bg-color);
  padding: 30px;
  border-radius: 8px;
  box-shadow: var(--el-box-shadow-light);
}

.chart-card,
.table-card {
  margin-top: 20px;
}

.chart-card h3,
.table-card h3 {
  text-align: center;
  margin-bottom: 20px;
  color: var(--el-color-success);
}
</style> 