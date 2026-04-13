# 宗亲寻根·薪火相传 APP

一款以"认祖归亲、族谱信息化、宗亲互动"为核心，依托大数据技术，为全球华人宗族、宗亲提供跨地域、智能化、专属化的综合性交流与传承平台。

## 项目简介

本项目采用前后端分离架构，致力于打破地域壁垒、弥补宗族传承断层，成为每个宗族的"数字化宗祠"、每个族人的"寻根指南针"。

## 技术栈

### 前端 (ui/)
- **框架**: Vue 3 + Quasar Framework
- **状态管理**: Pinia
- **路由**: Vue Router
- **HTTP客户端**: Axios

### 后端 (app/)
- **框架**: FastAPI (Python)
- **认证**: JWT + bcrypt
- **数据库**: 
  - PostgreSQL (关系型数据)
  - MongoDB (文档数据)
  - Redis (缓存)
- **搜索引擎**: Elasticsearch
- **ORM**: SQLAlchemy

## 项目结构

```
/workspace/
├── ui/                          # 前端代码
│   ├── src/
│   │   ├── components/         # 组件
│   │   ├── pages/             # 页面
│   │   ├── services/          # API 服务
│   │   ├── stores/            # 状态管理
│   │   ├── router/            # 路由管理
│   │   ├── css/               # 样式
│   │   └── layouts/           # 布局
│   ├── public/                # 静态资源
│   ├── package.json           # 依赖配置
│   └── quasar.config.js       # Quasar 配置
├── app/                        # 后端代码
│   ├── app/
│   │   ├── api/               # API 层
│   │   │   ├── controllers/   # 控制器
│   │   │   ├── routes/        # 路由
│   │   │   └── schemas/       # 数据模型
│   │   ├── services/          # 服务层
│   │   ├── models/            # 数据模型
│   │   ├── database/          # 数据库配置
│   │   ├── bigdata/           # 大数据处理
│   │   ├── config/            # 配置
│   │   └── utils/             # 工具类
│   ├── tests/                 # 测试
│   ├── main.py                # 应用入口
│   ├── requirements.txt       # 依赖配置
│   └── .env.example          # 环境变量示例
└── docs/                       # 项目文档
```

## 核心功能

### 1. 寻根问祖
- 祖上资料提交
- 大数据智能匹配
- 认祖申请与审核
- 表字生成

### 2. 族谱管理
- 族谱创建与编辑
- 族谱存储与查阅
- 精细化权限管理
- 家族历史文献存储

### 3. 宗亲互动
- 专属聊天室
- 宗族活动管理
- 祖训家风分享
- 宗亲名片

### 4. 辅助功能
- 用户认证
- 消息通知
- 搜索功能
- 帮助中心

## 安全特性

### 后端安全
- 密码使用 bcrypt 哈希存储
- JWT 令牌认证机制
- 访问令牌和刷新令牌分离
- 密码强度验证
- 输入清理防止注入攻击
- 安全响应头设置
- CORS 配置保护

### 前端安全
- Token 本地存储管理
- API 请求拦截器
- 自动重定向未认证用户

## 快速开始

### 前端启动

```bash
cd ui
npm install
npm run dev
```

### 后端启动

```bash
cd app
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 文件配置数据库等
uvicorn main:app --reload
```

## API 文档

启动后端服务后，访问以下地址查看 API 文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 开发指南

详细的架构设计和开发文档请参考：
- [CODE_WIKI.md](file:///workspace/CODE_WIKI.md)
- [宗亲寻根·薪火相传APP产品立项文件.md](file:///workspace/宗亲寻根·薪火相传APP产品立项文件.md)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目仅供学习和研究使用。