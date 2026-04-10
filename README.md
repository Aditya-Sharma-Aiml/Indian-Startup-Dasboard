# 🏢 Startup Funding Analysis Dashboard

A comprehensive **Streamlit-based interactive dashboard** for analyzing Indian startup funding data with powerful insights into startups, investors, and market trends.

---

## 🌐 Live Demo

**✨ Access the Live Dashboard Here:**

### 👉 [https://indian-startup.streamlit.app/](https://indian-startup.streamlit.app/)

The dashboard is deployed and live on **Streamlit Cloud**. You can access it directly from your browser without any setup!

---

## 📋 Project Overview

This dashboard provides three powerful perspectives for understanding startup ecosystem dynamics:

1. **Overall Analysis** — Market-wide insights and trends
2. **Investor Analysis** — Portfolio details and investment patterns
3. **Startup Analysis** — Company-specific funding history and metrics

---

## 📁 Project Structure

```
startup_dashboard/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── startup_cleaned.csv         # Cleaned dataset (primary data source)
├── startup_funding.csv         # Raw dataset (backup)
├── needs.txt                   # Project planning & references
└── README.md                   # This file
```

---

## 🎯 Features Implemented

### 1️⃣ **Overall Analysis Dashboard**

Provides comprehensive market-level insights:

#### Key Metrics (KPI Cards)

- **Total Invested** — Sum of all funding amounts (Cr)
- **Max Startup Funding** — Highest single funding amount
- **Avg Funding/Startup** — Average funding per company
- **Funded Startups** — Total count of funded companies

#### Visualizations

- 📊 **Month-over-Month (MoM) Trends** — Track funding activity over time
  - Toggle between Total Amount and Deal Count
  - Interactive line chart with date labels
- 🏆 **Top Sectors Analysis**
  - Horizontal bar chart: Sector-wise funding amounts
  - Pie chart: Sector distribution by deal count
- 🌆 **City-wise Funding**
  - Bar chart showing funding distribution across major Indian cities
  - Top 10 cities highlighted
- 🚀 **Top 10 Startups**
  - Ranked by total funding received
  - Dataframe with startup names and amounts
- 💼 **Top 10 Investors**
  - Ranked by number of investments made
  - Shows portfolio diversity

---

### 2️⃣ **Investor Analysis**

Detailed portfolio analysis for individual investors:

#### Investor Selection

- Dropdown menu with all unique investors in dataset
- Clean, validated list with no empty values

#### Summary Metrics

- Total Investments (deal count)
- Total Amount Invested (Cr)
- Average Investment Size (Cr)
- Unique Startups Funded

#### Analysis Sections

**📅 Most Recent Investments**

- Table showing last 10 investments
- Columns: Date, Startup, Vertical, City, Round, Amount

**💎 Biggest Investments**

- Horizontal bar chart of top 10 largest investments
- Helps identify core portfolio companies

**🎯 Sectors Invested In**

- Pie chart showing sector distribution
- Percentage breakdown of investment focus areas

**📈 Year-over-Year (YoY) Trends**

- Line chart showing investment evolution over years
- Identifies growing vs. declining investment activity

**🔷 Investment by Round Type**

- Bar chart of funding round distribution
- Shows seed, series A, B, C, PE, etc. patterns

---

### 3️⃣ **Startup Analysis**

Comprehensive company-level information:

#### Startup Selection

- Dropdown with all startups in dataset
- Filtered to exclude empty/null entries

#### Summary Metrics

- Funding Rounds (total funding events)
- Total Funding (Cr)
- Latest Round (most recent funding type)
- Total Investors (count of unique investors)

#### Company Information

- **Industry** — Primary vertical (e.g., FinTech, E-commerce)
- **Sub-industry** — Specific business domain
- **Headquarters** — Company location
- **First Funding Date** — When company first received funding
- **Latest Funding Date** — Most recent investment round

#### Key Sections

**💵 Funding Timeline**

- Chronological table of all funding events
- Shows progression of rounds and investor participation

**📊 Cumulative Funding Over Time**

- Line chart showing total capital raised progressively
- Visualizes company's funding trajectory

**👥 All Associated Investors**

- Comprehensive list of every investor who funded the startup
- Shows entire investor ecosystem around company

**🤝 Similar Companies**

- Companies in same vertical as selected startup
- Top 10 similar companies ranked by funding
- Allows competitive analysis

---

## 📊 Data Analysis & Processing

### Data Source

**Indian Startup Funding Dataset** (from Kaggle)

### Data Features

```
- date: Funding announcement date
- startup: Company name
- vertical: Primary industry sector
- subvertical: Specific business domain
- city: Headquarters location
- investors: Comma-separated investor names
- round: Funding round type (Seed, Series A, PE, etc.)
- amount: Funding amount in Crores (Cr)
```

### Data Cleaning Process

1. **Removed Invalid Entries**
   - URLs used as startup names → Removed
   - Missing startup names → Filtered out
2. **Standardized Values**
   - Converted all text to lowercase for consistency
   - Normalized round type naming (Seed Round, Series A, etc.)
3. **Handled Missing Data**
   - Zero/null funding amounts → Filtered for analysis
   - Invalid dates → Coerced to proper datetime format
4. **Investor Parsing**
   - Split comma-separated investor strings
   - Trimmed whitespace from investor names
   - Created unique investor list

### Data Preparation for Visualization

1. **Time-based Aggregation**
   - Extracted year and month from dates
   - Grouped by time periods for trends
2. **Categorical Analysis**
   - Grouped by vertical (sector)
   - Grouped by city (location)
   - Grouped by round type (funding stage)
3. **Aggregation Metrics**
   - Sum: Total funding amounts
   - Count: Number of deals/investments
   - Mean: Average funding sizes
   - Unique: Investor/startup counts

---

## 🛠️ Technology Stack

### Frontend

- **Streamlit** (v1.28.1) — Web app framework
- **Python** (3.x) — Programming language

### Data Processing

- **Pandas** (v2.1.3) — Data manipulation & analysis
- **NumPy** (v1.24.3) — Numerical operations

### Visualization

- **Matplotlib** (v3.8.2) — Chart library
- **Seaborn** (v0.13.0) — Statistical visualizations

---

## 📦 Installation & Setup

### Option 1: Use Live Dashboard (Recommended) ⚡

**No installation required!** Simply visit:

### 🌐 [https://indian-startup.streamlit.app/](https://indian-startup.streamlit.app/)

The dashboard is deployed and live, ready to use immediately.

---

### Option 2: Run Locally

#### Prerequisites

- Python 3.7+
- pip package manager
- Git
- Virtual environment (optional but recommended)

#### Step 1: Clone Repository

```bash
git clone https://github.com/Aditya-Sharma-Aiml/Indian-Startup-Dasboard.git
cd Indian-Startup-Dasboard
```

#### Step 2: Create Virtual Environment (Optional)

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run Dashboard

```bash
streamlit run app.py
```

Dashboard will open at: `http://localhost:8501`

---

## 🚀 How to Use

### Navigation

1. **Sidebar Menu** — Select Analysis Type
   - Overall Analysis
   - Investor Analysis
   - Startup Analysis

2. **Overall Analysis**
   - View market metrics and trends
   - No selection required
   - Explore all data at once

3. **Investor Analysis**
   - Select investor from dropdown
   - Click "View Details" button
   - Explore investment portfolio

4. **Startup Analysis**
   - Select startup from dropdown
   - Click "View Details" button
   - View company-specific metrics

---

## 📈 Key Insights You Can Derive

### Market-Level

- Largest funding rounds and key players
- Dominant sectors and investment trends
- Geographic distribution of startup activity
- Seasonal patterns in investment activity

### Investor-Level

- Investment strategy and sector focus
- Portfolio concentration and diversification
- Investment growth over years
- Typical investment round preferences

### Company-Level

