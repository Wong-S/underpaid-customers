MELON_COST = 1.00

# Create a Function that takes in a text file of customer orders and parses it to produce similar output
def customer_order_parsing(file):
    for line in file:
        line = line.rstrip()
        words = line.split("|")

        name = words[1]

        quanity = float(words[2])

        paid = float(words[3])

        customer_buy = quanity * MELON_COST
        if customer_buy != paid:
            # Python's ternary operator! VERY USEFUL
            payment_status = "underpaid" if customer_buy < paid else "overpaid"

            print(f"{name} has {payment_status} for their melons.")

            # print(f"{name} paid ${paid:.2f},", f"expected ${customer_buy:.2f}")

        else:
            print(f"{name} has paid the exact amount.")


customer_order_parsing(file=open("customer-orders.txt"))

