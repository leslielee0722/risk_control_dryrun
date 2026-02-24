# 企业信用风险智能评估演示系统

> 基于大语言模型的全链路金融风控解决方案

## 项目概述

本项目是一个现代化的企业信用风险智能评估演示系统，整合了数据工程、模型训练、智能推理和风险预警等核心功能。系统采用前后端分离架构，提供统一的用户界面和交互体验，旨在为金融机构提供从风险评估到预警处置的端到端解决方案。

### 核心特性

- **全链路流程可视化**：展示从风控数据到预警处置的完整业务流程
- **多模块协同工作**：集成开发平台、告警清单、预警服务和数据飞轮四大核心模块
- **AI驱动决策**：深度集成大语言模型（LLM），实现智能推理和风险分析
- **现代化UI设计**：采用玻璃拟态（Glassmorphism）设计风格，提供优秀的视觉体验
- **热重载开发环境**：支持实时预览和快速迭代开发

## 核心功能模块

### 1. 总览页面（Overview）

系统入口页面，展示业务场景全链路流程和四大核心模块导航。

- **业务流程可视化**：直观展示从风控数据、风控模型、预警加工到预警处置的完整流程
- **数据飞轮机制**：展示模型闭环优化和智能反馈循环
- **模块快速导航**：提供四个核心模块的快速访问入口

### 2. 信用风险预警智能开发平台

基于Flask的全栈开发平台，提供数据工程和模型训练两大流水线。

#### 数据工程流水线
- **多源数据管理**：集成和管理来自不同来源的数据
- **特征工程**：自动化的特征筛选和处理能力
- **COT数据合成**：利用大语言模型自动生成思维链（Chain of Thought）推理样本

#### 模型训练流水线
- **模型效果评估**：多模型差异对比分析功能
- **性能可视化**：模型性能和行为的可视化比较

### 3. 总行告警清单

总行级风险预警统一管控中心。

- **跨区域风险聚合**：提供跨区域、跨系统的风险信息聚合看板
- **总部直达督办**：支持总部直达督办能力
- **风险评估生成**：基于大模型的风险评估和归因解释
- **客户评估明细**：详细的客户风险评估数据展示

### 4. 风险预警服务平台

普惠业务客户经理工作平台。

- **风险核实处理**：针对贷后风险报告进行风险核实
- **闭环处理流程**：辅助决策与报告生成
- **客户核查管理**：客户经理专属的风险处理工作台

### 5. 数据飞轮平台

基于内容回复进行模型迭代的运营平台。

- **知识萃取**：违约情况知识萃取
- **语料构建**：模型训练语料构建
- **策略调整**：支持策略动态调整

## 技术栈

### 前端技术

| 技术 | 版本 | 用途 |
|------|------|------|
| Tailwind CSS | 3.x | CSS框架，实现现代化UI设计 |
| Alpine.js | - | 轻量级JavaScript框架，处理前端交互 |
| Material Symbols | - | Google图标库 |
| Noto Sans SC | - | 中文字体，提供优秀的中文显示效果 |
| Font Awesome | 6.4.0 | 图标库（部分模块使用） |

### 后端技术

| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.14+ | 主要编程语言 |
| Flask | - | Web框架 |
| Pandas | - | 数据处理和分析 |
| NumPy | - | 数值计算 |
| LightGBM | - | 机器学习模型 |
| scikit-learn | - | 机器学习工具库 |
| Matplotlib | - | 数据可视化 |
| OpenAI API | - | 大语言模型接口 |
| requests | - | HTTP请求库 |

### 开发工具

| 工具 | 用途 |
|------|------|
| livereload | 开发服务器热重载 |
| openpyxl | Excel文件处理 |

## 环境要求

- **Python**: 3.14 或更高版本
- **操作系统**: macOS, Linux, Windows
- **浏览器**: Chrome, Firefox, Safari, Edge（推荐使用最新版本）
- **内存**: 至少 4GB RAM
- **磁盘空间**: 至少 2GB 可用空间

## 项目结构

