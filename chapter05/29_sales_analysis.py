def main():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ]
    sales = [
        12_000, 14_500, 13_200, 15_000, 20_000, 18_500, 16_000, 15_500, 14_000, 19_000, 22_500, 24_000
    ]

    monthly_sales = dict(zip(months, sales))
    print(monthly_sales)

    for month, value in monthly_sales.items():
        print(f"{month:<9}: {value:>6} euros")

    print("-----------------------------")

    high_monthly_sales = {month: value for month, value in monthly_sales.items() if value >= 15000}
    for month, value in high_monthly_sales.items():
        print(f"{month:<9}: {value:>6} euros")

    print("-----------------------------")

    #discount
    discounted_sales = {
        month:value * 0.9 if value > 20000 else value
        for month, value in monthly_sales.items()
    }
    for month, value in discounted_sales.items():
        print(f"{month:<9}: {value:>6} euros")

    #total sales
    total_sales = sum(monthly_sales.values())
    print(f"total sales: {total_sales}")
    #best month
    #best_month = max(monthly_sales, key=monthly_sales.get)
    #print(f"Best month: {best_month} with sales: {monthly_sales[best_month]}")

    #worst month
    #worst_month = min(monthly_sales, key=monthly_sales.get)
    #print(f"Worst month: {worst_month} with sales: {monthly_sales[worst_month]}")

if __name__ == "__main__":
    main()