<template>
  <div class="xungen-page">
    <h1>寻根问祖</h1>
    <div class="search-container">
      <form @submit.prevent="handleSearch">
        <div class="form-group">
          <label for="surname">姓氏</label>
          <input type="text" id="surname" v-model="searchForm.surname" required>
        </div>
        <div class="form-group">
          <label for="ancestor">祖先姓名</label>
          <input type="text" id="ancestor" v-model="searchForm.ancestor">
        </div>
        <div class="form-group">
          <label for="hometown">祖籍地</label>
          <input type="text" id="hometown" v-model="searchForm.hometown">
        </div>
        <button type="submit" class="search-btn">开始寻根</button>
      </form>
    </div>
    
    <div class="results-container" v-if="results.length > 0">
      <h2>寻根结果</h2>
      <div class="result-card" v-for="(result, index) in results" :key="index">
        <h3>{{ result.surname }}氏家族</h3>
        <p><strong>祖籍地:</strong> {{ result.hometown }}</p>
        <p><strong>祖先:</strong> {{ result.ancestor }}</p>
        <p><strong>字辈:</strong> {{ result.generation }}</p>
        <button class="detail-btn">查看详情</button>
      </div>
    </div>
    
    <div class="tips-container">
      <h2>寻根提示</h2>
      <ul>
        <li>请尽可能提供详细的祖先信息</li>
        <li>祖籍地信息越详细，匹配成功率越高</li>
        <li>如果没有找到匹配结果，可以尝试使用不同的关键词</li>
        <li>您也可以联系我们的客服，获取更多帮助</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const searchForm = ref({
  surname: '',
  ancestor: '',
  hometown: ''
})

const results = ref([])

const handleSearch = async () => {
  // 这里可以添加搜索逻辑
  console.log('搜索信息:', searchForm.value)
  // 模拟搜索结果
  results.value = [
    {
      surname: '张',
      ancestor: '张三丰',
      hometown: '湖北省武汉市',
      generation: '天、地、玄、黄、宇、宙、洪、荒'
    },
    {
      surname: '张',
      ancestor: '张仲景',
      hometown: '河南省南阳市',
      generation: '文、武、德、智、勇、信、义、仁'
    }
  ]
}
</script>

<style scoped>
.xungen-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.xungen-page h1 {
  text-align: center;
  color: #8B4513;
  margin-bottom: 2rem;
  font-size: 2.5rem;
}

.search-container {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #666;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #8B4513;
  box-shadow: 0 0 0 2px rgba(139, 69, 19, 0.2);
}

.search-btn {
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-btn:hover {
  background-color: #6d3813;
}

.results-container {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.results-container h2 {
  color: #8B4513;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
}

.result-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: box-shadow 0.3s;
}

.result-card:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.result-card h3 {
  color: #8B4513;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.result-card p {
  margin-bottom: 0.5rem;
  color: #666;
}

.detail-btn {
  background-color: #8B4513;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 1rem;
}

.detail-btn:hover {
  background-color: #6d3813;
}

.tips-container {
  background-color: #fff8e1;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.tips-container h2 {
  color: #8B4513;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
}

.tips-container ul {
  list-style-type: disc;
  padding-left: 2rem;
  color: #666;
}

.tips-container li {
  margin-bottom: 0.5rem;
  line-height: 1.5;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .xungen-page {
    padding: 1rem;
  }
  
  .xungen-page h1 {
    font-size: 2rem;
  }
  
  .search-container,
  .results-container,
  .tips-container {
    padding: 1.5rem;
  }
}
</style>