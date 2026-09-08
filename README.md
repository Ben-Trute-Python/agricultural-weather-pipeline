# Agricultural Climate-Matching Pipeline 🌍🌱

An automated, Python-based data pipeline that evaluates
regional climate suitability for custom perennial crop and
orchard configurations across Texas. By matching historical
winter weather metrics against specific crop tolerances, the
application provides a collective viability verdict for
multi-crop agricultural setups.

## 🎯 The Problem & Inspiration
The current commercial agricultural system relies heavily on
intensive monocrops grown in hyper-specific zones (e.g.,
cold-sensitive citrus in Southern Florida/Texas or
high-chill apples in northern regions). For diversified local
food systems and resilient agricultural ventures, financial
stability and resource efficiency rely heavily on strategic
 crop diversification. By prioritizing perennial crops,
operations can significantly reduce annual planting costs,
labor, and fuel expenditures associated with plowing and
field preparation.

To maximize land utility, growers must locate microclimates
where unique varieties overlap—such as pairing cold-hardy
heirloom citrus with low-chill southern heirloom apples.
Manually tracking down decades of daily temperature lows,
programmatically calculating chill hours, and cross-referencing
rainfall datasets across hundreds of potential regions via
web searches is incredibly time-consuming and creates a
massive, unmanageable data bottleneck.

This application was built to automate that multi-variable
research, aggregating thousands of historical climate data
points instantly into a clear regional suitability verdict.

## 🚀 Features
* **Dynamic Historical Weather Tracking:** Automatically
  calculates and queries exact historical winter blocks
  (e.g., Oct 1 - Apr 30) using the Open-Meteo Archive API.
* **Unified Crop Database:** Centralizes critical horticultural
  thresholds (minimum chill hours, hardiness zones, and
  rainfall requirements) for multi-crop configurations.
* **Custom Research Exceptions:** Features smart error-handling
  and custom logic exceptions (such as specialized low-chill
  apple cultivar thresholds).
* **Interactive Terminal Controller:** A clean, numbered
  CLI menu letting users test collective orchard
  combinations simultaneously.

## 🛠️ System Architecture
The application is modularly split into three core pipeline
phases:
1. `fetcher.py`: Manages network requests, endpoint
   switching, and raw JSON retrieval from the historical
   weather API archive.
2. `processor.py`: Parses hourly temperature and daily
   rain arrays to crunch total chill hours and peak
   rainfall metrics.
3. `app.py`: Acts as the central pipeline controller,
   managing user selection, database matching, exception
   notes, and regional synthesis reports.

## 🧰 Tech Stack
* **Language:** Python 3
* **Libraries:** `urllib.request`, `json`, `datetime`
* **API Source:** Open-Meteo Archive API

## 💻 How to Run
Ensure you have Python installed, then clone the repository
and execute the main controller:
```bash
python app.py

## 🤝 Contact & Contributing
If you are a recruiter, hiring manager, or developer looking to connect, feel free to reach out:
* **Email:** padre.island.python@gmail.com 
* **GitHub Profile:** https://github.com/Ben-Trute-Python

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
 
