# Stock Portfolio Tracker

A simple command-line Python application that calculates the total value of a user-defined stock portfolio using manually configured stock prices.

Built as part of **CodeAlpha Python Programming Internship — Task 2**.

---

##  Features

-  Interactive CLI for entering stock names and quantities
-  Calculates per-stock and total investment value
-  Uses a hardcoded dictionary to simulate stock price data
-  Optional export of results to a `.txt` file
-  Input validation for unknown stocks and invalid quantities

---

##  Key Concepts Used

| Concept              | Usage in Project                                   |
|-----------------------|----------------------------------------------------|
| Dictionaries          | Storing stock prices and portfolio holdings         |
| Input / Output        | Collecting user input, printing results             |
| Basic Arithmetic       | Calculating per-stock value and total investment     |
| File Handling (I/O)   | Saving the portfolio summary to a `.txt` file        |

---

##  Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
```bash
git clone <your-repo-url>
cd stock-portfolio-tracker
```

No external dependencies are required — the project uses only Python's standard library.

### Running the Program
```bash
python stock_tracker.py
```

---

##  Usage

1. Run the script.
2. Enter a stock symbol (e.g., `AAPL`, `TSLA`) when prompted.
3. Enter the quantity of shares you hold.
4. Type `done` when you've finished entering stocks.
5. View your portfolio summary and total investment value.
6. Choose whether to save the results to a `.txt` file.

### Example Session
```
=== Stock Portfolio Tracker ===

Enter stock name and quantity (type 'done' to finish)
Stock name: AAPL
Quantity of AAPL: 10
Stock name: TSLA
Quantity of TSLA: 5
Stock name: done

--- Portfolio Summary ---
AAPL: 10 shares x $180 = $1800
TSLA: 5 shares x $250 = $1250

Total Investment Value: $3050

Save results to a file? (y/n): y

Portfolio saved to portfolio.txt
```

---

##  Supported Stocks

Stock prices are hardcoded for demonstration purposes:

| Symbol | Price ($) |
|--------|-----------|
| AAPL   | 180       |
| TSLA   | 250       |
| GOOGL  | 140       |
| AMZN   | 145       |
| MSFT   | 330       |

>  To add more stocks, simply extend the `stock_prices` dictionary in the source code.

---

##  Project Structure

```
stock-portfolio-tracker/
├── stock_tracker.py     # Main application script
├── portfolio.txt        # Generated output file (created after running)
├── .gitignore
└── README.md            # Project documentation
```

---

##  Possible Enhancements

- [ ] Support `.csv` export in addition to `.txt`
- [ ] Fetch live stock prices via an API (e.g., Alpha Vantage, Yahoo Finance)
- [ ] Add a GUI using Tkinter or a web interface with Flask
- [ ] Persist portfolio data across sessions using JSON

---

##  License

This project is created for educational purposes as part of the CodeAlpha internship program.

---

##  Acknowledgements

Developed as part of **CodeAlpha's Python Programming Internship — Module 1, Task 2**.