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
│  │  iOS App    │  │  Android App│  │  Web Admin  │     │
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
│                    基础设施层                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  云服务器   │  │  CDN服务    │  │  监控服务   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

### 2.2 模块架构

| 模块 | 主要职责 | 技术栈 | 依赖关系 |
|------|---------|--------|----------|
| 寻根匹配模块 | 祖上资料提交、智能匹配、认祖申请审核、表字生成 | Java/Spring Boot、Python、Elasticsearch | 用户认证、知识图谱 |
| 族谱管理模块 | 族谱创建与编辑、存储与查阅、权限管理、家族历史文献存储 | Java/Spring Boot、MongoDB、对象存储 | 用户认证 |
| 宗亲互动模块 | 专属聊天室、宗族活动管理、祖训家风分享、宗亲名片 | Java/Spring Boot、WebSocket、Redis | 用户认证、消息通知 |
| 辅助功能模块 | 用户认证、消息通知、搜索功能、帮助中心 | Java/Spring Boot、JWT、Elasticsearch | 所有业务模块 |

## 3. 主要模块职责

### 3.1 寻根匹配模块

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

### 3.2 族谱管理模块

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

### 3.3 宗亲互动模块

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

### 3.4 辅助功能模块

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

## 4. 关键类与函数

### 4.1 寻根匹配模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `AncestorDataService.submitAncestorData()` | 提交祖上资料 | ancestorData: AncestorData 祖上资料对象 | `{"success": true, "data": {"dataId": "...", "status": "pending"}}` | `{"success": false, "error": "..."}` | com.familysearch.service.AncestorDataService | 产品立项文件 3.1 寻根匹配模块 |
| `MatchService.matchRelatives()` | 宗亲匹配 | dataId: String 资料ID | `{"success": true, "data": {"matches": [...]}}` | `{"success": false, "error": "..."}` | com.familysearch.service.MatchService | 产品立项文件 3.1 寻根匹配模块 |
| `ApplicationService.submitApplication()` | 提交认祖申请 | application: Application 申请对象 | `{"success": true, "data": {"applicationId": "...", "status": "pending"}}` | `{"success": false, "error": "..."}` | com.familysearch.service.ApplicationService | 产品立项文件 3.1 寻根匹配模块 |
| `ApplicationService.reviewApplication()` | 审核认祖申请 | applicationId: String 申请ID<br>status: String 审核状态 | `{"success": true, "data": {"status": "approved/rejected"}}` | `{"success": false, "error": "..."}` | com.familysearch.service.ApplicationService | 产品立项文件 3.1 寻根匹配模块 |
| `TabletService.generateTablet()` | 生成表字 | userId: String 用户ID<br>clanId: String 宗族ID | `{"success": true, "data": {"tablet": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.TabletService | 产品立项文件 3.1 寻根匹配模块 |

### 4.2 族谱管理模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `GenealogyService.createGenealogy()` | 创建族谱 | genealogy: Genealogy 族谱对象 | `{"success": true, "data": {"genealogyId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.GenealogyService | 产品立项文件 3.2 族谱信息化模块 |
| `GenealogyService.updateGenealogy()` | 更新族谱 | genealogyId: String 族谱ID<br>genealogy: Genealogy 族谱对象 | `{"success": true, "data": {"genealogyId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.GenealogyService | 产品立项文件 3.2 族谱信息化模块 |
| `GenealogyService.getGenealogy()` | 获取族谱 | genealogyId: String 族谱ID | `{"success": true, "data": Genealogy对象}` | `{"success": false, "error": "..."}` | com.familysearch.service.GenealogyService | 产品立项文件 3.2 族谱信息化模块 |
| `PermissionService.setPermission()` | 设置权限 | genealogyId: String 族谱ID<br>permission: Permission 权限对象 | `{"success": true}` | `{"success": false, "error": "..."}` | com.familysearch.service.PermissionService | 产品立项文件 3.2 族谱信息化模块 |
| `DocumentService.uploadDocument()` | 上传家族文献 | document: Document 文献对象<br>file: MultipartFile 文件 | `{"success": true, "data": {"documentId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.DocumentService | 产品立项文件 3.2 族谱信息化模块 |

### 4.3 宗亲互动模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `ChatService.createChatRoom()` | 创建聊天室 | clanId: String 宗族ID | `{"success": true, "data": {"chatRoomId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.ChatService | 产品立项文件 3.3 宗亲互动模块 |
| `ChatService.sendMessage()` | 发送消息 | chatRoomId: String 聊天室ID<br>message: Message 消息对象 | `{"success": true, "data": {"messageId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.ChatService | 产品立项文件 3.3 宗亲互动模块 |
| `ActivityService.createActivity()` | 创建宗族活动 | activity: Activity 活动对象 | `{"success": true, "data": {"activityId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.ActivityService | 产品立项文件 3.3 宗亲互动模块 |
| `ActivityService.registerActivity()` | 报名活动 | activityId: String 活动ID<br>userId: String 用户ID | `{"success": true}` | `{"success": false, "error": "..."}` | com.familysearch.service.ActivityService | 产品立项文件 3.3 宗亲互动模块 |
| `FamilyCultureService.shareFamilyCulture()` | 分享祖训家风 | culture: FamilyCulture 文化对象 | `{"success": true, "data": {"cultureId": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.FamilyCultureService | 产品立项文件 3.3 宗亲互动模块 |
| `CardService.generateCard()` | 生成宗亲名片 | userId: String 用户ID | `{"success": true, "data": Card对象}` | `{"success": false, "error": "..."}` | com.familysearch.service.CardService | 产品立项文件 3.3 宗亲互动模块 |

### 4.4 辅助功能模块

| 类/函数名 | 说明 | 参数（类型/含义） | 成功返回结构/类型 | 失败返回结构/类型 | 所属文件/模块 | 溯源 |
|----------|------|-----------------|-----------------|-----------------|--------------|------|
| `AuthService.register()` | 用户注册 | user: User 用户对象 | `{"success": true, "data": {"userId": "...", "token": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.AuthService | 产品立项文件 3.4 辅助功能 |
| `AuthService.login()` | 用户登录 | username: String 用户名<br>password: String 密码 | `{"success": true, "data": {"userId": "...", "token": "..."}}` | `{"success": false, "error": "..."}` | com.familysearch.service.AuthService | 产品立项文件 3.4 辅助功能 |
| `AuthService.verifyIdentity()` | 身份验证 | userId: String 用户ID<br>identityInfo: IdentityInfo 身份信息 | `{"success": true}` | `{"success": false, "error": "..."}` | com.familysearch.service.AuthService | 产品立项文件 3.4 辅助功能 |
| `NotificationService.sendNotification()` | 发送通知 | notification: Notification 通知对象 | `{"success": true}` | `{"success": false, "error": "..."}` | com.familysearch.service.NotificationService | 产品立项文件 3.4 辅助功能 |
| `SearchService.search()` | 搜索功能 | keyword: String 关键词<br>type: String 搜索类型 | `{"success": true, "data": {"results": [...]}}` | `{"success": false, "error": "..."}` | com.familysearch.service.SearchService | 产品立项文件 3.4 辅助功能 |

## 5. 依赖关系

### 5.1 前端依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| React Native | 0.70+ | 跨平台移动应用开发 | 产品立项文件 4.2 技术可行性 |
| Redux | 4.2+ | 状态管理 | 常见前端技术栈 |
| Axios | 1.3+ | API请求 | 常见前端技术栈 |
| WebSocket | - | 实时通信 | 产品立项文件 3.3 宗亲互动模块 |
| React Navigation | 6.0+ | 路由导航 | 常见前端技术栈 |
| styled-components | 5.3+ | 样式管理 | 常见前端技术栈 |

### 5.2 后端依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| Spring Boot | 3.0+ | 后端框架 | 产品立项文件 4.2 技术可行性 |
| Spring Security | 6.0+ | 安全认证 | 产品立项文件 3.4 辅助功能 |
| JWT | 0.11+ | 身份令牌 | 产品立项文件 3.4 辅助功能 |
| Spring Data JPA | 3.0+ | 数据访问 | 常见后端技术栈 |
| MongoDB | 4.4+ | 文档数据库 | 产品立项文件 3.2 族谱信息化模块 |
| Redis | 7.0+ | 缓存和实时数据 | 产品立项文件 3.3 宗亲互动模块 |
| Elasticsearch | 8.0+ | 搜索和大数据分析 | 产品立项文件 3.1 寻根匹配模块 |
| WebSocket | - | 实时通信 | 产品立项文件 3.3 宗亲互动模块 |
| AWS S3 | - | 对象存储 | 产品立项文件 3.2 族谱信息化模块 |

### 5.3 大数据依赖

| 依赖名称 | 版本 | 用途 | 溯源 |
|---------|------|------|------|
| Python | 3.9+ | 数据分析 | 产品立项文件 4.2 技术可行性 |
| TensorFlow | 2.10+ | 机器学习 | 产品立项文件 3.1 寻根匹配模块 |
| NetworkX | 2.8+ | 知识图谱构建 | 产品立项文件 3.1 寻根匹配模块 |
| Pandas | 1.5+ | 数据处理 | 常见大数据技术栈 |
| NumPy | 1.24+ | 数值计算 | 常见大数据技术栈 |

## 6. 项目运行方式

### 6.1 开发环境

**前端开发环境**：
1. 安装 Node.js 16+ 和 npm 8+
2. 安装 React Native CLI
3. 安装 iOS/Android 开发环境
4. 克隆代码仓库
5. 执行 `npm install` 安装依赖
6. 执行 `npx react-native run-ios` 或 `npx react-native run-android` 启动开发服务器

**后端开发环境**：
1. 安装 JDK 17+
2. 安装 Maven 3.8+
3. 安装 MongoDB、Redis、Elasticsearch
4. 克隆代码仓库
5. 执行 `mvn clean install` 构建项目
6. 执行 `mvn spring-boot:run` 启动后端服务

**大数据服务**：
1. 安装 Python 3.9+
2. 安装所需 Python 依赖
3. 启动知识图谱服务
4. 启动匹配算法服务

### 6.2 生产环境

**部署架构**：
- 前端：通过 App Store 和 Google Play 发布
- 后端：部署在云服务器上，使用容器化技术
- 数据库：使用云数据库服务
- 存储：使用对象存储服务
- 缓存：使用云缓存服务
- 搜索引擎：使用云搜索服务

**配置管理**：
- 使用环境变量管理配置
- 不同环境（开发、测试、生产）使用不同配置
- 敏感信息通过密钥管理服务存储

**监控与维护**：
- 应用性能监控
- 日志收集与分析
- 自动告警机制
- 定期数据备份

### 6.3 API 文档

API 文档使用 Swagger 生成，可通过以下地址访问：
- 开发环境：http://localhost:8080/swagger-ui.html
- 生产环境：https://api.familysearch.com/swagger-ui.html

## 7. 目录结构

```
├── frontend/                  # 前端代码
│   ├── src/                   # 源代码
│   │   ├── components/        # 组件
│   │   ├── screens/           # 页面
│   │   ├── services/          # API 服务
│   │   ├── redux/             # 状态管理
│   │   └── utils/             # 工具函数
│   ├── public/                # 静态资源
│   └── package.json           # 依赖配置
├── backend/                   # 后端代码
│   ├── src/                   # 源代码
│   │   ├── main/java/com/familysearch/  # Java 代码
│   │   │   ├── controller/    # 控制器
│   │   │   ├── service/       # 服务层
│   │   │   ├── repository/    # 数据访问
│   │   │   ├── model/         # 数据模型
│   │   │   ├── config/        # 配置
│   │   │   └── utils/         # 工具类
│   │   └── resources/         # 资源文件
│   ├── pom.xml                # Maven 配置
│   └── Dockerfile             # Docker 配置
├── bigdata/                   # 大数据代码
│   ├── src/                   # 源代码
│   │   ├── matching/          # 匹配算法
│   │   ├── knowledgegraph/    # 知识图谱
│   │   └── utils/             # 工具函数
│   ├── requirements.txt       # Python 依赖
│   └── Dockerfile             # Docker 配置
├── docs/                      # 文档
│   ├── api/                   # API 文档
│   ├── architecture/          # 架构文档
│   └── user/                  # 用户文档
└── README.md                  # 项目说明
```

## 8. 关键技术点

### 8.1 知识图谱构建

**技术要点**：
- 使用 NetworkX 构建宗族关系知识图谱
- 基于姓氏、堂号、始祖信息等构建实体和关系
- 支持图谱的查询和分析

**应用场景**：
- 宗亲匹配算法的基础
- 族谱关系的可视化展示
- 家族历史的追溯和分析

### 8.2 大数据匹配算法

**技术要点**：
- 使用机器学习算法进行宗亲匹配
- 基于多维度特征进行相似度计算
- 支持实时匹配和批量匹配

**应用场景**：
- 寻根匹配功能
- 潜在宗亲推荐
- 族谱关联分析

### 8.3 实时通信

**技术要点**：
- 使用 WebSocket 实现实时聊天
- 支持群组聊天和一对一聊天
- 消息的持久化存储

**应用场景**：
- 宗亲聊天室
- 活动通知
- 实时消息推送

### 8.4 安全认证

**技术要点**：
- 采用 JWT 进行身份认证
- 实现多因素认证
- 数据加密和权限控制

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
- 采用前后端分离架构
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