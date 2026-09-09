# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}

def get_portfolio():
    portfolio = {}
    print("Enter stock name and quantity (type 'done' to finish)")

    while True:
        stock = input("Stock name: ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"'{stock}' not found in price list. Available stocks: {list(stock_prices.keys())}")
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio

def calculate_total(portfolio):
    total = 0
    breakdown = []
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        breakdown.append((stock, qty, price, value))
    return total, breakdown

def save_to_file(breakdown, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("-" * 40 + "\n")
        for stock, qty, price, value in breakdown:
            f.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"\nPortfolio saved to {filename}")

def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total, breakdown = calculate_total(portfolio)

    print("\n--- Portfolio Summary ---")
    for stock, qty, price, value in breakdown:
        print(f"{stock}: {qty} shares x ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total}")

    save_choice = input("\nSave results to a file? (y/n): ").lower()
    if save_choice == "y":
        save_to_file(breakdown, total)

if __name__ == "__main__":
    main()