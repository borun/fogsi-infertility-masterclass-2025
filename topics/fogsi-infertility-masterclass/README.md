# 🧬 FOGSI-ICOG & ISAR Infertility Masterclass E-Learning Portal

Part of the **[MedEd Open Platform](../../README.md)**.

## 📌 Overview

This directory contains the curriculum and interactive viewer for the **FOGSI-ICOG & ISAR Certificate Course on Infertility**.

The platform organizes over 9 hours of clinical masterclasses into a highly accessible, single-page application (SPA) powered by Markdown syllabus notes, precision-timed video playback, and interactive progress tracking.

* **Live Course Interactive Viewer:** [Open Course Viewer](index.html)
* **Main MedEd Discovery Portal:** [Open MedEd Hub](../../index.html)

---

## ✨ Key Features

* **🎬 Precision Video Playback:** Integrates the YouTube IFrame API to automatically jump to specific lecture segments using exact `startSeconds` and `endSeconds` timestamps.
* **🧠 Markdown-Driven Clinical Summaries:** Each module features quick-reference clinical notes, WHO 6th Edition semen analysis criteria, Poseidon stratification tables, and evidence-based ART protocols.
* **✅ Local Progress Tracking:** Save your lecture completion status automatically to browser `localStorage` without requiring sign-ins or servers.
* **🔍 Real-Time Search:** Instantly filter lectures across the active day by speaker name, topic, or clinical keywords.
* **📱 Responsive Clinical UI:** Designed for comfortable reading and viewing on smartphones, iPads, tablets, and desktop workstations.

---

## 📚 Curriculum Structure

All syllabus content and clinical notes are organized as modular Markdown files in [`content/`](content/):

| Day | Topic Focus | Content File |
| :--- | :--- | :--- |
| **Day 1** | Male Factor Evaluation, Genetics & IUI Protocols | [`content/day1.md`](content/day1.md) |
| **Day 2** | Female Infertility, Endoscopy & Endometrial Receptivity | [`content/day2.md`](content/day2.md) |
| **Day 3** | Advanced ART, Embryology & Maximizing Success | [`content/day3.md`](content/day3.md) |

---

## 🛠️ Tech Stack

* **Structure:** HTML5 + Markdown (`content/*.md`)
* **Markdown Parser:** [Marked.js](https://marked.js.org/)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/)
* **State Management:** Vanilla ES6 JavaScript + `localStorage`
* **Media:** YouTube IFrame API
* **Icons & Typography:** FontAwesome 6 + Google Fonts (`Plus Jakarta Sans`, `JetBrains Mono`)

---

## ⚖️ Attribution & Disclaimer

This project is created for open educational purposes to index and organize publicly available webinars from FOGSI-ICOG & ISAR. All medical video recordings, logos, and presentation copyrights belong to the respective original speakers and medical societies.