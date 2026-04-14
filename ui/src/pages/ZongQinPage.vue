<template>
  <div class="zongqin-page">
    <h1>宗亲互动</h1>
    <div class="card">
      <div class="card-body">
        <h2>宗亲互动</h2>
        <p>专属聊天室、宗族活动、祖训家风分享，宗亲交流平台</p>
      </div>
    </div>
    
    <div class="tabs">
      <button 
        class="tab" 
        :class="{ active: activeTab === 'chat' }" 
        @click="activeTab = 'chat'"
      >
        💬 聊天室
      </button>
      <button 
        class="tab" 
        :class="{ active: activeTab === 'activities' }" 
        @click="activeTab = 'activities'"
      >
        📅 活动
      </button>
      <button 
        class="tab" 
        :class="{ active: activeTab === 'culture' }" 
        @click="activeTab = 'culture'"
      >
        📚 家风
      </button>
    </div>
    
    <div class="tab-content">
      <div v-if="activeTab === 'chat'" class="tab-panel">
        <div class="chat-room" v-for="room in chatRooms" :key="room.id">
          <div class="chat-room-avatar" :style="{ backgroundColor: room.color }">
            {{ room.name.charAt(0) }}
          </div>
          <div class="chat-room-info">
            <h4>{{ room.name }}</h4>
            <p>{{ room.lastMessage }}</p>
          </div>
          <div class="chat-room-unread" v-if="room.unread">
            {{ room.unread }}
          </div>
        </div>
      </div>
      
      <div v-if="activeTab === 'activities'" class="tab-panel">
        <div class="activity-card" v-for="activity in activities" :key="activity.id">
          <img :src="activity.image" alt="活动图片">
          <div class="activity-card-body">
            <h4>{{ activity.title }}</h4>
            <p class="activity-meta">
              📅 {{ activity.date }}
            </p>
            <p class="activity-meta">
              📍 {{ activity.location }}
            </p>
            <p class="activity-description">{{ activity.description }}</p>
          </div>
          <div class="activity-card-actions">
            <button class="btn-primary">报名参加</button>
          </div>
        </div>
      </div>
      
      <div v-if="activeTab === 'culture'" class="tab-panel">
        <div class="culture-card" v-for="item in cultureItems" :key="item.id">
          <div class="culture-card-body">
            <div class="culture-author">
              <img :src="item.avatar" alt="作者头像" class="author-avatar">
              <div class="author-info">
                <h4>{{ item.author }}</h4>
                <p class="author-time">{{ item.time }}</p>
              </div>
            </div>
            <p class="culture-content">{{ item.content }}</p>
          </div>
          <div class="culture-card-actions">
            <button class="btn-icon">👍 点赞</button>
            <button class="btn-icon">💬 评论</button>
            <button class="btn-icon">🔗 分享</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('chat')

const chatRooms = ref([
  { id: 1, name: '陇西李氏宗亲群', lastMessage: '李氏族谱更新了', unread: 5, color: '#007bff' },
  { id: 2, name: '太原王氏宗亲群', lastMessage: '下周祭祖活动', unread: 0, color: '#6c757d' }
])

const activities = ref([
  {
    id: 1,
    title: '李氏宗亲祭祖大典',
    date: '2024-04-20 09:00',
    location: '陇西李氏宗祠',
    description: '一年一度的李氏宗亲祭祖大典，欢迎各地宗亲参加',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20ancestor%20worship%20ceremony&image_size=landscape_16_9'
  }
])

const cultureItems = ref([
  {
    id: 1,
    author: '李明',
    time: '2天前',
    avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20avatar%20portrait&image_size=square',
    content: '李氏祖训：忠孝传家，耕读为本。希望后世子孙牢记祖训，传承家风。'
  }
])
</script>

<style scoped>
.zongqin-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.zongqin-page h1 {
  text-align: center;
  color: #8B4513;
  margin-bottom: 2rem;
  font-size: 2.5rem;
}

.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  overflow: hidden;
}

.card-body {
  padding: 1.5rem;
}

.card-body h2 {
  color: #8B4513;
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.card-body p {
  color: #666;
}

.tabs {
  display: flex;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  overflow: hidden;
}

.tab {
  flex: 1;
  padding: 1rem;
  background-color: #f8f9fa;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 1rem;
  font-weight: 500;
}

.tab:hover {
  background-color: #e9ecef;
}

.tab.active {
  background-color: #8B4513;
  color: white;
}

.tab-content {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
}

.tab-panel {
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.chat-room {
  display: flex;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #e9ecef;
  cursor: pointer;
  transition: background-color 0.3s;
}

.chat-room:hover {
  background-color: #f8f9fa;
}

.chat-room-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 1.5rem;
  margin-right: 1rem;
}

.chat-room-info {
  flex: 1;
}

.chat-room-info h4 {
  color: #333;
  margin-bottom: 0.25rem;
}

.chat-room-info p {
  color: #666;
  font-size: 0.9rem;
}

.chat-room-unread {
  background-color: red;
  color: white;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: bold;
}

.activity-card {
  border: 1px solid #e9ecef;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.activity-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.activity-card-body {
  padding: 1.5rem;
}

.activity-card-body h4 {
  color: #8B4513;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.activity-meta {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.activity-description {
  color: #666;
  line-height: 1.5;
}

.activity-card-actions {
  padding: 1rem 1.5rem;
  background-color: #f8f9fa;
  border-top: 1px solid #e9ecef;
  display: flex;
  justify-content: flex-end;
}

.culture-card {
  border: 1px solid #e9ecef;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.culture-card-body {
  padding: 1.5rem;
}

.culture-author {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.author-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 1rem;
}

.author-info h4 {
  color: #333;
  margin-bottom: 0.25rem;
}

.author-time {
  color: #666;
  font-size: 0.8rem;
}

.culture-content {
  color: #666;
  line-height: 1.5;
}

.culture-card-actions {
  padding: 1rem 1.5rem;
  background-color: #f8f9fa;
  border-top: 1px solid #e9ecef;
  display: flex;
  gap: 1rem;
}

.btn-primary {
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #6d3813;
}

.btn-icon {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  transition: color 0.3s;
  font-size: 0.9rem;
}

.btn-icon:hover {
  color: #8B4513;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .zongqin-page {
    padding: 1rem;
  }
  
  .zongqin-page h1 {
    font-size: 2rem;
  }
  
  .tabs {
    flex-direction: column;
  }
  
  .tab {
    text-align: left;
  }
}
</style>