- Funding trajectory and capital raised
- Investor relationships and backing
- Industry position relative to peers
- Company growth stage indicators

---

## ⚙️ Features & Error Handling

### Robust Error Handling

✅ All charts wrapped in try-catch blocks
✅ Validates data before visualization
✅ Graceful error messages for missing data
✅ No crashes on empty datasets

### Data Validation

✅ Filters out null/NaN values
✅ Validates numeric fields before plotting
✅ Checks for positive amounts (removes zero funding)
✅ Cleans investor and startup names

### User Experience

✅ Empty data shows info messages instead of errors
✅ Loading with caching for better performance
✅ Responsive layout for different screen sizes
✅ Clear navigation and intuitive interface

---

## 🎨 UI/UX Design Elements

### Icons & Symbols (HTML Entities)

- &#128202; Chart (Overall Analysis)
- &#128176; Money (Investor)
- &#128640; Rocket (Startup)
- &#128188; Briefcase (Investors list)
- &#128197; Calendar (Recent investments)
- &#127919; Target (Sectors)
- &#128200; Chart Up (Trends)
- &#127970; Building (Dashboard title)

### Color Scheme

- **Primary Charts** — Blue (#1f77b4), Green (#2ca02c), Orange (#ff7f0e)
- **Emphasis** — Red (#d62728), Purple (#9467bd)
- **Footer** — Professional grey tones

### Layout

- Wide layout for better visualization
- Multi-column sections for side-by-side comparisons
- Dividers for clear section separation
- Professional footer with copyright

---

## � Dashboard Screenshots

### 🌐 Overall Analysis Section

Comprehensive market-wide insights and trends across the Indian startup ecosystem.

#### Key Metrics and Trends

<img src="DashboardScreenShots/Screenshot 2026-04-11 042400.png" alt="Overall Analysis - Main Dashboard" width="100%">

_Overall Analysis dashboard with KPI metrics and month-over-month trends_

#### Year-over-Year Investment Trends

<img src="DashboardScreenShots/Screenshot 2026-04-11 042159.png" alt="Year-over-Year Investment Trends" width="100%">

_Visualization of investment amounts declining over the years (2015-2018)_

#### Biggest Investments & Sectors

<img src="DashboardScreenShots/Screenshot 2026-04-11 042215.png" alt="Biggest Investments and Sectors" width="100%">

_Top startup investments and sector-wise distribution analysis_

#### City-wise Funding Distribution

<img src="DashboardScreenShots/Screenshot 2026-04-11 042408.png" alt="City-wise Funding" width="100%">

_Funding amount breakdown by major Indian cities (Bangalore, Gurgaon, Mumbai, etc.)_

#### Top Startups and Investors

<img src="DashboardScreenShots/Screenshot 2026-04-11 042416.png" alt="Top 10 Startups and Investors" width="100%">

_Ranked list of top 10 funded startups and most active investors_

#### Top Sectors Analysis

<img src="DashboardScreenShots/Screenshot 2026-04-11 042424.png" alt="Top Sectors by Funding" width="100%">

_Sector-wise funding amounts and distribution by number of deals_

#### Investment Round Type Distribution

<img src="DashboardScreenShots/Screenshot 2026-04-11 042731.png" alt="Investment Distribution by Round Type" width="100%">

_Comparison of investment amounts across different funding rounds (Private Equity, Seed Angel Funding)_

---

### 👤 Investor Analysis Section

Detailed portfolio analysis for individual investors with investment patterns and history.

#### Investor Portfolio Overview (Amazon Example)

<img src="DashboardScreenShots/Screenshot 2026-04-11 042147.png" alt="Investor Analysis - Amazon" width="100%">

_Amazon investor profile with total investments, amount invested, and recent investment history_

#### Additional Investor Analytics

<img src="DashboardScreenShots/Screenshot 2026-04-11 042223.png" alt="Investor Additional Metrics" width="100%">

_Detailed investor metrics and investment breakdown_

---

### 🚀 Startup Analysis Section

Comprehensive company-level information and funding history analysis.

#### Startup Profile (Unacademy Example)

<img src="DashboardScreenShots/Screenshot 2026-04-11 042234.png" alt="Startup Analysis - Unacademy" width="100%">

_Unacademy startup details with funding rounds, total funding, and company information_

#### Cumulative Funding Timeline

<img src="DashboardScreenShots/Screenshot 2026-04-11 042737.png" alt="Cumulative Funding Over Time" width="100%">

_Unacademy's cumulative funding growth trajectory from 2017 to 2019_

#### Similar Companies Analysis

<img src="DashboardScreenShots/Screenshot 2026-04-11 042745.png" alt="Similar Companies in Same Vertical" width="100%">

_Competitive analysis showing similar EdTech startups and their funding amounts_

---

## �📝 Plan of Action (Completed)

### Phase 1: Data Cleaning ✅

- Removed invalid entries
- Standardized field values
- Fixed formatting issues

### Phase 2: Data Analysis ✅

- Aggregated metrics
- Created utility functions
- Prepared data for visualization

### Phase 3: Streamlit Implementation ✅

- Overall Analysis section
- Investor POV implementation
- Startup/Company POV implementation
- General Analysis features
- Footer & branding

### Phase 4: Error Handling & Optimization ✅

- Added comprehensive error handling
- Optimized performance with caching
- Validated all inputs
- Created user-friendly messages

---

## 🔧 Utility Functions (Backend)

```python
get_startup_investors(startup_name)
# Returns: DataFrame of all funding rounds for a startup

get_investor_startups(investor_name)
# Returns: DataFrame of all investments by an investor

get_all_unique_investors()
# Returns: Sorted list of unique investor names

get_similar_startups(vertical_name)
# Returns: All startups in the same vertical/sector

get_similar_investors(investor_name, top_n=5)
# Returns: Top N investors with similar investment patterns
```

---

## 📖 Dataset Information

### Total Records

- Startups: 100+ unique companies
- Investors: 200+ unique investors
- Funding Rounds: 400+ investment events
- Time Period: 2019-2020

### Key Statistics

- Total Funding: ₹100,000+ Crores
- Average Deal Size: ₹200-400 Crores
- Top Sector: FinTech, E-commerce
- Top Cities: Bengaluru, Gurgaon, Mumbai, Delhi

---

## 🐛 Known Limitations

1. **Dataset Scope** — Limited to Indian startups (2019-2020)
2. **Founder Info** — Founder names not included in current dataset
3. **Company Details** — Limited to available columns in CSV
4. **Real-time Data** — Static dataset, not updated live

---

## 🚀 Future Enhancements

- [ ] Add founder information lookup
- [ ] Implement advanced filtering options
- [ ] Add export to PDF/Excel functionality
- [ ] Real-time data integration
- [ ] Machine learning predictions
- [ ] Investor recommendation system
- [ ] Company performance tracking
- [ ] Interactive network graphs

---

## 📞 Support & Documentation

### Streamlit Docs

https://docs.streamlit.io/

### Dataset Source

https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding

### Markdown Guide

https://www.markdownguide.org/

---

## � Important Links

- **🌐 Live Dashboard:** https://indian-startup.streamlit.app/
- **📚 GitHub Repository:** https://github.com/Aditya-Sharma-Aiml/Indian-Startup-Dasboard
- **📖 Streamlit Documentation:** https://docs.streamlit.io/
- **📊 Dataset Source:** https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding

---

## 📄 License & Credits

**Created by:** Aditya Sharma  
**Built with:** ❤️ Streamlit & Python  
**Data Source:** Indian Startup Funding Dataset (Kaggle)  
**Deployment:** Streamlit Cloud

© 2026 All rights reserved.

---

## 📝 Version History

**v1.0 (Current)**

- Initial release with 3 analysis perspectives
- Complete error handling implementation
- Professional UI/UX design
- Comprehensive documentation

---

> **Note:** This dashboard is designed for educational and analytical purposes. Data accuracy depends on dataset quality and completeness.
