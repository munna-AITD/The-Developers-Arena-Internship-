def category_summary(expenses):
    summary = {}

    for exp in expenses:
        cat = exp['Category']
        amt = float(exp['Amount'])
        summary[cat] = summary.get(cat, 0) + amt

    print("\n📊 Category-wise Summary")
    for k, v in summary.items():
        print(f"{k}: ₹{v:.2f}")


def monthly_report(expenses, month):
    total = 0
    count = 0

    for exp in expenses:
        if exp['Date'].startswith(month):
            total += float(exp['Amount'])
            count += 1

    if count == 0:
        print("No expenses found")
        return

    avg = total / count
    print(f"\n📅 Monthly Report ({month})")
    print(f"Total: ₹{total:.2f}")
    print(f"Average: ₹{avg:.2f}")
