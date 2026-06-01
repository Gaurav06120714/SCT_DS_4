# 🚗 SCT_DS_4 — US Traffic Accident Analysis

## Task Overview
Analyze US traffic accident data to identify patterns related to road conditions, weather, and time of day. Visualize accident hotspots and contributing factors.

## Dataset
**Source:** Kaggle — US Accidents (2016–2023)  
**File:** `US_Accidents_March23.csv`  
**Records:** ~7.7 million accident records across 49 US states  
**Features:** 46 columns including severity, location, weather, time, road features

## What the Script Does
- Loads the large dataset with low_memory mode
- **Data Cleaning:**
  - Drops rows missing critical fields (location, severity, weather, day/night)
  - Parses `Start_Time` to extract `Hour`, `Month`, and `DayOfWeek`
- **Visualizations (6-panel figure):**
  1. Accidents by Severity Level (bar chart)
  2. Accidents by Hour of Day (line chart with fill)
  3. Accidents by Day of Week (bar chart)
  4. Top 10 States by accident count (horizontal bar)
  5. Top 8 Weather Conditions during accidents (horizontal bar)
  6. Day vs Night accident split (pie chart)

## Key Findings
- Peak accident hours are **7–9 AM** and **4–6 PM** (rush hours)
- **California, Florida, and Texas** have the highest accident counts
- Most accidents occur in **Fair/Clear** weather (more traffic volume)
- **Friday** sees the highest weekly accident count
- Roughly **2/3 of accidents** happen during daytime

## Project Structure
```
SCT_DS_4/
├── US_Accidents_March23.csv         ← main dataset (~7.7M records)
├── SCT_DS_4.py                      ← main script
├── task04_accident_analysis.png     ← output visualization
└── README.md
```

## Libraries Used
| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, time parsing |
| `matplotlib` | All chart types |
| `seaborn` | Imported for styling consistency |

## How to Run
```bash
cd SCT_DS_4
python SCT_DS_4.py
```

> Note: The dataset is large (~1.5 GB). Loading may take 30–60 seconds depending on your machine.

## Output
A 6-panel figure saved as `task04_accident_analysis.png` revealing time, weather, and geographic patterns in US traffic accidents.

---
**Internship:** SkillCraft Technology — Data Science  
**Task:** 04 | Traffic Accident Data Analysis
