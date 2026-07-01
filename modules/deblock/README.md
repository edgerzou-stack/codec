# C-Model Deblock Architecture Design

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](#)



Welcome to the **C-Model Deblock Architecture Design** repository. This repository serves as a centralized hub for modern, web-based C-model algorithm specifications and workflow dashboards.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience for algorithm engineers and developers.

## Live Document Links (GitHub Pages)

You can directly access the interactive online documentation via the following link:

### 1. [C-Model Deblock Architecture Dashboard](https://edgerzou-stack.github.io/cmodel-deblock-doc/cmodel_deblock_dashboard.html)
- **Target Audience:** Algorithm Engineers, Software Developers, and Hardware Architects.
- **Content:** An overview of the entire C-Model Deblocking (去块滤波) architecture, primarily focusing on HEVC/VVC standards as implemented in the Video Codec codebase.
- **Highlights:**
  - Auto-stretching, zero-drag Mermaid hierarchy graphs for Boundary Strength (BS) decision logic.
  - Interactive sidebar navigation with glassmorphism UI elements.
  - Native CSS spatial diagrams mapping physical pixel positions to C-Model array pointer representations (`p[0]`, `p[-1]`).
  - Visual influence ranges and core formulas for Luma/Chroma weak, strong, and VVC long-tap filters.

## Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean. All intermediate scripts or notes remain on the local machine.
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Geek UI/UX:** We bring modern Web UI principles (glassmorphism, high-contrast alerts) into algorithm and architecture specification viewing.

---
*Maintained by the Core Algorithm Design Team.*


---


## Content Index

| Item | Type | Description |
|---|---|---|
| `cmodel_deblock_dashboard.html` | **File** | Interactive HTML Dashboard |

---

## License & Copyright
> **开源协议声明 (License & Copyright)**
> 本仓库包含的架构文档、设计思路及配套代码均采用 **CC BY-NC 4.0 (知识共享-署名-非商业性使用)** 协议发布。
> 允许个人学习、学术研究及开源技术交流。**严格禁止任何企业或个人将其直接或间接用于任何商业目的**（包括但不限于商业芯片研发、企业内部培训、闭源软件开发等）。如需商业使用，请与作者联系获取单独授权。
