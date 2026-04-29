<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1628,50:0d4a6e,100:0e7490&height=200&section=header&text=Startup%20Funding%20Dashboard&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Indian%20Startup%20Ecosystem%20%7C%20Powered%20by%20Streamlit&descAlignY=58&descSize=18&descColor=7dd3fc"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=650&lines=Explore+Indian+Startup+Funding+Trends.;Analyze+Investor+Portfolios+at+a+Glance.;Uncover+Market+Insights+Interactively.;Live+on+Streamlit+Cloud+%E2%80%94+No+Setup+Needed.)](https://git.io/typing-svg)

<br/>

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-Open%20Dashboard-0ea5e9?style=for-the-badge&labelColor=0a1628)](https://indian-startup.streamlit.app/)
&nbsp;
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

<br/>

<img src="https://img.shields.io/badge/Dataset-Indian%20Startups-0ea5e9?style=flat-square"/>
&nbsp;
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3D4DB7?style=flat-square&logo=plotly&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/Matplotlib-Visualizations-11557C?style=flat-square"/>
&nbsp;
<img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square"/>

<br/><br/>

> 🏢 A comprehensive **Streamlit-based interactive dashboard** for analyzing Indian startup funding data
> with powerful insights into startups, investors, and market trends.

<br/>

[🌐 **Live Demo**](https://indian-startup.streamlit.app/) 

</div>

---

## 🌐 Live Demo

<div align="center">

### ✨ Access the Live Dashboard Here:

### 👉 [https://indian-startup.streamlit.app/](https://indian-startup.streamlit.app/)

The dashboard is deployed and live on **Streamlit Cloud**.
You can access it directly from your browser without any setup!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indian-startup.streamlit.app/)

</div>

---

## 📋 Project Overview

This dashboard provides **three powerful perspectives** for understanding startup ecosystem dynamics:

<div align="center">

| # | View | What You'll Find |
|:---:|---|---|
| 1️⃣ | **Overall Analysis** | Market-wide insights and trends |
| 2️⃣ | **Investor Analysis** | Portfolio details and investment patterns |
| 3️⃣ | **Startup Analysis** | Company-specific funding history and metrics |

</div>

---

## 📁 Project Structure

```
startup_dashboard/
│
├── 📄 app.py                    # Main Streamlit application
├── 📦 requirements.txt          # Python dependencies
├── 🗂️  startup_cleaned.csv      # Cleaned dataset (primary data source)
├── 🗂️  startup_funding.csv      # Raw dataset (backup)
├── 📝 needs.txt                 # Project planning & references
└── 📖 README.md                 # This file
```

---

## 📸 Dashboard Screenshots

### 🔹 Overall Dashboard

<p align="center">
<img src="DashboardScreenShots/overall1.png" width="30%" />
<img src="DashboardScreenShots/overall2.png" width="30%" />
<img src="DashboardScreenShots/overall3.png" width="30%" />
</p>

### 🔹 Investor Analysis

<p align="center">
<img src="DashboardScreenShots/investor1.png" width="30%" />
<img src="DashboardScreenShots/investor2.png" width="30%" />
<img src="DashboardScreenShots/investor3.png" width="30%" />
</p>

### 🔹 Startup Analysis

<p align="center">
<img src="DashboardScreenShots/startup1.png" width="30%" />
<img src="DashboardScreenShots/startup2.png" width="30%" />
<img src="DashboardScreenShots/startup3.png" width="30%" />
</p>

---

## ✨ Key Features

<table>
<tr>
<td valign="top" width="50%">

### 📊 &nbsp;Overall Analysis
> *The big picture of Indian startup funding*

- 📈 Month-over-month funding trends
- 🏙️ Top funded cities & sectors
- 💰 Funding type distribution (Seed, Series A/B/C...)
- 🔥 Heatmaps & time-series visualizations

</td>
<td valign="top" width="50%">

### 👤 &nbsp;Investor Analysis
> *Deep-dive into any investor's portfolio*

- 🔍 Search any investor by name
- 📋 Full investment portfolio view
- 🏭 Sector & stage preferences
- 🤝 Co-investor network insights

</td>
</tr>
<tr>
<td valign="top" width="50%">

### 🚀 &nbsp;Startup Analysis
> *Detailed profile for every startup*

- 📜 Complete funding round history
- 💵 Total funds raised breakdown
- 👥 Investor list per company
- 📅 Timeline of funding milestones

</td>
<td valign="top" width="50%">

### ⚡ &nbsp;Built for Exploration
> *Intuitive, fast, and interactive*

- 🎛️ Sidebar filters for instant drill-down
- 📱 Responsive layout for all screen sizes
- 🌐 Zero setup — runs live in your browser
- 📤 Exportable charts and data tables

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| | Technology | Purpose |
|:---:|---|---|
| 🖥️ | **Streamlit** | Web app framework & deployment |
| 🐼 | **Pandas** | Data wrangling & analysis |
| 📊 | **Plotly** | Interactive charts & graphs |
| 📉 | **Matplotlib / Seaborn** | Static visualizations |
| ☁️ | **Streamlit Cloud** | Free hosting & deployment |

</div>

---

## ⚙️ Run Locally

**① Clone the repository**
```bash
git clone https://github.com/your-username/startup-dashboard.git
cd startup-dashboard
```

**② Install dependencies**
```bash
pip install -r requirements.txt
```

**③ Launch the app**
```bash
streamlit run app.py
# ✅ App opens at http://localhost:8501
```

---

## 📊 Dataset

The dashboard is powered by `startup_cleaned.csv` — a cleaned and preprocessed version of Indian startup funding records.

| Column | Description |
|---|---|
| `startup_name` | Name of the startup |
| `industry_vertical` | Sector / Industry |
| `city` | Headquarter city |
| `investors_name` | Names of investors |
| `investment_type` | Seed / Series A / B / C etc. |
| `amount_in_usd` | Funding amount in USD |
| `date` | Date of funding round |

---

---

<div align="center">

## ⭐ Found it useful? Give it a star!

*"Data is the new oil — but only if you can refine it."*

<br/>

[![Open Dashboard](https://img.shields.io/badge/🚀%20Open%20Live%20Dashboard-0ea5e9?style=for-the-badge)](https://indian-startup.streamlit.app/)

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1628,50:0d4a6e,100:0e7490&height=100&section=footer"/>

</div>
