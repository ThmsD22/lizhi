<template>
  <div class="media-container">
    <h1 class="page-title">视频图文展示</h1>

    <!-- 视频展示区 -->
    <el-section class="video-display-section">
      <h2 class="section-title">荔枝精彩视频</h2>
      <el-row :gutter="20">
        <el-col :span="12" v-for="video in videos" :key="video.id">
          <el-card class="video-card" :body-style="{ padding: '0px' }">
            <video :src="video.url" controls class="video-player"></video>
            <div class="video-info">
              <h3>{{ video.title }}</h3>
              <p>{{ video.description }}</p>
              <div class="video-stats">
                <span><el-icon><View /></el-icon> {{ video.views }}</span>
                <span><el-icon><ChatDotSquare /></el-icon> {{ video.comments }}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-section>

    <!-- 用户留言区 -->
    <el-section class="comments-section">
      <h2 class="section-title">用户留言</h2>
      <el-input
        v-model="newComment"
        :rows="3"
        type="textarea"
        placeholder="留下您的宝贵留言..."
      />
      <div class="comment-actions">
        <el-button type="primary" @click="addComment">提交留言</el-button>
        <el-select v-model="filterOption" placeholder="筛选留言" class="filter-select">
          <el-option label="最新" value="latest" />
          <el-option label="热门" value="popular" />
          <el-option label="所有" value="all" />
        </el-select>
      </div>
      <el-card class="comment-list-card">
        <div v-for="comment in filteredComments" :key="comment.id" class="comment-item">
          <div class="comment-header">
            <span class="comment-author">{{ comment.author }}</span>
            <span class="comment-date">{{ comment.date }}</span>
          </div>
          <p class="comment-content">{{ comment.content }}</p>
        </div>
        <el-empty v-if="filteredComments.length === 0" description="暂无留言" />
      </el-card>
    </el-section>

    <!-- 互动话题区 -->
    <el-section class="topics-section">
      <h2 class="section-title">热门互动话题</h2>
      <el-row :gutter="20">
        <el-col :span="8" v-for="topic in topics" :key="topic.id">
          <el-card class="topic-card">
            <h3>{{ topic.title }}</h3>
            <p>{{ topic.description }}</p>
            <el-button type="text" class="discussion-button">参与讨论 ({{ topic.discussions }})</el-button>
          </el-card>
        </el-col>
      </el-row>
    </el-section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { View, ChatDotSquare } from '@element-plus/icons-vue'

const videos = ref([
  {
    id: 1,
    title: '荔枝种植全过程',
    description: '从育苗到丰收，带您了解荔枝的生长之旅。 ',
    url: '/videos/planting.mp4',
    views: 12345,
    comments: 234
  },
  {
    id: 2,
    title: '美味荔枝美食制作',
    description: '用新鲜荔枝制作创意甜点和饮品，简单易学。 ',
    url: '/videos/cooking.mp4',
    views: 9876,
    comments: 150
  }
])

const newComment = ref('')
const comments = ref([
  {
    id: 1,
    author: '荔枝爱好者1号',
    date: '2024-07-20',
    content: '视频拍得真好，对荔枝种植有了更深入的了解！',
    type: 'latest'
  },
  {
    id: 2,
    author: '美食达人小李',
    date: '2024-07-19',
    content: '荔枝美食看起来太诱人了，周末就动手尝试！',
    type: 'popular'
  },
  {
    id: 3,
    author: '果园老王',
    date: '2024-07-18',
    content: '作为一名荔枝种植户，看到这些视频感到非常骄傲！',
    type: 'latest'
  }
])
const filterOption = ref('latest')

const addComment = () => {
  if (newComment.value.trim() !== '') {
    comments.value.unshift({
      id: comments.value.length + 1,
      author: '匿名用户',
      date: new Date().toISOString().slice(0, 10),
      content: newComment.value.trim(),
      type: 'latest'
    })
    newComment.value = ''
  }
}

const filteredComments = computed(() => {
  if (filterOption.value === 'all') {
    return comments.value
  } else if (filterOption.value === 'latest') {
    return comments.value.sort((a, b) => new Date(b.date) - new Date(a.date))
  } else if (filterOption.value === 'popular') {
    // 假设popular是根据某个互动数据排序，这里简单模拟
    return comments.value.sort((a, b) => b.id - a.id) // 实际中需要根据点赞数等
  }
  return comments.value
})

const topics = ref([
  {
    id: 1,
    title: '你最喜欢哪种荔枝品种？',
    description: '分享你心中最美味的荔枝品种及其独特之处。',
    discussions: 128
  },
  {
    id: 2,
    title: '荔枝除了直接吃还能怎么做？',
    description: '发挥你的创意，分享荔枝的各种吃法和美食食谱。',
    discussions: 95
  },
  {
    id: 3,
    title: '对荔枝文化有什么独到见解？',
    description: '从历史、民俗、艺术等角度，探讨荔枝文化的魅力。',
    discussions: 72
  }
])
</script>

<style scoped>
.media-container {
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

.video-display-section,
.comments-section,
.topics-section {
  margin-bottom: 40px;
  background-color: var(--el-bg-color);
  padding: 30px;
  border-radius: 8px;
  box-shadow: var(--el-box-shadow-light);
}

.video-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.video-card:hover {
  transform: translateY(-5px);
}

.video-player {
  width: 100%;
  height: 300px;
  background-color: black;
}

.video-info {
  padding: 20px;
}

.video-info h3 {
  margin: 0 0 10px;
  font-size: 22px;
  color: var(--el-color-primary);
}

.video-info p {
  color: var(--el-text-color-regular);
  font-size: 15px;
  margin-bottom: 15px;
}

.video-stats span {
  margin-right: 20px;
  color: var(--el-text-color-secondary);
  display: inline-flex;
  align-items: center;
}

.video-stats .el-icon {
  margin-right: 5px;
}

.comments-section .el-input {
  margin-bottom: 15px;
}

.comment-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.filter-select {
  width: 120px;
}

.comment-list-card {
  margin-top: 20px;
}

.comment-item {
  border-bottom: 1px solid var(--el-border-color-light);
  padding: 15px 0;
}

.comment-item:last-child {
  border-bottom: none;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.comment-author {
  font-weight: bold;
  color: var(--el-text-color-primary);
}

.comment-date {
  font-size: 13px;
  color: var(--el-text-color-secondary);
}

.comment-content {
  color: var(--el-text-color-regular);
  line-height: 1.6;
}

.topic-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.topic-card:hover {
  transform: translateY(-5px);
}

.topic-card h3 {
  margin: 0 0 10px;
  font-size: 20px;
  color: var(--el-color-primary);
}

.topic-card p {
  color: var(--el-text-color-regular);
  font-size: 14px;
  margin-bottom: 15px;
}

.discussion-button {
  font-size: 14px;
  color: var(--el-color-success);
}
</style> 