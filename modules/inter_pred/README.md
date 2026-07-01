# Inter Prediction Architecture Design

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](#)



Welcome to the **Inter Prediction Architecture Design** repository. This centralized hub documents the core hardware design philosophies, pipeline optimizations, and algorithmic decoupling mechanisms for the Inter Prediction module (Motion Estimation & Motion Compensation).

All documentation is generated and hosted statically via GitHub Pages, delivering an interactive, highly readable, zero-drag "Geek Dashboard" experience.

## 📖 Live Document Links (GitHub Pages)

You can directly access the interactive online documentation via the following links:

### 🎨 1. [Inter Prediction Architecture & ME/MC Pipeline](https://edgerzou-stack.github.io/inter-pred-architecture/html/inter_prediction_architecture.html)
- **Target Audience:** Core Inter Architects, Algorithm Engineers, RTL Designers.
- **Content:** A comprehensive analysis of multi-stage Motion Estimation, AMVR precision control, Spatial/Temporal MVP extraction, and hardware-aligned sub-pixel refinement search.
- **Highlights:**
  - Full ME pipeline visualization from coarse to sub-pixel refinement.
  - Deep dive into AMVR 4-level precision selection and MV round-trip alignment.
  - Spatial MVP 5-neighbor extraction with MTT partition compatibility.
  - TMVP cross-frame MV scaling mechanism.
  - Hardware-aligned 3×3 nine-point diamond search grid.

### 🚀 2. [Inter RDO Architecture: Eradicating Step-Delay](https://edgerzou-stack.github.io/codec/inter_pred/html/inter_rdo_pipeline_optimization.html)
- **Target Audience:** Hardware Architects, RTL Designers, Performance Engineers.
- **Content:** A deep dive into the physical delay bottlenecks of Inter Fractional Interpolation and how to achieve concurrent RDO initialization.
- **Highlights:**
  - Analysis of Intra vs Inter physical delay differences.
  - Row-level interleaving micro-architecture for time-multiplexed interpolation engines.
  - Sync-Fire Pred Buffer for staggered delay isolation.
  - Ultimate Data-Control path decoupling pipeline (Y-shape).

## 🛠️ Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean. All intermediate scripts remain on the local machine. (Note: SVGs in the assets directory are force-tracked for GitHub pages rendering).
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX:** We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.

---
*Maintained by the Core Architecture Team.*


---

## License & Copyright

> **开源协议声明 (License & Copyright)**
> 本仓库包含的架构文档、设计思路及配套代码均采用 **CC BY-NC 4.0 (知识共享-署名-非商业性使用)** 协议发布。
> 允许个人学习、学术研究及开源技术交流。**严格禁止任何企业或个人将其直接或间接用于任何商业目的**（包括但不限于商业芯片研发、企业内部培训、闭源软件开发等）。如需商业使用，请与作者联系获取单独授权。
