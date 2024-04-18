import tkinter as tk
from datetime import datetime

def calculate_total():
    total = 0
    for i in range(len(items)):
        try:
            price = float(prices[i].get())
            tax = float(taxes[i].get())
            subtotal = price + (price * tax / 100)
            total += subtotal
            # Append transaction details to daily report
            daily_report.append((items[i].get(), price, tax, subtotal))
        except ValueError:
            pass  # Handle invalid input
    total_label.config(text="Total: ${:.2f}".format(total))

    # Generate and display separate bill
    generate_bill()

def generate_bill():
    bill_window = tk.Toplevel(root)
    bill_window.title("Generated Bill")

    bill_text = "Item\tPrice ($)\tTax (%)\tSubtotal\n"
    for item, price, tax, subtotal in daily_report:
        bill_text += f"{item}\t{price}\t{tax}\t{subtotal}\n"
    bill_text += f"Total: ${total_label.cget('text').split(': $')[1]}"

    bill_label = tk.Label(bill_window, text=bill_text, justify='left')
    bill_label.pack(padx=10, pady=10)

# Initialize daily report list
daily_report = []

root = tk.Tk()
root.title("Billing Module")

# Labels
labels = ["Sr. No", "Item", "Item Code", "Price ($)", "Taxes (%)"]
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=0, column=i, padx=5, pady=5)

# Entry widgets
sr_no = []
items = []
item_codes = []
prices = []
taxes = []
for i in range(5):
    sr_no_entry = tk.Entry(root)
    sr_no_entry.grid(row=i+1, column=0, padx=5, pady=5)
    sr_no.append(sr_no_entry)
    
    item_entry = tk.Entry(root)
    item_entry.grid(row=i+1, column=1, padx=5, pady=5)
    items.append(item_entry)

    item_code_entry = tk.Entry(root)
    item_code_entry.grid(row=i+1, column=2, padx=5, pady=5)
    item_codes.append(item_code_entry)

    price_entry = tk.Entry(root)
    price_entry.grid(row=i+1, column=3, padx=5, pady=5)
    prices.append(price_entry)

    tax_entry = tk.Entry(root)
    tax_entry.grid(row=i+1, column=4, padx=5, pady=5)
    taxes.append(tax_entry)

# Button to calculate total
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=6, columnspan=5, pady=10)

# Label to display total
total_label = tk.Label(root, text="Total: $0.00")
total_label.grid(row=7, columnspan=5)

root.mainloop()
