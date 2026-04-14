<template>
  <div class="error-page">
    <div class="error-content">
      <h1 class="error-code">404</h1>
      <p class="error-message">页面未找到</p>
      <button class="btn-primary" @click="$router.push('/')">返回首页</button>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.error-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
}

.error-content {
  text-align: center;
  padding: 2rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

.error-code {
  font-size: 4rem;
  font-weight: bold;
  color: #8B4513;
  margin-bottom: 1rem;
  font-family: 'STXingkai', 'KaiTi', cursive;
}

.error-message {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 2rem;
}

.btn-primary {
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

.btn-primary:hover {
  background-color: #6d3813;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .error-content {
    padding: 1.5rem;
  }
  
  .error-code {
    font-size: 3rem;
  }
  
  .error-message {
    font-size: 1.2rem;
  }
}
</style>