<template>
  <div class="zupu-page">
    <h1>族谱管理</h1>
    <div class="card">
      <div class="card-header">
        <h2>族谱管理</h2>
        <button class="btn-primary">创建族谱</button>
      </div>
      <div class="card-body">
        <p>数字化族谱，传承家族历史，支持创建、编辑和查阅族谱</p>
      </div>
    </div>
    
    <div class="zupu-list">
      <div class="zupu-card" v-for="genealogy in genealogies" :key="genealogy.id">
        <img :src="genealogy.image" alt="族谱封面">
        <div class="zupu-card-body">
          <h3>{{ genealogy.name }}</h3>
          <p class="member-count">
            👥 {{ genealogy.memberCount }}位族人
          </p>
          <p class="description">{{ genealogy.description }}</p>
        </div>
        <div class="zupu-card-actions">
          <button class="btn-primary">查看</button>
          <button class="btn-secondary">编辑</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const genealogies = ref([
  {
    id: 1,
    name: '陇西李氏宗谱',
    memberCount: 1256,
    description: '记录陇西李氏一脉的繁衍历史，始于唐代，至今已有千年历史',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20genealogy%20book%20family%20tree&image_size=landscape_16_9'
  },
  {
    id: 2,
    name: '太原王氏族谱',
    memberCount: 892,
    description: '太原王氏宗族谱牒，详细记载了王氏族人的世系传承',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=ancient%20chinese%20family%20tree%20scroll%20traditional&image_size=landscape_16_9'
  }
])
</script>

<style scoped>
.zupu-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.zupu-page h1 {
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

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
}

.card-header h2 {
  color: #8B4513;
  font-size: 1.5rem;
  margin: 0;
}

.card-body {
  padding: 1.5rem;
  color: #666;
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

.btn-secondary {
  background-color: #6c757d;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-secondary:hover {
  background-color: #5a6268;
}

.zupu-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.zupu-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: box-shadow 0.3s;
}

.zupu-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.zupu-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.zupu-card-body {
  padding: 1.5rem;
}

.zupu-card-body h3 {
  color: #8B4513;
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.member-count {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.description {
  color: #666;
  line-height: 1.5;
}

.zupu-card-actions {
  padding: 1rem 1.5rem;
  background-color: #f8f9fa;
  border-top: 1px solid #e9ecef;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .zupu-page {
    padding: 1rem;
  }
  
  .zupu-page h1 {
    font-size: 2rem;
  }
  
  .card-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .zupu-list {
    grid-template-columns: 1fr;
  }
}
</style>