<template>
  <div class="index-page">
    <div class="hero-section">
      <h1>宗亲寻根·薪火相传</h1>
      <p>认祖归亲 · 族谱信息化 · 宗亲互动</p>
    </div>
    
    <div class="features-section">
      <div class="feature-card" @click="$router.push('/xungen')">
        <div class="feature-icon">🧭</div>
        <h3>寻根问祖</h3>
        <p>大数据智能匹配，助力认祖归亲</p>
      </div>
      
      <div class="feature-card" @click="$router.push('/zupu')">
        <div class="feature-icon">📜</div>
        <h3>族谱管理</h3>
        <p>数字化族谱，传承家族历史</p>
      </div>
      
      <div class="feature-card" @click="$router.push('/zongqin')">
        <div class="feature-icon">👥</div>
        <h3>宗亲互动</h3>
        <p>专属聊天室，宗亲交流平台</p>
      </div>
    </div>
    
    <div class="culture-section">
      <h2>宗族文化传承</h2>
      <div class="culture-content">
        <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20ancestor%20hall%20family%20tree%20culture&image_size=landscape_16_9" alt="宗族文化">
        <p>
          宗族文化是中华传统文化的重要组成部分，承载着家族血脉延续、文化传承的重要使命。
          本平台致力于推动传统族谱信息化、数字化保存，帮助流失在外的族人认祖归亲，
          重建宗亲联系，弘扬中华优秀传统文化。
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.index-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.hero-section {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background-color: #fff8e1;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.hero-section h1 {
  font-size: 2.5rem;
  color: #8B4513;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1.2rem;
  color: #666;
}

.features-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.feature-card {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  color: #8B4513;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #666;
}

.culture-section {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.culture-section h2 {
  font-size: 2rem;
  color: #8B4513;
  margin-bottom: 1.5rem;
  text-align: center;
}

.culture-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.culture-content img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.culture-content p {
  color: #666;
  line-height: 1.6;
}

/* 响应式设计 */
@media (min-width: 768px) {
  .culture-content {
    flex-direction: row;
    align-items: center;
  }
  
  .culture-content img {
    flex: 1;
    max-width: 50%;
  }
  
  .culture-content p {
    flex: 1;
  }
}
</style>