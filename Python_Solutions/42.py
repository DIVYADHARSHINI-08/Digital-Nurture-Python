import statistics

sales_data = []

try:
    with open("sales.txt", "r") as file:
        for line in file:
            try:
                value = float(line.strip())
                sales_data.append(value)

            except ValueError:
                print(f"Invalid data skipped: {line.strip()}")

    if len(sales_data) == 0:
        print("No valid sales data found.")

    else:
        mean_value = statistics.mean(sales_data)
        median_value = statistics.median(sales_data)
        print("----- Sales Statistics Summary -----")
        print(f"Total Records : {len(sales_data)}")
        print(f"Sales Data    : {sales_data}")
        print(f"Mean Sales    : {mean_value}")
        print(f"Median Sales  : {median_value}")

except FileNotFoundError:
    print("Error: sales.txt file not found.")

except Exception as e:
    print("An unexpected error occurred:", e)