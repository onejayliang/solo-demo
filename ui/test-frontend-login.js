import axios from 'axios';

async function testFrontendLogin() {
  try {
    // 首先访问首页，获取 CSRF token 或其他必要的信息
    const homeResponse = await axios.get('http://localhost:8081/');
    console.log('访问首页成功');
    
    // 然后访问登录页面
    const loginResponse = await axios.get('http://localhost:8081/login');
    console.log('访问登录页面成功');
    
    // 模拟登录请求
    const loginData = {
      username: 'admin',
      password: '123456'
    };
    
    // 发送登录请求
    const response = await axios.post('http://localhost:7000/api/auth/login', 'username=admin&password=123456', {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    
    console.log('登录成功:', response.data);
    
    // 保存令牌到本地存储
    if (response.data.data && response.data.data.tokens) {
      const tokens = response.data.data.tokens;
      console.log('令牌获取成功:', tokens);
    }
  } catch (error) {
    console.error('登录失败:', error.response?.data || error.message);
  }
}

testFrontendLogin();