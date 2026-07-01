# HEVC CABAC EMC Dashboard

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](#)



Welcome to the **HEVC CABAC EMC Dashboard** repository. This repository serves as a highly interactive, web-based visualization sandbox designed specifically to demystify the underlying hardware logic and arithmetic coding engine (CABAC) of the HEVC (H.265) video coding standard.

All documentation is generated and hosted statically via GitHub Pages, ensuring an interactive, highly readable, and zero-drag "Geek Dashboard" experience for hardware and algorithm engineers.

## Live Document Links (GitHub Pages)

You can directly access the interactive online documentation via the following link:

### [HEVC CABAC EMC Hardware Interactive Sandbox](https://edgerzou-stack.github.io/hevc-cabac-emc-dashboard/index.html)
- **Target Audience:** RTL Designers, Algorithm Engineers, and Video Codec Researchers.
- **Content:** An interactive breakdown of the Entropy Coding Module (EMC) scheduling, the CABAC compression engine, and the bitstream decryption mechanics.
- **Highlights:**
  - **Z-Scan Spatial Engine:** Visualizes the 64x64 CTU depth stack and asynchronous FIFO architecture.
  - **Interactive Binarization & Range LUT:** Manually step through the multiplication-free Range interval splitting.
  - **Interactive Context (Ctx) Modeling Sandbox:** Features a dual-mode (Manual/Auto-play) state machine visualization, instantly mapping spatial PU conditions to `ContextModel3DBuffer` 1D array indices and revealing the internal `pStateIdx` 6-bit registers.
  - **Mathematical Demystification:** Employs MathJax LaTeX rendering to break down the probability-to-bits theoretical pipeline ($P_{LPS}$ exponential decay $\rightarrow$ 15-bit fixed-point fractional `m_entropyBits`).
  - **5-Pass Coeff Scanning:** An animated derivation of the hardware-friendly 5-pass reverse diagonal scanning mechanism for residual coefficients.

## Local Deployment

Since this platform is a pure single-file frontend application (HTML + Vanilla JS + Native CSS), it requires **zero dependencies and zero build configuration**!

1. `git clone` this repository.
2. Double-click `index.html` in any modern browser to explore the interactive simulations.

---
*Created and maintained by edgerzou-stack.*


---


## Content Index

| Item | Type | Description |
|---|---|---|
| `index.html` | **File** | Interactive HTML Dashboard |

---

## License & Copyright
> **开源协议声明 (License & Copyright)**
> 本仓库包含的架构文档、设计思路及配套代码均采用 **CC BY-NC 4.0 (知识共享-署名-非商业性使用)** 协议发布。
> 允许个人学习、学术研究及开源技术交流。**严格禁止任何企业或个人将其直接或间接用于任何商业目的**（包括但不限于商业芯片研发、企业内部培训、闭源软件开发等）。如需商业使用，请与作者联系获取单独授权。
