# 会展布展搭建管理平台

面向展会立项、展位分配、展位设计、搭建施工、用电申报与消防验收的一体化布展管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 展会立项 | `project` | 展会项目 | 项目编号、展会名称、主办单位 |
| 展位分配 | `booth` | 展位 | 展位编号、所属展会、展馆区域 |
| 参展单位 | `exhibitor` | 参展单位 | 单位编码、单位名称、单位类型 |
| 展位设计 | `design` | 设计图纸 | 图纸编号、所属展位、设计单位 |
| 搭建施工 | `construction` | 施工任务 | 任务编号、所属展位、承建单位 |
| 展具租赁 | `material` | 租赁单 | 租赁单号、展具名称、展具规格 |
| 用电申报 | `power` | 用电申请单 | 申请单号、所属展位、用电容量 |
| 消防验收 | `fire` | 消防验收单 | 验收单号、所属展位、检查项目 |
| 现场安全 | `safety` | 安全巡查 | 巡查编号、巡查区域、巡查事项 |
| 安保通行 | `security` | 通行证件 | 证件编号、持证人员、所属单位 |
| 展品运输 | `logistics` | 运输任务 | 任务编号、所属展位、展品件数 |
| 撤展清运 | `cleaning` | 清运任务 | 任务编号、所属展位、清运内容 |
| 排期计划 | `schedule` | 排期计划 | 计划编号、所属展会、施工阶段 |
| 布展收费 | `fee` | 收费单 | 收费单号、参展单位、收费项目 |
| 承建单位 | `contractor` | 承建单位 | 单位编码、单位名称、资质等级 |
| 投诉处理 | `complaint` | 投诉记录 | 投诉编号、投诉单位、投诉事由 |
| 项目结算 | `settlement` | 结算单 | 结算单号、参展单位、结算周期 |
| 展会复盘 | `review` | 复盘记录 | 复盘编号、所属展会、复盘维度 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
