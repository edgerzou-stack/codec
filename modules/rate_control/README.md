# Rate Control Architecture Dashboard

![Architecture](https://img.shields.io/badge/Architecture-Rate_Control-3b82f6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge)

Welcome to the **Rate Control Architecture Dashboard** repository. This repository hosts a specialized, interactive dashboard detailing the closed-loop Rate Control system for modern video encoders.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience for hardware engineers, algorithm designers, and firmware developers.

## 📖 Live Document Link (GitHub Pages)

You can directly access the interactive online documentation via the following link:

### 🌟 1. [Rate Control & Virtual Buffer Architecture](https://edgerzou-stack.github.io/rate-control-dashboard/html/rate_control_dashboard.html)
- **Target Audience:** RTL Designers, Firmware Engineers, System Architects.
- **Content:** Demystifying the rate control (RC) closed-loop system, from HRD Virtual Buffer concepts to C-Model Bit Allocation (`targetPicSize`) and Linear Regression R-Q updates.
- **Highlights:**
  - Complete decoupling of **ABR/CBR (Target Bitrate)** and **CRF (Constant Rate Factor)** modes.
  - Interactive "Water Pipe and Reservoir" economic analogy for Virtual Buffer (VBV) safety margins.
  - Granular breakdown of temporal exponential moving average (EMA) and spatial nonlinear folding (`qCompress`).
  - Strict formal spec derivation avoiding non-standard metaphorical language.

## 🛠️ Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean.
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX:** We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.

---
*Maintained by the RDO Core Design Team.*
