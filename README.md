# PortfolioLab

A web-based portfolio simulator for finance students and beginner investors.
Built with real market data from Yahoo Finance.

🔗 **[Live Demo](https://portfoilo-lab-cbku.vercel.app/)**

---

## What it does

Most retail tools are either too simple (basic returns only) or too complex (Bloomberg-level).
PortfolioLab fills the gap — clean, educational, and quantitatively rigorous.

- **Portfolio Builder** — Add any stock or ETF by ticker, adjust weights with sliders, real-time validation
- **Performance Metrics** — Annualized return, volatility, Sharpe ratio, max drawdown vs S&P 500
- **Efficient Frontier** — Monte Carlo simulation of 1,000 portfolios, one-click optimal rebalancing
- **Correlation Heatmap** — Pairwise Pearson correlation matrix to visualize diversification quality

## How it works
```
Browser → Vercel Serverless Function → Yahoo Finance (yfinance)
```

All market data is fetched live from Yahoo Finance via a Python serverless function on Vercel.
Portfolio calculations (returns, covariance matrix, Monte Carlo) run client-side in the browser.

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | HTML / CSS / JavaScript |
| Charts | Chart.js |
| Market data | Yahoo Finance (yfinance) |
| Backend | Python (Vercel Serverless Functions) |
| Deployment | Vercel |

## Quantitative methods

| Metric | Method |
|---|---|
| Expected return | Weighted average of individual asset mean returns |
| Portfolio volatility | √(wᵀ Σ w), Σ = covariance matrix |
| Sharpe ratio | (E[Rp] − Rf) / σp, Rf = 5% |
| Efficient frontier | Monte Carlo: 1,000 random weight vectors |
| Correlation | Pearson correlation of log daily returns |
| Max drawdown | Max peak-to-trough decline over backtest period |

## Default portfolio

AAPL · MSFT · NVDA · SPY · QQQ · SCHD · JEPI · BND

## Roadmap

- [ ] Factor exposure analysis (value, momentum, quality)
- [ ] Dividend yield and income projection
- [ ] Backtesting with custom rebalancing schedules
- [ ] Export to PDF / CSV
- [ ] User accounts and saved portfolios

---

*Built by Johnathan Park · 2026*
