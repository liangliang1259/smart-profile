# Smart Profile

一个智能的个人信息生成工具，支持生成精美的个人介绍图片并分享到社交媒体。

## 功能特点

- 支持手动输入个人信息
- 支持从LinkedIn、GitHub等平台导入信息
- AI驱动的内容优化
- 精美的模板系统
- 一键分享到社交媒体

## 技术栈

### 后端
- Python 3.9+
- FastAPI
- MySQL
- Redis
- Kimi AI API

### 前端
- Vue 3
- TypeScript
- Element Plus
- Pinia
- Vite

## 开始使用

### 后端设置

1. 创建虚拟环境并安装依赖：
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows使用: .\venv\Scripts\activate
pip install -r requirements.txt
```

2. 设置环境变量：
复制 `.env.example` 到 `.env` 并填写必要的配置信息。

3. 运行数据库迁移：
```bash
alembic upgrade head
```

4. 启动后端服务：
```bash
uvicorn app.main:app --reload
```

### 前端设置

1. 安装依赖：
```bash
cd frontend
npm install
```

2. 启动开发服务器：
```bash
npm run dev
```

## API文档

启动后端服务后，访问 http://localhost:8000/docs 查看API文档。

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT
