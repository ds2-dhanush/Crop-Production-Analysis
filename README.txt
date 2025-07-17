
# 🌾 India Crop Production Predictor – End‑to‑End ML Project

A Streamlit‑powered web app that predicts crop production (in **tonnes**) for any Indian district, crop, season and year.  
Built for planners, farmers, agritech analysts – and as a full‑stack machine‑learning portfolio piece.

---

## 📌 Table of Contents
1. Problem Statement
2. Dataset
3. Project Pipeline
4. How It Works
5. Why It’s Useful
6. Web App Usage
7. Model & Tech Stack
8. Real‑World Workflow Mapping
9. Future Work
10. Author

---

## Problem Statement
> *“Given historical agricultural records, estimate the crop production for a particular (`State`, `District`, `Crop`, `Season`, `Year`, `Area`).“*

Accurate forecasts help:
- 🏛 **Government** – allocate storage & subsidies  
- 🚚 **Supply‑chain planners** – schedule transport & logistics  
- 🚜 **Farmers** – gauge future earnings & optimise inputs  

---

## Dataset
| Column | Notes |
|--------|-------|
| **State, District** | Location identifiers |
| **Crop** | e.g. Rice, Wheat, Cotton |
| **Year** | Financial‑year string (“2001‑02”) → cleaned to 2001 |
| **Season** | Kharif, Rabi, etc. |
| **Area** | Cultivated land (hectares) |
| **Production** | Target (tonnes) |
| **Yield** | Production per area |

Raw size: **340 k+ rows** (2000‑2022).  
Unit columns were normalised – only **tonnes** kept for production; **Area.units** dropped (all “hectares”).

---

## Project Pipeline

```
data/           ← raw dataset
notebooks/      ← EDA & model
models/         ← saved model + encoders
app.py          ← Streamlit interface
```

1. **Cleaning** – removed NaNs, fixed Year, standardised units  
2. **EDA** – distribution plots, Area vs Production, state averages  
3. **Encoding** – Label‑encoding for categorical features  
4. **Model** – Random Forest (best: R² ≈ 0.97, RMSE ≈ 61 k t)  
5. **Deployment** – Streamlit app with CSV upload + manual form  

---

## How It Works
### Batch Mode
Upload CSV → encodes → predicts → download results

### Single Input
Select state/district/crop/season + area + year → instant prediction

---

## Why It’s Useful
- **Farmers**: plan earnings and resources  
- **Planners**: forecast surplus/deficit  
- **Startups**: integrate into advisory dashboards  

---

## Web App Usage
```bash
streamlit run app.py
```
Or visit: `https://crop‑predictor.streamlit.app`

---

## Model & Tech Stack
Random Forest Regressor, Sklearn LabelEncoders, Streamlit, Python 3.10

---

## Future Work
- Weather & soil API features  
- Map visualisations  
- Time‑series forecasting (Prophet/LSTM)

---

## Author
Dhanush R – [Portfolio](https://ds2-dhanush.github.io/My-Portfolio/)
