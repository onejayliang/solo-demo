# 宗亲寻根·薪火相传APP - Code Wiki

## 1. 项目概述

**项目名称**：宗亲寻根·薪火相传APP

**项目定位**：一款以"认祖归亲、族谱信息化、宗亲互动"为核心，依托大数据技术，为全球华人宗族、宗亲提供跨地域、智能化、专属化的综合性交流与传承平台。

**核心价值**：
- 文化传承价值：推动传统族谱信息化、数字化保存
- 宗亲联结价值：通过大数据技术实现宗亲分支智能匹配
- 社交互动价值：为认证宗亲提供专属交流空间

## 2. 项目架构

### 2.1 整体架构

本项目采用前后端分离的架构设计，主要分为以下几层：

```
┌─────────────────────────────────────────────────────────┐
│                    客户端层                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Web App    │  │  Android App│  │  Admin Panel│     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│                    API 网关层                            │
│  ┌─────────────────────────────────────────────────┐     │
│  │                API Gateway                    │     │
│  └─────────────────────────────────────────────────┘     │
├─────────────────────────────────────────────────────────┤
│                    应用服务层                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  寻根匹配服务 │  │  族谱管理服务 │  │  宗亲互动服务 │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  用户认证服务 │  │  消息通知服务 │  │  搜索服务   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│                    数据服务层                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  关系数据库  │  │  文档数据库  │  │  缓存服务   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  搜索引擎   │  │  对象存储   │  │  知识图谱   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│                    大数据处理层                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  数据采集   │  │  数据清洗   │  │  数据存储   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│  ┌─────────────┐  ┌─────────────┐                      │
│  │  数据分析   │  │  匹配算法   │                      │
│  └─────────────┘  └─────────────┘                      │
├─────────────────────────────────────────────────────────┤
│                    基础设施层                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  云服务器   │  │  CDN服务    │  │  监控服务   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

### 2.2 模块架构

| 模块 | 主要职责 | 技术栈 | 依赖关系 |
|------|---------|--------|----------|
| 前端应用 | Web和Android跨平台应用 | Vue 3 + Quasar Framework | 后端API |
| 寻根匹配服务 | 祖上资料提交、智能匹配、认祖申请审核、表字生成 | Python/FastAPI、Elasticsearch | 用户认证、知识图谱 |
| 族谱管理服务 | 族谱创建与编辑、存储与查阅、权限管理、家族历史文献存储 | Python/FastAPI、MongoDB、对象存储 | 用户认证 |
| 宗亲互动服务 | 专属聊天室、宗族活动管理、祖训家风分享、宗亲名片 | Python/FastAPI、WebSocket、Redis | 用户认证、消息通知 |
| 辅助功能服务 | 用户认证、消息通知、搜索功能、帮助中心 | Python/FastAPI、JWT、Elasticsearch | 所有业务模块 |
| 大数据处理 | 数据采集、清洗、分析、匹配算法 | Python、TensorFlow、NetworkX | 寻根匹配服务 |

## 3. 主要模块职责

### 3.1 前端应用

**核心职责**：
- 提供跨平台用户界面（Web和Android）
- 实现用户交互和数据展示
- 处理前端逻辑和状态管理
- 与后端API进行通信

**技术特点**：
- 使用Vue 3 + Quasar Framework实现跨平台兼容
- 响应式设计，适配不同设备屏幕
- 模块化组件设计，提高代码复用性
- 状态管理和路由管理

### 3.2 寻根匹配模块

**核心职责**：
- 接收并处理用户提交的祖上资料
- 利用大数据和知识图谱技术进行宗亲匹配
- 管理认祖申请与审核流程
- 生成符合宗族规范的表字

**主要流程**：
1. 用户提交祖上资料（姓氏、堂号、始祖信息等）
2. 系统对资料进行标准化处理
3. 基于知识图谱和大数据算法进行匹配
4. 推荐可能的宗族分支和潜在宗亲
5. 用户提交认祖申请
6. 宗族管理员审核申请
7. 审核通过后，用户获得宗族成员身份
8. 系统为用户生成表字

### 3.3 族谱管理模块

**核心职责**：
- 支持宗族管理员创建和编辑数字化族谱
- 提供族谱的存储、查阅和下载功能
- 实现精细化的权限管理
- 存储和管理家族历史文献

**主要流程**：
1. 宗族管理员创建族谱
2. 录入族人信息（姓名、性别、出生日期、亲属关系等）
3. 设置族谱权限（查看、编辑、下载）
4. 上传家族历史文献
5. 用户根据权限查阅族谱
6. 管理员实时更新族谱信息

### 3.4 宗亲互动模块

**核心职责**：
- 为宗族和宗亲分支提供专属聊天室
- 管理宗族活动的发布和参与
- 支持祖训家风的分享和传播
- 为认证宗亲生成专属名片

**主要流程**：
1. 系统为每个宗族创建专属聊天室
2. 认证宗亲加入聊天室进行交流
3. 宗族管理员发布活动信息
4. 用户在线报名参与活动
5. 活动结束后上传活动照片和视频
6. 用户分享祖训家风和家族故事
7. 系统为认证宗亲生成宗亲名片

### 3.5 辅助功能模块

**核心职责**：
- 提供用户认证和身份管理
- 推送消息通知
- 支持关键词搜索
- 提供帮助中心和用户支持

**主要流程**：
1. 用户注册并完成实名认证
2. 系统生成JWT令牌进行身份验证
3. 系统推送认祖申请审核结果、活动提醒等通知
4. 用户通过关键词搜索宗族、宗亲、族谱
5. 用户通过帮助中心解决使用问题

### 3.6 大数据处理模块

**核心职责**：
- 采集和处理宗族相关数据
- 清洗和标准化数据
- 构建和维护知识图谱
- 实现宗亲匹配算法
- 分析和挖掘数据价值

**主要流程**：
1. 采集宗族、族谱、宗亲等相关数据
2. 清洗和标准化数据，确保数据质量
3. 构建和更新知识图谱，建立实体和关系
4. 训练和优化匹配算法
5. 为寻根匹配服务提供数据支持
6. 分析数据，挖掘潜在价值

## 4. 关键类与函数

### 4.1 前端模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `AuthService.login()` | 用户登录 | credentials: Object 登录凭证 | `{"success": true, "token": "...", "user": {...}}` | `{"success": false, "error": "..."}` | src/services/auth.js | 产品立项文件 3.4 辅助功能 |
| `AncestorDataService.submitData()` | 提交祖上资料 | data: Object 祖上资料 | `{"success": true, "dataId": "..."}` | `{"success": false, "error": "..."}` | src/services/ancestorData.js | 产品立项文件 3.1 寻根匹配模块 |
| `MatchService.getMatches()` | 获取匹配结果 | dataId: String 资料ID | `{"success": true, "matches": [...]}` | `{"success": false, "error": "..."}` | src/services/match.js | 产品立项文件 3.1 寻根匹配模块 |
| `GenealogyService.createGenealogy()` | 创建族谱 | genealogy: Object 族谱信息 | `{"success": true, "genealogyId": "..."}` | `{"success": false, "error": "..."}` | src/services/genealogy.js | 产品立项文件 3.2 族谱信息化模块 |
| `ChatService.sendMessage()` | 发送消息 | chatRoomId: String 聊天室ID<br>message: Object 消息内容 | `{"success": true, "messageId": "..."}` | `{"success": false, "error": "..."}` | src/services/chat.js | 产品立项文件 3.3 宗亲互动模块 |

### 4.2 后端模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `auth_controller.login()` | 用户登录 | username: str 用户名<br>password: str 密码 | `{"success": true, "access_token": "...", "user": {...}}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/auth.py | 产品立项文件 3.4 辅助功能 |
| `ancestor_data_controller.submit_data()` | 提交祖上资料 | ancestor_data: AncestorData 祖上资料 | `{"success": true, "data_id": "...", "status": "pending"}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/ancestor_data.py | 产品立项文件 3.1 寻根匹配模块 |
| `match_controller.match_relatives()` | 宗亲匹配 | data_id: str 资料ID | `{"success": true, "matches": [...]}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/match.py | 产品立项文件 3.1 寻根匹配模块 |
| `application_controller.submit_application()` | 提交认祖申请 | application: Application 申请信息 | `{"success": true, "application_id": "...", "status": "pending"}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/application.py | 产品立项文件 3.1 寻根匹配模块 |
| `application_controller.review_application()` | 审核认祖申请 | application_id: str 申请ID<br>status: str 审核状态 | `{"success": true, "status": "approved/rejected"}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/application.py | 产品立项文件 3.1 寻根匹配模块 |
| `genealogy_controller.create_genealogy()` | 创建族谱 | genealogy: Genealogy 族谱信息 | `{"success": true, "genealogy_id": "..."}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/genealogy.py | 产品立项文件 3.2 族谱信息化模块 |
| `chat_controller.create_chat_room()` | 创建聊天室 | clan_id: str 宗族ID | `{"success": true, "chat_room_id": "..."}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/chat.py | 产品立项文件 3.3 宗亲互动模块 |
| `activity_controller.create_activity()` | 创建宗族活动 | activity: Activity 活动信息 | `{"success": true, "activity_id": "..."}` | `{"success": false, "error": "..."}` | backend/app/api/controllers/activity.py | 产品立项文件 3.3 宗亲互动模块 |

