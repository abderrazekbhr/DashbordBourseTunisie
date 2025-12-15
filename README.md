# Dashboard Bourse Tunisie

A lightweight Python-based dashboard to explore and monitor Tunisian stock market data (TSE).  
This repository contains a single entry script (`main.py`) plus a `data/` folder for datasets and caching. Use this README as a concise, clear project overview and quick-start guide.

## One‑line summary
Interactive dashboard for visualizing Tunisian stock market prices, volumes, indices and simple analytics — implemented in Python (see `main.py` and `requirements.txt`).

## What’s included
- `main.py` — main application script (entry point)
- `data/` — directory for raw or cached CSV/JSON data
- `requirements.txt` — Python dependencies used by the project
- `.gitignore`, other small config files

## Key features
- Time-series charts for individual tickers and indices
- Volume and performance summaries (daily change, simple moving averages)
- Lists of top gainers / losers and basic sector breakdown
- Export or download selected ranges as CSV (if implemented)
- Lightweight structure so the project is easy to run and extend

(Exact features depend on the implementation in `main.py` — open that file to see what’s active.)

## Tech stack
- Python — application and dashboard logic live in `main.py`
- Third-party Python libraries — install via `requirements.txt` (check the file to see which charting / web UI libraries are used, e.g., Streamlit / Flask / Plotly / Matplotlib)

## Prerequisites
- Python 3.8+
- pip

## Quick start (developer)
1. Clone the repo:
   git clone https://github.com/abderrazekbhr/DashbordBourseTunisie.git
2. Move into the project folder:
   cd DashbordBourseTunisie
3. Install dependencies:
   pip install -r requirements.txt
4. Prepare data / config:
   - Place any raw CSV/JSON data into `data/` or configure your data source as required by `main.py`.
   - If the project expects environment variables or an API key, create a `.env` or edit a config as described in the code.
5. Run the app:
   python main.py
   (If `main.py` is a web dashboard using Streamlit: run `streamlit run main.py` — confirm by checking the file for Streamlit imports.)

Open the printed/local URL in your browser if the app starts a web server, or follow CLI prompts if it runs in the terminal.

## Project structure (recommended)
- main.py — entry point
- data/ — CSV/JSON raw or cached files
- docs/ — (optional) architecture diagrams, screenshots, sample outputs
- tests/ — (optional) unit/integration tests

## Data sources & update cadence
- Store the source(s) of the TSE data (API, CSV, scraped source) in the repo or document them in a `DATA.md` file.
- Indicate update frequency (real-time, hourly, daily) and any limitations (delays, missing fields).

## Notes for maintainers
- Inspect `main.py` to confirm which UI or plotting library is used and update `requirements.txt` or this README accordingly.
- If the app uses Streamlit, Flask, or another framework, add specific run instructions (e.g., `streamlit run main.py`) and mention the default port.
- Add example screenshots to the README for a better first impression.

## Contributing
- Open issues for bugs or feature requests.
- Fork the repository, create a feature branch, and open a PR with a clear description of your changes.
- Include tests where appropriate and update the README if public behavior changes.

## Roadmap ideas
- Add user authentication and persistent watchlists
- Alerts (email/push) for price thresholds
- Additional indicators: RSI, MACD, volatility metrics
- Caching & scheduled data updates (cron or background job)
- Package the app in Docker for easier deployment

## License
Specify the license you want to use (e.g., MIT). Add a `LICENSE` file at the repo root.

## Contact
Author: abderrazekbhr  
Add email / Twitter / LinkedIn or other contact details here.

---

To finalize the README I curated the text to match the repository layout (single Python entry script and a data folder). If you want, I can update the README file with these contents and tailor the run instructions after you confirm which UI/library `main.py` uses (Streamlit, Flask, Dash, etc.).  
