# Video Codec Core Architecture Dashboards

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](#)




> **开源协议声明 (License & Copyright)**
> 本仓库包含的架构文档、设计思路及配套代码均采用 **CC BY-NC 4.0 (知识共享-署名-非商业性使用)** 协议发布。
> 允许个人学习、学术研究及开源技术交流。**严格禁止任何企业或个人将其直接或间接用于任何商业目的**（包括但不限于商业芯片研发、企业内部培训、闭源软件开发等）。如需商业使用，请与作者联系获取单独授权。

Welcome to the **Video Codec Ultimate Dashboard Monorepo**. This unified knowledge base consolidates the detailed hardware architectures, algorithm derivations, and system specifications for the core video codec modules.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience.

---

## 核心模块 (Module Directory)

You can directly access the documentation for each subsystem via the following links:

| Module | Subsystem | Target Audience |
|---|---|---|
| [**Rate Control**](./modules/rate_control/README.md) | Rate Control & Virtual Buffer | System Architects, Firmware |
| [**RDO**](./modules/rdo/README.md) | Transform Core & RDOQ Optimization | RDO Architects, RTL Designers |
| [**CABAC**](./modules/cabac/README.md) | HEVC/VVC Entropy Encoding | Algorithm Engineers, RTL |
| [**Inter Pred**](./modules/inter_pred/README.md) | Motion Estimation / Compensation | Core RTL, Verification |
| [**Intra Pred**](./modules/intra_pred/README.md) | Spatial Prediction & Filtering | Core RTL, Algorithm |
| [**Deblock**](./modules/deblock/README.md) | Deblocking Filter (DBF) | RTL Designers, Firmware |
| [**SAO**](./modules/sao/README.md) | Sample Adaptive Offset | RTL Designers |
| [**Doc Skills**](./doc_skills/README.md) | Interactive Doc Generation & Deployment | System Architects, RTL |

---

## 架构哲学 (Monorepo Philosophy)

This repository is designed to be **clean and purely web-facing**. We embrace the following principles across all modules:

- **Clean Structure**: A unified Monorepo structure categorizing the vast codec IP ecosystem.
- **Zero Horizontal Scrolling**: All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX**: We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.
- **Strict Objective Truth**: We reject subjective metaphors in favor of mathematically and physically rigorous documentation (per `doc-skills` specifications).