```
dryrun_code_v1/
├── overview/                          # 总览页面
│   └── overview_code.html             # 主入口页面
├── development_platform/              # 信用风险预警智能开发平台（Flask应用）
│   ├── app/
│   │   ├── routes/                   # 路由定义
│   │   │   ├── main.py              # 主路由
│   │   │   ├── data_tool.py         # 数据工具路由
│   │   │   └── risk_cot/            # 大模型风控路由
│   │   ├── services/                # 核心服务逻辑
│   │   │   ├── data_core/           # 数据处理服务
│   │   │   └── risk_cot/            # 大模型风控服务
│   │   ├── templates/               # Jinja2模板
│   │   └── __init__.py              # Flask应用工厂
│   ├── config/                      # 配置文件
│   ├── data/                        # 数据文件
│   ├── docs/                        # 文档
│   ├── scripts/                     # 脚本工具
│   ├── requirements.txt              # Python依赖
│   ├── run.py                       # Flask应用启动脚本
│   └── README.md                    # 开发平台文档
├── headquarters_alarm_list/          # 总行告警清单
│   └── headquarters_alarm_list.html  # 告警清单页面
├── warning_service_platform/         # 风险预警服务平台
│   └── warning_service_platform_v5.html # 预警服务页面
├── operations_platform/              # 数据飞轮平台
│   └── operations_paltform.html     # 运营平台页面
├── index.html                       # 重定向页面
├── start.py                         # 一键启动脚本
├── serve.py                         # 开发服务器（热重载）
├── requirements.txt                  # 项目依赖
└── README.md                        # 本文档
```

## 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd dryrun_code_v1
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

项目使用环境变量来配置服务器IP地址和端口号，方便在不同环境中部署。

**创建环境变量文件：**

```bash
# 复制环境变量模板
cp .env.example .env
```

**编辑 `.env` 文件：**

```env
# 服务器IP配置
SERVER_IP=127.0.0.1
STATIC_SERVER_PORT=9090
FLASK_SERVER_PORT=8465
```

**环境变量说明：**

| 变量名                  | 说明        | 默认值         |
| -------------------- | --------- | ------------ |
| `SERVER_IP`          | 服务器IP地址   | `localhost`   |
| `STATIC_SERVER_PORT` | 静态服务器端口   | `9090`        |
| `FLASK_SERVER_PORT`  | Flask应用端口 | `8465`        |

**本地开发环境配置：**

如果是在本地开发，可以将 `SERVER_IP` 设置为 `localhost`：

```env
SERVER_IP=localhost
```

**部署环境配置：**

如果部署到特定服务器，将 `SERVER_IP` 设置为服务器的实际IP地址。

### 5. 配置API密钥

如需使用大语言模型功能，请配置API密钥：

编辑 `development_platform/app/services/risk_cot/cot_synthesis_service.py`：

```python
self.api_key = "YOUR_DEEPSEEK_API_KEY"
self.api_url = "https://api.deepseek.com/chat/completions"
self.model = "deepseek-reasoner"
```

### 6. 启动开发服务器

#### 方式一：使用一键启动脚本（推荐）

使用项目提供的一键启动脚本，可以同时启动两个服务：

```bash
python start.py
```

**启动脚本功能说明：**

- 自动检查依赖是否安装
- 按顺序启动服务：先启动Flask应用（端口8465），待其成功启动后再启动静态页面服务器（端口9090）
- 显示服务启动状态和访问地址
- 提供友好的错误提示
- 支持Ctrl+C优雅停止所有服务

**启动脚本输出示例：**

```
============================================================
企业信用风险智能评估演示系统 - 服务启动器
============================================================

检查依赖...
✓ 所有依赖已安装

启动服务...
------------------------------------------------------------
正在启动Flask应用 (端口 8465)...
✓ Flask应用启动成功
等待Flask服务完全启动...
✓ Flask应用运行正常

正在启动静态页面服务器 (端口 9090)...
✓ 静态页面服务器启动成功
等待静态页面服务器完全启动...
✓ 静态页面服务器运行正常

============================================================
所有服务已启动！
============================================================

访问地址:

服务名称: 总览页面
访问地址: http://100.100.135.127:9090
功能描述: 系统入口，展示业务流程和模块导航
------------------------------------------------------------

服务名称: 开发平台
访问地址: http://100.100.135.127:8465
功能描述: 数据工程和模型训练平台
------------------------------------------------------------

其他模块:
  - 告警清单: http://100.100.135.127:9090/headquarters_alarm_list/headquarters_alarm_list.html
  - 预警服务: http://100.100.135.127:9090/warning_service_platform/warning_service_platform_v5.html
  - 运营平台: http://100.100.135.127:9090/operations_platform/operations_paltform.html

============================================================
按 Ctrl+C 停止所有服务
============================================================
```

