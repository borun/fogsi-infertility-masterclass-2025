# 🩺 MedEd — Open Medical E-Learning Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20On-GitHub%20Pages-teal.svg)](https://borun.github.io/meded/)
[![Access](https://img.shields.io/badge/Access-100%25%20Free%20%26%20Open-emerald.svg)](#)
[![Format](https://img.shields.io/badge/Format-Markdown%20%2B%20Interactive%20SPA-sky.svg)](#)

> **Live Platform:** [https://borun.github.io/meded/](https://borun.github.io/meded/)

---

## 📌 Mission & Vision

**MedEd** is an open-access medical e-learning platform designed for medical students, postgraduate trainees, residents, and healthcare professionals. 

Medical education today suffers from two extremes:
1. **Unstructured multi-hour webinars / conference recordings:** Filled with dead time, introductions, and Q&A sessions that make targeted review tedious.
2. **Scattered textbook notes:** Static and disconnected from expert lectures and clinical case discussions.

**MedEd bridges this gap by providing:**
* **Curated Lecture Restructuring:** Precision-timestamped video segments jumping directly to core clinical pearls.
* **Markdown-Driven Clinical Notes:** High-yield summaries, diagnostic criteria tables (e.g., WHO 6th Edition, Poseidon, FIGO), and algorithm flowcharts rendered alongside lecture streams.
* **Offline-First Progress Tracking:** Track your completed lectures with zero accounts, cookies, or tracking servers via browser `localStorage`.
* **AI-Guided Synthesis:** Clean, evidence-based distillations of complex medical topics ready for bedside consultation or exam revision.

---

## 🗂️ Course Directory & Learning Topics

| Specialty | Course / Topic | Format | Status | Duration | Interactive Portal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Reproductive / OB-GYN** | **FOGSI-ICOG & ISAR Infertility Masterclass** | Curated Masterclass | `Active` | 9+ Hours (28 Modules) | [🚀 Launch Course](topics/fogsi-infertility-masterclass/index.html) |
| **Reproductive / OB-GYN** | **Infertility Masterclass by Dr. Jay Mehta** | Curated Masterclass | `Active` | 27+ Hours (69 Modules) | [🚀 Launch Course](topics/infertility-masterclass-dr-jay-mehta/index.html) |
| **Obstetrics / Perinatology** | **Obstetric Emergencies & Labor Ward Procedures** | Curated Masterclass | `Active` | 3.5+ Hours (8 Modules) | [🚀 Launch Course](topics/obstetrics-labor-ward-emergencies/index.html) |
| **Gynecologic Surgery** | **Total Abdominal Hysterectomy (TAH) Manual** | AI-Guided Protocol | `Active` | 35 Mins (Manual + Safety) | [🚀 Launch Manual](topics/total-abdominal-hysterectomy/index.html) |
| **Cardiology** | **Clinical ECG Masterclass & Arrhythmias** | AI-Guided Protocol | `Roadmap` | 4 Hours (16 Modules) | *In Development* |
| **Critical Care** | **Mechanical Ventilation & ICU Physiology** | AI-Guided Protocol | `Roadmap` | 5 Hours (12 Modules) | *In Development* |
| **Internal Medicine** | **Clinical Antimicrobial Stewardship** | AI-Guided Protocol | `Roadmap` | 3.5 Hours (10 Modules) | *In Development* |

---

## 📂 Repository Architecture

```text
meded/
├── index.html                           # MedEd Main Discovery Portal (GitHub Pages Root)
├── README.md                            # Platform Vision, Index & Contribution Guide
├── LICENSE                              # Open Source License & Attribution Notice
├── data/
│   └── topics.json                      # Central topic registry (metadata for hub search & filters)
└── topics/
    ├── fogsi-infertility-masterclass/
    │   ├── index.html                   # Interactive course viewer & video player SPA
    │   ├── README.md                    # Course documentation & syllabus index
    │   └── content/                     # Modular day1-3 markdown syllabus
    ├── infertility-masterclass-dr-jay-mehta/
    │   ├── index.html                   # 8-phase chronological interactive viewer SPA
    │   ├── README.md                    # Course syllabus & phase index
    │   └── content/                     # Phase 1-8 structured markdown curriculum
    ├── obstetrics-labor-ward-emergencies/
    │   ├── index.html                   # Labor room procedures & PPH interactive viewer
    │   ├── README.md                    # Emergency obstetric syllabus & module index
    │   └── content/                     # Modules 1-8 structured operative protocols
    └── total-abdominal-hysterectomy/
        ├── index.html                   # Operative manual & resident safety viewer
        ├── README.md                    # Surgical syllabus & illustration index
        ├── images/                      # High-resolution anatomical & operative figures
        └── content/                     # Operative manual & ureter safety cheat sheet
```

---

## ✍️ How to Add a New Medical Topic

Adding a new course or AI-synthesized topic to MedEd is simple and requires zero backend:

### Step 1: Create the Topic Directory
Create a new directory under `topics/` with a slugified name:
```bash
mkdir -p topics/your-topic-slug/content
```

### Step 2: Write Markdown Content Files
Create `.md` files under `content/` with YAML frontmatter containing lecture timestamps and clinical notes:
```markdown
---
id: "lesson-1"
title: "Management of Severe Preeclampsia"
speaker: "Prof. Jane Doe"
videoId: "YOUTUBE_VIDEO_ID"
startSeconds: 320
endSeconds: 1450
---

### 📋 Key Clinical Takeaways
- Magnesium Sulfate loading: 4g IV over 20 mins followed by 1g/hr infusion.
- Blood pressure threshold for emergency antihypertensives: SBP ≥ 160 or DBP ≥ 110 mmHg.
```

### Step 3: Register Topic in `data/topics.json`
Add an entry in `data/topics.json` so the course appears automatically on the homepage filter and search engine:
```json
{
  "id": "your-topic-slug",
  "title": "Severe Preeclampsia & Eclampsia Masterclass",
  "subtitle": "Emergency Protocols & Management",
  "category": "Reproductive Medicine / OB-GYN",
  "categorySlug": "obgyn",
  "type": "AI-Guided Clinical Protocol",
  "typeSlug": "ai-guided",
  "status": "Active",
  "duration": "2.5 Hours",
  "path": "topics/your-topic-slug/index.html",
  "tags": ["Preeclampsia", "Hypertension", "OB-GYN", "Critical Care"]
}
```

---

## 🧪 Testing & Local Preview (Pre-Commit Checks)

To guarantee you never push broken links, malformed Markdown, or invalid JSON, MedEd includes a built-in automated test suite and zero-dependency preview server:

### 1. Run the Platform Test Suite
Runs in under 1 second and checks JSON schemas, Markdown frontmatter, HTML syntax, and all relative links:
```bash
python3 scripts/validate.py
```

### 2. Start the Local Preview Server
Validates the codebase and immediately opens `http://localhost:8000` in your browser with cache-busting enabled:
```bash
python3 scripts/dev.py
```

### 3. Continuous Integration (CI)
A GitHub Actions workflow ([`.github/workflows/test.yml`](.github/workflows/test.yml)) automatically runs `scripts/validate.py` on every Push or Pull Request, ensuring the public GitHub Pages site is never broken.

---

## 🛠️ Tech Stack & Philosophy

* **100% Static & Zero Build Step:** Runs directly on GitHub Pages with vanilla HTML5, CSS, and modern JavaScript (ES6).
* **Marked.js:** Dynamic client-side Markdown parser for fast rendering of clinical tables, blockquotes, and lists.
* **Tailwind CSS:** Modern clinical dark/light design system with responsive layouts for mobile, tablet, and desktop.
* **YouTube IFrame API:** Precision cueing to start and stop at specified timestamps.
* **Local State Persistence:** Uses browser `localStorage` for privacy-first, zero-login progress tracking.

---

## ⚠️ MANDATORY MEDICAL & CLINICAL PRACTICE DISCLAIMER

> [!CAUTION]
> ### 🛑 CRITICAL CLINICAL PRACTICE NOTICE — STRICTLY FOR EDUCATIONAL & TRAINING PURPOSES
> 
> 1. **No Medical Advice:** The **MedEd** platform, its curated modules, AI-guided summaries, surgical manuals, and clinical notes are intended **strictly for academic education and clinical revision** by certified medical practitioners, postgraduate residents, and healthcare trainees.
> 2. **Not a Substitute for Bedside Clinical Judgment:** This material does **NOT** constitute patient-specific medical advice, individualized diagnostic directives, or standardized operative mandates.
> 3. **Verification of Dosages & Protocols:** Clinical medicine and surgical techniques evolve rapidly. All pharmaceutical dosages, stimulation protocols, and surgical algorithms **must be independently verified** against official institutional formularies, manufacturer packaging, and up-to-date peer-reviewed clinical society guidelines (e.g. ACOG, RCOG, FOGSI, ESHRE, WHO, NICE).
> 4. **No Doctor-Patient Relationship:** Accessing or using this material creates no physician-patient or advisor-advisee relationship. The authors, contributors, and platform maintainers assume **no liability or responsibility** for individual clinical decisions, adverse events, or patient outcomes resulting from the use of this material.

---

## ⚖️ Intellectual Property & Licensing

* **Third-Party Content:** Original webinar recordings, video presentations, slides, and conference media belong to their respective medical societies (e.g. FOGSI, ICOG, ISAR), authors, and speakers. MedEd indexes publicly available academic videos with clear timestamps and attribution.
* **Open Source Platform Code:** All original platform architecture, HTML/JS/CSS source code, and original structured curriculum syntheses are licensed under the [MIT License](LICENSE).