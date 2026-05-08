def calculate_daily_budget(total_budget, days):
    if days <= 0:
        raise ValueError("Days must be greater than zero.")

    return round(total_budget / days, 2)


def budget_category(daily_budget):
    if daily_budget < 50:
        return "Low Budget"
    elif daily_budget < 200:
        return "Moderate"
    else:
        return "Luxury"