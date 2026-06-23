# Video Codec Core Architecture Dashboards

![Architecture](https://img.shields.io/badge/Hardware-Architecture-3b82f6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge)

Welcome to the **Video Codec Ultimate Dashboard Monorepo**. This unified knowledge base consolidates the detailed hardware architectures, algorithm derivations, and system specifications for the core video codec modules.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience.

## 📖 Module Directory (Live Dashboards)

You can directly access the interactive online documentation for each subsystem via the following links:

| Module | Subsystem | Live Dashboard Link | Target Audience |
|---|---|---|---|
| 🎛️ [**Rate Control**](./rate_control/README.md) | Rate Control & Virtual Buffer | [Launch Dashboard](https://edgerzou-stack.github.io/codec/rate_control/html/rate_control_dashboard.html) | System Architects, Firmware |
| 🧮 [**RDO**](./rdo/README.md) | Transform Core & RDOQ Optimization | [Launch Dashboard](https://edgerzou-stack.github.io/codec/rdo/html/index.html) | RDO Architects, RTL Designers |
| 📦 [**CABAC**](./cabac/README.md) | HEVC/VVC Entropy Encoding | [Launch Dashboard](https://edgerzou-stack.github.io/codec/cabac/index.html) | Algorithm Engineers, RTL |
| 🔍 [**Inter Pred**](./inter_pred/README.md) | Motion Estimation / Compensation | [Launch Dashboard](https://edgerzou-stack.github.io/codec/inter_pred/html/inter_prediction_architecture.html) | Core RTL, Verification |
| 🔮 [**Intra Pred**](./intra_pred/README.md) | Spatial Prediction & Filtering | [Launch Dashboard](https://edgerzou-stack.github.io/codec/intra_pred/index.html) | Core RTL, Algorithm |
| 🧹 [**Deblock**](./deblock/README.md) | Deblocking Filter (DBF) | [Launch Dashboard](https://edgerzou-stack.github.io/codec/deblock/cmodel_deblock_dashboard.html) | RTL Designers, Firmware |
| 🎨 [**SAO**](./sao/README.md) | Sample Adaptive Offset | [Launch Dashboard](https://edgerzou-stack.github.io/codec/sao/cmodel_sao_dashboard.html) | RTL Designers |

> **Note**: If a link fails to load immediately after deployment, please allow a few minutes for GitHub Pages to complete the build process.

## 🛠️ Monorepo Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles across all modules:
- **Clean Structure**: A unified Monorepo structure categorizing the vast codec IP ecosystem.
- **Zero Horizontal Scrolling**: All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX**: We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.
- **Strict Objective Truth**: We reject subjective metaphors in favor of mathematically and physically rigorous documentation (per `doc-skills` specifications).

---
*Maintained by the Codec Core Design Team.*
