import axios from 'axios';

async function testLogin() {
  try {
    // 使用 URL 编码的字符串发送登录请求，使用测试用户凭据
    const response = await axios.post('http://localhost:7000/api/auth/login', 'username=admin&password=123456', {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    console.log('登录成功:', response.data);
  } catch (error) {
    console.error('登录失败:', error.response?.data || error.message);
  }
}

testLogin();