### 4.3 大数据处理模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `data_collector.collect_data()` | 采集数据 | source: str 数据源<br>params: dict 采集参数 | `{"success": true, "data_count": int}` | `{"success": false, "error": "..."}` | backend/app/bigdata/data_collector.py | 产品立项文件 3.1 寻根匹配模块 |
| `data_cleaner.clean_data()` | 清洗数据 | data: dict 原始数据 | `{"success": true, "cleaned_data": dict}` | `{"success": false, "error": "..."}` | backend/app/bigdata/data_cleaner.py | 产品立项文件 3.1 寻根匹配模块 |
| `knowledge_graph.build_graph()` | 构建知识图谱 | data: dict 清洗后的数据 | `{"success": true, "graph_id": "..."}` | `{"success": false, "error": "..."}` | backend/app/bigdata/knowledge_graph.py | 产品立项文件 3.1 寻根匹配模块 |
| `matching_algorithm.match()` | 执行匹配算法 | user_data: dict 用户数据 | `{"success": true, "matches": [...]}` | `{"success": false, "error": "..."}` | backend/app/bigdata/matching_algorithm.py | 产品立项文件 3.1 寻根匹配模块 |

## 5. 依赖关系

### 5.1 前端依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| Vue | 3.3+ | 前端框架 | 项目需求 |
| Quasar Framework | 2.12+ | 跨平台UI框架 | 项目需求 |
| Vuex | 4.1+ | 状态管理 | 常见前端技术栈 |
| Vue Router | 4.2+ | 路由管理 | 常见前端技术栈 |
| Axios | 1.6+ | API请求 | 常见前端技术栈 |
| WebSocket | - | 实时通信 | 产品立项文件 3.3 宗亲互动模块 |
| Pinia | 2.1+ | 状态管理（可选） | 常见前端技术栈 |

