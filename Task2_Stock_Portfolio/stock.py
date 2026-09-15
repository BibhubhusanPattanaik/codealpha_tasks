import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200,
    "MSFT": 400
}

total_investment = 0
portfolio = []

print("==============================")
print("     STOCK PORTFOLIO TRACKER")
print("==============================")

while True:

    stock_name = input(
        "\tEnter stock name (or 'done' to finish): "
    ).upper()


    if stock_name == "DONE":
        break


    if stock_name not in stock_prices:
        print("Stock not found. Please enter a valid stock.")
        continue


    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue


    price = stock_prices[stock_name]


    investment = price * quantity


    total_investment += investment


    portfolio.append([
        stock_name,
        quantity,
        price,
        investment
    ])

    print("Stock price:", price)
    print("Investment for", stock_name, ":", investment)


# Display summary
print("\n==============================")
print("       PORTFOLIO SUMMARY")
print("==============================")

for item in portfolio:
    print(
        item[0],
        "- Quantity:", item[1],
        "- Investment:", item[3]
    )

print("------------------------------")
print("Total investment:", total_investment)
print("==============================")



with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock",
        "Quantity",
        "Price",
        "Investment"
    ])

    for item in portfolio:
        writer.writerow(item)


print("\tPortfolio saved to portfolio.csv")