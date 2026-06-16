# MacroPulse Colombia: Predictive Analytics & Corporate Credit Risk Engine

## 📊 Project Overview
**MacroPulse Colombia** is an autonomous, data-driven financial software designed to assess corporate credit risk and investment vulnerabilities within Colombian listed corporations (*BVC*). 

By dynamically bridging macroeconomic indicators fetched from the Central Bank (*Banco de la República*) with standard corporate financial statements under IFRS/NIIF regulations, the system calculates leverage metrics and executes stress-testing simulations against macroeconomic shocks (e.g., interest rate hikes and local currency devaluation).

---

## 🛠️ Tech Stack & Architecture
This platform is architected into a modular, production-ready pipeline:
*   **Data Ingestion & Scraping:** `requests`, `BeautifulSoup4`, and Open Data APIs (`datos.gov.co`) for automated macroeconomic extraction.
*   **Database Management System:** Relational storage engine built with `SQLite` and orchestrated via `SQLAlchemy` for transactional integrity.
*   **Analytics Engine:** Quantitative modeling utilizing `Pandas` and `Numpy` for financial ratio calculation and macroeconomic sensitivity stress-testing.
*   **Interactive Interface:** Web application UI deployed using `Streamlit` combined with dynamic visualization frameworks via `Plotly Express`.

---

## ⚙️ Financial & Econometric Logic
The software ingests standard quarterly corporate income statements and balance sheets to compute institution-grade risk metrics:
1.  **EBITDA Margin:** $\frac{\text{EBITDA}}{\text{Total Revenue}} \times 100$ (Assesses core operational profitability).
2.  **Leverage Ratio (Debt-to-EBITDA):** $\frac{\text{Total Debt}}{\text{EBITDA}}$ (Measures debt service capabilities).
3.  **Macroeconomic Stress Model:** Simulates a monetary policy tightening shock ($\Delta R_{bancaria}$). The engine evaluates the marginal cost increase of corporate debt based on historical leverage tiers, yielding a projected contraction in corporate margins and dynamically flags the asset's risk exposure into three regulatory tiers: **LOW (Healthy)**, **MEDIUM (Monitoring)**, or **HIGH (Vulnerable)**.

---

## 🚀 How to Run the Environment

### 1. Clone the repository and install dependencies:
```bash
git clone https://github.com
cd macropulse-colombia
pip install pandas numpy requests beautifulsoup4 sqlalchemy streamlit plotly
```

### 2. Initialize the Database and Ingest Macro Data:
```bash
python macro_fetcher.py
```

### 3. Ingest Corporate Financial Records:
```bash
python corporate_scraper.py
```

### 4. Launch the Interactive Analytical UI:
```bash
streamlit run app.py
```

---

## 📈 Portfolio Objectives
Developed by an **Economist & Quantitative Financial Analyst**, this software serves as a empirical demonstration of technical capabilities in financial engineering, database relational modeling, and macroeconomic risk assessment, bypassing the need for premium terminals (e.g., Bloomberg) through open-source innovation.
