Here is a professional and comprehensive project description that you can copy and paste directly into your GitHub repository's **`README.md`** file.

---

# 🧬 FOGSI-ICOG & ISAR Infertility Masterclass E-Learning Portal

## 📌 Overview

This repository contains the source code for a custom, fully responsive e-learning portal designed to host the **FOGSI-ICOG & ISAR Certificate Course on Infertility**.

The platform organizes over 9 hours of clinical masterclasses into a highly accessible, single-page application (SPA). It is built with medical professionals and students in mind, featuring precision-timed video playback, clinical summaries, and interactive progress tracking to streamline the learning experience.

## ✨ Key Features

* **🎬 Precision Video Playback:** Integrates the YouTube IFrame API to automatically play specific lecture segments (using precise `start` and `end` timestamps). This bypasses unnecessary transitions, introductions, and Q&A sessions, saving valuable learning time.
* **🧠 Detailed Clinical Summaries:** Each module features quick-reference clinical notes, including WHO 6th Edition semen analysis criteria, Poseidon stratification tables, and evidence-based ART protocols.
* **✅ Local Progress Tracking:** Users can mark lectures as "Completed." The application uses browser `localStorage` to save progress offline without requiring a database or user authentication.
* **🔍 Real-Time Search:** Instantly filter lectures across the active day by speaker name, topic, or specific medical keywords (e.g., *Letrozole, Micro-TESE, PCOS*).
* **📱 Fully Responsive UI:** Built with Tailwind CSS to ensure a seamless viewing experience across desktop, tablet, and mobile devices.
* **🚀 Zero Backend Required:** 100% client-side code (HTML, JS, Tailwind CSS). Highly performant and deployable directly to static hosting services like GitHub Pages.

## 📚 Curriculum Covered

### **Day 1: Male Factor Evaluation, Genetics & IUI Protocols**

* WHO 6th Edition Semen Analysis Interpretation
* Clinical Approach to Obstructive vs. Non-Obstructive Azoospermia
* Medical Management of Male Infertility & Genetic Workups
* Ovulation Induction and Semen Preparation for IUI

### **Day 2: Female Infertility, Endoscopy & Endometrial Receptivity**

* Tubal Factor Evaluation: ART vs. Reconstructive Surgery
* Hysteroscopy in Fertility Surgery
* Ovarian Reserve Assessment & Poseidon Poor Responder Management
* Managing Chronic Endometritis & Genital Tuberculosis

### **Day 3: Advanced ART, Embryology & Maximizing Success**

* Patient Selection & Early Referral for ART
* Ovarian Stimulation Protocols & OHSS Prevention
* Day 3 vs. Day 5 Embryo Transfers
* Recent Advances & Automation in the Embryology Lab

## 🛠️ Tech Stack

* **Markup:** HTML5
* **Styling:** [Tailwind CSS](https://tailwindcss.com/) (via CDN)
* **Interactivity & State Management:** Vanilla JavaScript (ES6) + `localStorage`
* **Media:** YouTube IFrame API
* **Typography & Icons:** Google Fonts (Plus Jakarta Sans, JetBrains Mono) & FontAwesome

## 💻 How to Run Locally

Because this project requires no backend, running it locally is incredibly simple:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/infertility-masterclass.git

```


2. Open the directory and double-click `index.html` to open it in any modern web browser.
3. *Note: An active internet connection is required to load the Tailwind CSS CDN, FontAwesome icons, and YouTube videos.*

## 🌐 Live Demo

*(You can add your GitHub Pages link here once you deploy it)*
**[View the Live Portal Here](https://borun.github.io/fogsi-infertility-masterclass-2025/)**

---

### 📝 License

This project is created for educational purposes to organize the publicly available webinars of the FOGSI-ICOG & ISAR certification course. Medical content and video rights belong to their respective original speakers and organizations.