> **注意**：实际访问地址会根据 `.env` 文件中的 `SERVER_IP` 配置自动调整。

#### 方式二：手动分别启动

如果需要单独启动某个服务，可以使用以下命令：

**启动静态页面服务器（端口9090）：**

```bash
python serve.py
```

**启动Flask应用（端口8465）：**

在新的终端窗口中：

```bash
cd development_platform
python run.py
```

### 7. 访问系统

根据 `.env` 文件中的配置，访问地址如下：

- **总览页面**: http://`{SERVER_IP}`:`{STATIC_SERVER_PORT}`
- **开发平台**: http://`{SERVER_IP}`:`{FLASK_SERVER_PORT}`
- **告警清单**: http://`{SERVER_IP}`:`{STATIC_SERVER_PORT}`/headquarters_alarm_list/headquarters_alarm_list.html
- **预警服务**: http://`{SERVER_IP}`:`{STATIC_SERVER_PORT}`/warning_service_platform/warning_service_platform_v5.html
- **运营平台**: http://`{SERVER_IP}`:`{STATIC_SERVER_PORT}`/operations_platform/operations_paltform.html

> **提示**：请将 `{SERVER_IP}`、`{STATIC_SERVER_PORT}` 和 `{FLASK_SERVER_PORT}` 替换为 `.env` 文件中配置的实际值。

## 使用指南

### 访问总览页面

1. 打开浏览器访问 http://localhost:8080
2. 浏览业务场景全链路流程图
3. 点击任意模块卡片进入对应系统

### 使用开发平台

1. 访问 http://localhost:5005
2. **数据工程**：
   - 上传和管理多源数据
   - 进行特征工程和筛选
   - 生成COT思维链数据
3. **模型训练**：
   - 训练和评估模型
   - 对比不同模型性能
   - 查看模型差异分析

### 查看告警清单

1. 访问告警清单页面
2. 查看风险评估统计信息
3. 浏览客户风险评估明细
4. 点击"详情"查看归因解释

### 使用预警服务平台

1. 访问预警服务平台页面
2. 查看待处理预警任务
3. 进行风险核实和处理
4. 生成处理报告

### 管理数据飞轮

1. 访问运营平台页面
2. 查看模型迭代数据
3. 进行知识萃取
4. 调整模型策略

## 配置说明

### 启动脚本配置

项目提供了一键启动脚本 `start.py`，用于同时启动两个服务。

**脚本功能：**

| 功能 | 说明 |
|------|------|
| 依赖检查 | 自动检查Flask和livereload是否已安装 |
| 服务启动 | 同时启动静态页面服务器（8080）和Flask应用（5005） |
| 状态监控 | 实时监控服务运行状态，服务异常停止时自动退出 |
| 优雅停止 | 支持Ctrl+C优雅停止所有服务 |
| 错误处理 | 提供清晰的错误提示和解决方案 |

**使用方法：**

```bash
python start.py
```

**参数说明：**

当前版本无需额外参数，脚本会自动：

1. 检查Python环境和依赖
2. 启动静态页面服务器（端口8080）
3. 启动Flask应用（端口5005）
4. 显示服务访问地址
5. 监控服务运行状态

**错误处理：**

| 错误类型 | 提示信息 | 解决方案 |
|----------|----------|----------|
| 依赖缺失 | `✗ 缺少依赖: <package_name>` | 运行 `pip install -r requirements.txt` |
| 端口占用 | `Address already in use` | 修改对应启动脚本中的端口号 |
| 服务启动失败 | `✗ <服务名>启动失败` | 检查Python环境和依赖是否正确安装 |
| 服务异常停止 | `警告: <服务名>已意外停止` | 查看服务日志，检查错误原因 |

**自定义端口：**

如需修改端口，编辑以下文件：

- 静态页面服务器端口：编辑 `serve.py`，修改 `port=9090`
- Flask应用端口：编辑 `development_platform/run.py`，修改 `port=8465`

### 端口配置

- **静态页面服务器**: 默认端口 9090（可在 `serve.py` 中修改）
- **Flask应用**: 默认端口 8465（可在 `development_platform/run.py` 中修改）

### 样式配置

项目使用Tailwind CSS进行样式管理，主要样式定义在各个HTML文件的 `<style>` 标签中。

- **主色调**: `#3b82f6`（蓝色）
- **背景渐变**: `radial-gradient(circle at 50% 50%, #f8fafc 0%, #ffffff 100%)`
- **字体**: Noto Sans SC（中文）+ Manrope（英文）

