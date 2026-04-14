<template>
  <div class="profile-page">
    <div class="profile-header">
      <img :src="profile.avatar" alt="头像" class="profile-avatar">
      <h2>{{ profile.name }}</h2>
      <p>{{ profile.clan }}</p>
      <div class="seal-stamp">{{ profile.styleName }}</div>
    </div>
    
    <div class="profile-card">
      <h3>基本信息</h3>
      <ul class="info-list">
        <li class="info-item">
          <span class="info-icon">👤</span>
          <div class="info-content">
            <span class="info-label">姓名</span>
            <span class="info-value">{{ profile.name }}</span>
          </div>
        </li>
        <li class="info-item">
          <span class="info-icon">🏠</span>
          <div class="info-content">
            <span class="info-label">宗族</span>
            <span class="info-value">{{ profile.clan }}</span>
          </div>
        </li>
        <li class="info-item">
          <span class="info-icon">📜</span>
          <div class="info-content">
            <span class="info-label">辈分</span>
            <span class="info-value">{{ profile.generation }}</span>
          </div>
        </li>
        <li class="info-item">
          <span class="info-icon">✏️</span>
          <div class="info-content">
            <span class="info-label">表字</span>
            <span class="info-value">{{ profile.styleName }}</span>
          </div>
        </li>
      </ul>
    </div>
    
    <div class="profile-card">
      <h3>功能菜单</h3>
      <ul class="menu-list">
        <li class="menu-item" @click="handleMenuClick('settings')">
          <span class="menu-icon">⚙️</span>
          <span class="menu-label">账号设置</span>
        </li>
        <li class="menu-item" @click="handleMenuClick('notifications')">
          <span class="menu-icon">🔔</span>
          <span class="menu-label">消息通知</span>
        </li>
        <li class="menu-item" @click="handleMenuClick('help')">
          <span class="menu-icon">❓</span>
          <span class="menu-label">帮助中心</span>
        </li>
        <li class="menu-item logout" @click="handleMenuClick('logout')">
          <span class="menu-icon">🚪</span>
          <span class="menu-label">退出登录</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const profile = ref({
  name: '李明',
  clan: '陇西李氏',
  generation: '第28代',
  styleName: '明远',
  avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20portrait%20avatar&image_size=square'
})

const handleMenuClick = (menu) => {
  console.log('点击菜单:', menu)
  if (menu === 'logout') {
    // 模拟退出登录
    router.push('/login')
  }
}
</script>

<style scoped>
.profile-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 0;
}

.profile-header {
  text-align: center;
  padding: 2rem;
  background-color: #fff8e1;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.profile-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-bottom: 1rem;
  border: 4px solid #8B4513;
}

.profile-header h2 {
  color: #8B4513;
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}

.profile-header p {
  color: #666;
  margin-bottom: 1rem;
}

.seal-stamp {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #8B4513;
  color: white;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: bold;
  transform: rotate(-5deg);
}

.profile-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  overflow: hidden;
}

.profile-card h3 {
  padding: 1.5rem;
  margin: 0;
  color: #8B4513;
  font-size: 1.3rem;
  border-bottom: 1px solid #e9ecef;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.info-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e9ecef;
}

.info-item:last-child {
  border-bottom: none;
}

.info-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
  width: 30px;
  text-align: center;
}

.info-content {
  flex: 1;
}

.info-label {
  display: block;
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.25rem;
}

.info-value {
  display: block;
  color: #333;
  font-weight: 500;
}

.menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e9ecef;
  cursor: pointer;
  transition: background-color 0.3s;
}

.menu-item:hover {
  background-color: #f8f9fa;
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-icon {
  font-size: 1.2rem;
  margin-right: 1rem;
  width: 30px;
  text-align: center;
}

.menu-label {
  flex: 1;
  color: #333;
}

.menu-item.logout {
  color: #dc3545;
}

.menu-item.logout .menu-label {
  color: #dc3545;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .profile-page {
    padding: 1rem;
  }
  
  .profile-header {
    padding: 1.5rem;
  }
  
  .profile-avatar {
    width: 100px;
    height: 100px;
  }
  
  .profile-header h2 {
    font-size: 1.5rem;
  }
  
  .info-item,
  .menu-item {
    padding: 0.75rem 1rem;
  }
}
</style>