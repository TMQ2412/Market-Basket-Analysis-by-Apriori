import numpy as np
import pandas as pd
from apyori import apriori
import tkinter as tk


store_data = pd.read_csv("store_data.csv", header=None)
records = []
for i in range(1, 7501):
    records.append([str(store_data.values[i, j]) for j in range(0, 20)])

def generate_rules(min_support, min_confidence, min_lift):
    rules = apriori(records, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=2)
    rules = list(rules)
    return rules

root = tk.Tk()
root.title("Product Association Rule Explorer")

min_support_label = tk.Label(root, text="Nhập vào giá trị minimum support:")
min_support_entry = tk.Entry(root)
min_confidence_label = tk.Label(root, text="Nhập vào giá trị minimum confidence:")
min_confidence_entry = tk.Entry(root)
min_lift_label = tk.Label(root, text="Nhập vào giá trị minimum lift:")
min_lift_entry = tk.Entry(root)

min_support_label.grid(row=0, column=0)
min_support_entry.grid(row=0, column=1)
min_confidence_label.grid(row=1, column=0)
min_confidence_entry.grid(row=1, column=1)
min_lift_label.grid(row=2, column=0)
min_lift_entry.grid(row=2, column=1)

generate_rules_button = tk.Button(root, text="Phân tích", command=lambda: generate_and_display_rules())
generate_rules_button.grid(row=3, column=0)


rules_text = tk.Text(root)
rules_text.grid(row=4, columnspan=2)

def generate_and_display_rules():
    try:
        min_support = float(min_support_entry.get())
        min_confidence = float(min_confidence_entry.get())
        min_lift = float(min_lift_entry.get())
        rules = generate_rules(min_support, min_confidence, min_lift)
        rules_text.delete('1.0', tk.END)
        for rule in rules:
            items = [str(item) for item in rule[0]]
            rules_text.insert(tk.END, "Rule: " + items[0] + " -> " + items[1] + "\n")
            rules_text.insert(tk.END, "Support: " + str(rule[1]) + "\n")
            rules_text.insert(tk.END, "Confidence: " + str(rule[2][0][2]) + "\n")
            rules_text.insert(tk.END, "Lift: " + str(rule[2][0][3]) + "\n\n")
    except ValueError:
        rules_text.delete('1.0', tk.END)
        rules_text.insert(tk.END, "Không tìm thấy dữ liệu, vui lòng nhập vào dữ liệu.")

root.mainloop()