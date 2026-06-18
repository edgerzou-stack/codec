# Inter Prediction Architecture Design

![Architecture](https://img.shields.io/badge/Hardware-Architecture-3b82f6?style=for-the-badge)
![HEVC/VVC](https://img.shields.io/badge/HEVC%2FVVC-Inter_Prediction-ec4899?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge)

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

## 🛠️ Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean. All intermediate scripts remain on the local machine.
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX:** We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.

---
*Maintained by the Core Architecture Team.*