### 5.2 后端依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| FastAPI | 0.104+ | 后端框架 | 项目需求 |
| Uvicorn | 0.24+ | ASGI服务器 | FastAPI依赖 |
| Pydantic | 2.5+ | 数据验证 | FastAPI依赖 |
| SQLAlchemy | 2.0+ | ORM | 数据访问 |
| MongoDB | 4.4+ | 文档数据库 | 产品立项文件 3.2 族谱信息化模块 |
| Redis | 7.0+ | 缓存和实时数据 | 产品立项文件 3.3 宗亲互动模块 |
| Elasticsearch | 8.0+ | 搜索和大数据分析 | 产品立项文件 3.1 寻根匹配模块 |
| JWT | 2.6+ | 身份令牌 | 产品立项文件 3.4 辅助功能 |
| WebSocket | - | 实时通信 | 产品立项文件 3.3 宗亲互动模块 |
| Boto3 | 1.34+ | 对象存储 | 产品立项文件 3.2 族谱信息化模块 |

### 5.3 大数据依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| Python | 3.9+ | 编程语言 | 项目需求 |
| TensorFlow | 2.10+ | 机器学习 | 产品立项文件 3.1 寻根匹配模块 |
| NetworkX | 2.8+ | 知识图谱构建 | 产品立项文件 3.1 寻根匹配模块 |
| Pandas | 2.1+ | 数据处理 | 常见大数据技术栈 |
| NumPy | 1.26+ | 数值计算 | 常见大数据技术栈 |
| Scikit-learn | 1.4+ | 机器学习 | 产品立项文件 3.1 寻根匹配模块 |
| Scrapy | 2.11+ | 数据采集 | 产品立项文件 3.1 寻根匹配模块 |

## 6. 项目运行方式

### 6.1 开发环境

**前端开发环境**：
1. 安装 Node.js 16+ 和 npm 8+
2. 安装 Quasar CLI：`npm install -g @quasar/cli`
3. 克隆代码仓库
4. 进入前端目录：`cd frontend`
5. 安装依赖：`npm install`
6. 启动开发服务器：`quasar dev`（Web）或 `quasar dev -m capacitor -T android`（Android）

**后端开发环境**：
1. 安装 Python 3.9+
2. 安装 pip 和虚拟环境：`pip install virtualenv`
3. 克隆代码仓库
4. 进入后端目录：`cd backend`
5. 创建虚拟环境：`virtualenv venv`
6. 激活虚拟环境：`source venv/bin/activate`（Linux/Mac）或 `venv\Scripts\activate`（Windows）
7. 安装依赖：`pip install -r requirements.txt`
8. 启动后端服务：`uvicorn app.main:app --reload`

### 6.2 生产环境

**前端部署**：
- Web：构建静态文件：`quasar build`，部署到静态网站服务器
- Android：构建APK：`quasar build -m capacitor -T android`，发布到Google Play

