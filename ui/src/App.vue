<template>
  <div class="app">
    <header class="header">
      <div class="logo">
        <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20family%20seal%20red%20stamp%20design&image_size=square" alt="宗亲寻根">
      </div>
      <h1 class="title">宗亲寻根·薪火相传</h1>
      <nav class="nav">
        <a href="/" class="nav-link">首页</a>
        <a href="/xungen" class="nav-link">寻根</a>
        <a href="/zupu" class="nav-link">族谱</a>
        <a href="/zongqin" class="nav-link">宗亲</a>
        <a href="/profile" class="nav-link">我的</a>
      </nav>
    </header>
    <main class="main">
      <router-view />
    </main>
    <footer class="footer">
      <div class="footer-content">
        <p>宗亲寻根·薪火相传 © 2024</p>
        <p>弘扬中华优秀传统文化</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.header {
  background-color: #8B4513;
  color: white;
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.title {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav {
  display: flex;
  gap: 1rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.main {
  flex: 1;
  padding: 2rem;
  background-color: #f5f5f5;
}

.footer {
  background-color: #8B4513;
  color: white;
  padding: 1rem;
  text-align: center;
  margin-top: auto;
}

.footer-content p {
  margin: 0.5rem 0;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .nav {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .main {
    padding: 1rem;
  }
}
</style>