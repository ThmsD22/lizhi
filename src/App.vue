<script setup>
import { HomeFilled, Collection, Location, VideoCamera, Shop } from '@element-plus/icons-vue'
</script>

<template>
  <el-container class="app-container">
    <el-header height="60px">
      <el-menu
        :router="true"
        mode="horizontal"
        :ellipsis="false"
        class="main-menu"
      >
        <el-menu-item index="/">
          <el-icon><HomeFilled /></el-icon>
          首页
        </el-menu-item>
        <el-menu-item index="/varieties">
          <el-icon><Collection /></el-icon>
          品种文化
        </el-menu-item>
        <el-menu-item index="/map">
          <el-icon><Location /></el-icon>
          产区地图
        </el-menu-item>
        <el-menu-item index="/media">
          <el-icon><VideoCamera /></el-icon>
          视频图文
        </el-menu-item>
        <el-menu-item index="/brands">
          <el-icon><Shop /></el-icon>
          品牌农户
        </el-menu-item>
      </el-menu>
    </el-header>
    
    <el-main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </el-main>

    <el-footer height="60px">
      <div class="footer-content">
        © 2024 粤西荔枝文化展示平台
      </div>
    </el-footer>
  </el-container>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
}

.main-menu {
  border-bottom: solid 1px var(--el-border-color-light);
}

.el-header {
  padding: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.el-main {
  padding: 20px;
  background-color: var(--el-bg-color-page);
}

.el-footer {
  background-color: var(--el-bg-color);
  border-top: solid 1px var(--el-border-color-light);
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-content {
  color: var(--el-text-color-secondary);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
