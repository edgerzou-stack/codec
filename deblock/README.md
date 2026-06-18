# C-Model Deblock Architecture Design

![Architecture](https://img.shields.io/badge/Algorithm-Architecture-3b82f6?style=for-the-badge)
![C-Model Deblock](https://img.shields.io/badge/C--Model-Deblock-ec4899?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge)

Welcome to the **C-Model Deblock Architecture Design** repository. This repository serves as a centralized hub for modern, web-based C-model algorithm specifications and workflow dashboards.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience for algorithm engineers and developers.

## 📖 Live Document Links (GitHub Pages)

You can directly access the interactive online documentation via the following link:

### 🌟 1. [C-Model Deblock Architecture Dashboard](https://edgerzou-stack.github.io/cmodel-deblock-doc/cmodel_deblock_dashboard.html)
- **Target Audience:** Algorithm Engineers, Software Developers, and Hardware Architects.
- **Content:** An overview of the entire C-Model Deblocking (去块滤波) architecture, primarily focusing on HEVC/VVC standards as implemented in the KHEnc codebase.
- **Highlights:**
  - Auto-stretching, zero-drag Mermaid hierarchy graphs for Boundary Strength (BS) decision logic.
  - Interactive sidebar navigation with glassmorphism UI elements.
  - Native CSS spatial diagrams mapping physical pixel positions to C-Model array pointer representations (`p[0]`, `p[-1]`).
  - Visual influence ranges and core formulas for Luma/Chroma weak, strong, and VVC long-tap filters.

## 🛠️ Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean. All intermediate scripts or notes remain on the local machine.
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Geek UI/UX:** We bring modern Web UI principles (glassmorphism, high-contrast alerts) into algorithm and architecture specification viewing.

---
*Maintained by the Core Algorithm Design Team.*
