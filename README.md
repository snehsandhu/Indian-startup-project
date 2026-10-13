# 🚀 Indian Startup Funding Analysis

An interactive **Streamlit dashboard** that explores funding activity in the Indian startup ecosystem. Slice the data three ways: the ecosystem as a whole, a single startup, or a single investor.

Built with **Python, Pandas, Matplotlib and Streamlit**.

---

## ✨ Features

### 📊 Overall Analysis
- Headline metrics: **total funding**, **maximum single investment**, **average funding per startup**, and **number of funded startups**
- **Month-over-Month (MoM) trend** of funding, switchable between *total amount* and *number of deals*

### 🏢 Startup View
- Profile: **industry**, **sub-industry** and **location**
- Full funding history table (date, round, amount, investors)
- Metrics: total funding, number of funding rounds, largest funding, number of investors
- Charts: **funding journey over time** and **investment by funding round**
- Table of the **top investors** in that startup

### 💼 Investor View
- Most recent investments by the investor
- Biggest investments (bar chart)
- Distribution of investment by **city**, **sector** and **funding round** (pie charts)
- **Year-over-Year (YoY)** investment trend

---

## 🗂️ Project Structure

```
Indian-startup-project/
├── app.py                    # Streamlit dashboard
├── analysis.ipynb            # Data cleaning & exploratory analysis
├── startup_funding.csv       # Raw dataset
├── startup_cleaned_data.csv  # Cleaned dataset used by the app
└── README.md
```

---

## 📦 Dataset

The dashboard reads `startup_cleaned_data.csv`, produced from the raw `startup_funding.csv` in `analysis.ipynb`. The app relies on these columns:

| Column | Description |
| --- | --- |
| `date` | Date of the funding round |
| `startup` | Startup name |
| `Vertical` | Industry / sector |
| `subvertical` | Sub-industry |
| `city` | City of the startup |
| `investors` | Comma-separated list of investors |
| `round` | Funding round type (Seed, Series A, etc.) |
| `amount in usd` | Amount raised, in USD |

---

## ⚙️ Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/snehsandhu/Indian-startup-project.git
cd Indian-startup-project
```

**2. (Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install streamlit pandas matplotlib
```

**4. Run the app**

```bash
streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

> Run the command from the project folder so `app.py` can find `startup_cleaned_data.csv`.

---

## 🧭 How to Use

1. Use the **sidebar** to choose between **Overall Analysis**, **Startup** or **Investor**.
2. For *Startup* or *Investor*, pick a name from the dropdown.
3. Click **Find startup Details** / **Find Investor Details** to load the analysis.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** for data cleaning and aggregation
- **Matplotlib** for charts
- **Streamlit** for the web interface
- **Jupyter Notebook** for exploratory analysis

---

## 🔮 Future Improvements

- Add screenshots and a live deployment link (e.g. Streamlit Community Cloud)
- Add a `requirements.txt` for one-step setup
- Add city-wise and sector-wise analysis to the overall view
- Add investor similarity and startup comparison features
- Switch to interactive charts (Plotly)

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome. Feel free to open an issue or submit a pull request.

---

## 👤 Author

**Sneh Sandhu**
GitHub: [@snehsandhu](https://github.com/snehsandhu)