### 数据配置

数据文件存储在 `development_platform/data/` 目录下，包括：

- CSV数据文件
- Excel数据文件
- JSON配置文件
- 缓存文件

## 常见问题解答（FAQ）

### Q1: 如何使用一键启动脚本？

**A**: 使用以下命令启动所有服务：

```bash
python start.py
```

脚本会自动：
1. 检查依赖是否安装
2. 启动静态页面服务器（端口8080）
3. 启动Flask应用（端口5005）
4. 显示服务访问地址

按 `Ctrl+C` 可以优雅停止所有服务。

### Q2: 启动脚本提示依赖缺失怎么办？

**A**: 运行以下命令安装所有依赖：

```bash
pip install -r requirements.txt
```

### Q3: 启动服务器时提示端口被占用怎么办？

**A**: 修改对应启动脚本中的端口号：

- 修改 `serve.py` 中的 `port=8080`
- 修改 `development_platform/run.py` 中的 `port=5005`

### Q4: 页面样式显示不正常？

**A**: 确保网络连接正常，因为Tailwind CSS和字体文件通过CDN加载。如果网络受限，可以考虑：

1. 使用本地Tailwind CSS构建
2. 下载字体文件到本地

### Q5: Flask应用无法启动？

**A**: 检查以下几点：

1. 确认Python版本 >= 3.14
2. 确认所有依赖已安装：`pip install -r requirements.txt`
3. 检查是否有其他应用占用5005端口

### Q6: 大语言模型功能无法使用？

**A**: 确保已正确配置API密钥：

1. 编辑 `development_platform/app/services/risk_cot/cot_synthesis_service.py`
2. 填入有效的DeepSeek API密钥
3. 检查网络连接是否正常

### Q7: 如何重置开发环境？

**A**: 执行以下步骤：

```bash
# 删除虚拟环境
rm -rf .venv

# 重新创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 重新安装依赖
pip install -r requirements.txt
```

### Q8: 热重载不工作？

**A**: 确保使用 `python start.py` 或 `python serve.py` 启动服务器，而不是直接打开HTML文件。livereload需要通过服务器运行才能正常工作。

### Q9: 服务启动后无法访问？

**A**: 检查以下几点：

1. 确认防火墙允许访问8080和5005端口
2. 确认服务已成功启动（查看启动脚本输出）
3. 尝试使用 `http://127.0.0.1:8080` 和 `http://127.0.0.1:5005` 访问
4. 检查浏览器控制台是否有错误信息

## 开发指南

### 添加新页面

1. 在对应模块目录下创建新的HTML文件
2. 遵循现有的设计规范和样式
3. 在总览页面添加导航链接

### 修改样式

项目使用Tailwind CSS，主要样式变量定义在各页面的 `<style>` 标签中：

```css
:root {
    --primary: #3b82f6;
    --primary-glow: rgba(59, 130, 246, 0.4);
    --glass-bg: rgba(255, 255, 255, 0.9);
    --glass-border: rgba(59, 130, 246, 0.15);
}
```

### 添加新功能

1. **Flask应用**：在 `app/routes/` 下添加新路由
2. **服务逻辑**：在 `app/services/` 下添加新服务
3. **前端页面**：在 `app/templates/` 下添加新模板

### 代码规范

- Python代码遵循PEP 8规范
- HTML/CSS代码遵循W3C标准
- 使用有意义的变量和函数命名
- 添加必要的注释和文档字符串

## 贡献指南

欢迎贡献代码、报告问题或提出改进建议！

### 贡献流程

1. Fork本仓库
2. 创建特性分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 提交Pull Request

### 问题反馈

如发现问题或有改进建议，请：

1. 在Issues中描述问题
2. 提供复现步骤
3. 附上相关日志和截图（如适用）

## 许可证

本项目仅供内部使用，未经授权不得用于商业用途。

## 联系方式

- **技术支持**: 技术支持热线 400-123-4567
- **项目维护**: 风控技术团队

## 更新日志

### v1.0.0 (2024-02-10)
- 初始版本发布
- 实现四大核心模块
- 集成大语言模型功能
- 完成UI风格统一

## 致谢

感谢所有为本项目做出贡献的团队成员！

---

**企业信用风险智能评估演示系统** | © 2024 Professional Enterprise Infrastructure | Version 1.0.0