**后端部署**：
- 使用 Docker 容器化部署
- 配置环境变量和数据库连接
- 使用 Gunicorn + Uvicorn 作为生产服务器
- 配置 Nginx 作为反向代理

**大数据服务**：
- 部署为独立服务或集成到后端
- 配置定时任务进行数据采集和处理
- 监控和优化性能

### 6.3 API 文档

API 文档使用 FastAPI 的自动文档生成功能，可通过以下地址访问：
- 开发环境：http://localhost:8000/docs
- 生产环境：https://api.familysearch.com/docs

## 7. 目录结构

```
├── frontend/                  # 前端代码
│   ├── src/                   # 源代码
│   │   ├── components/        # 组件
│   │   ├── pages/             # 页面
│   │   ├── services/          # API 服务
│   │   ├── stores/            # 状态管理
│   │   ├── router/            # 路由管理
│   │   └── utils/             # 工具函数
│   ├── public/                # 静态资源
│   ├── quasar.conf.js         # Quasar 配置
│   └── package.json           # 依赖配置
├── backend/                   # 后端代码
│   ├── app/                   # 应用代码
│   │   ├── api/               # API 层
│   │   │   ├── controllers/   # 控制器
│   │   │   ├── routes/        # 路由
│   │   │   └── schemas/       # 数据模型
│   │   ├── services/          # 服务层
│   │   ├── models/            # 数据模型
│   │   ├── database/          # 数据库配置
│   │   ├── bigdata/           # 大数据处理
│   │   │   ├── data_collector.py  # 数据采集
│   │   │   ├── data_cleaner.py    # 数据清洗
│   │   │   ├── knowledge_graph.py # 知识图谱
│   │   │   └── matching_algorithm.py # 匹配算法
│   │   ├── config/            # 配置
│   │   └── utils/             # 工具类
│   ├── main.py                # 应用入口
│   ├── requirements.txt       # 依赖配置
│   └── Dockerfile             # Docker 配置
├── docs/                      # 文档
│   ├── api/                   # API 文档
│   ├── architecture/          # 架构文档
│   └── user/                  # 用户文档
└── README.md                  # 项目说明
```

## 8. 关键技术点

### 8.1 跨平台前端开发

**技术要点**：
- 使用 Quasar Framework 实现一套代码，多平台部署
- 响应式设计，适配不同设备屏幕
- 组件化开发，提高代码复用性
- 状态管理和路由管理

**应用场景**：
- Web 浏览器访问
- Android 移动应用
- 管理后台

### 8.2 知识图谱构建

**技术要点**：
- 使用 NetworkX 构建宗族关系知识图谱
- 基于姓氏、堂号、始祖信息等构建实体和关系
- 支持图谱的查询和分析

**应用场景**：
- 宗亲匹配算法的基础
- 族谱关系的可视化展示
- 家族历史的追溯和分析

### 8.3 大数据匹配算法

**技术要点**：
- 使用机器学习算法进行宗亲匹配
- 基于多维度特征进行相似度计算
- 支持实时匹配和批量匹配

**应用场景**：
- 寻根匹配功能
- 潜在宗亲推荐
- 族谱关联分析

### 8.4 实时通信

**技术要点**：
- 使用 WebSocket 实现实时聊天
- 支持群组聊天和一对一聊天
- 消息的持久化存储

**应用场景**：
- 宗亲聊天室
- 活动通知
- 实时消息推送

### 8.5 数据安全

**技术要点**：
- 采用 JWT 进行身份认证
- 实现多因素认证
- 数据加密和权限控制
- 敏感数据保护

**应用场景**：
- 用户登录和注册
- 权限管理
- 数据安全保护

## 9. 总结

**宗亲寻根·薪火相传APP**是一款基于大数据技术的宗族宗亲数字化平台，通过整合寻根匹配、族谱管理、宗亲互动等核心功能，为全球华人提供了一个跨地域、智能化的宗族文化传承与交流平台。

**核心价值**：
- 推动传统宗族文化的数字化传承
- 帮助流失在外的族人认祖归亲
- 促进宗亲之间的交流与联系
- 弘扬中华优秀传统文化

**技术特色**：
- 采用 Vue 3 + Quasar Framework 实现跨平台兼容
- 使用 FastAPI + Python 构建高效后端
- 整合大数据和知识图谱技术
- 实现实时通信和智能匹配
- 提供安全可靠的用户认证

**未来展望**：
- 进一步优化匹配算法，提高匹配准确率
- 拓展功能，如宗族文创、宗亲旅游等
- 构建全球宗族数据库，形成更完整的宗族网络
- 推动宗族文化的数字化保护与传承

---

*注：本Code Wiki基于产品立项文件设计，实际实现可能会根据开发过程中的具体情况进行调整。*