from datetime import datetime, timedelta
import calendar


def subtract_months(current_date, months):
    # Subtract the specified number of months
    one_month_ago = current_date.replace(day=1) - timedelta(days=1)
    for _ in range(months - 1):
        one_month_ago = one_month_ago.replace(day=1) - timedelta(days=1)

    # Set the day to the last day of the month if necessary
    _, last_day_of_previous_month = calendar.monthrange(
        one_month_ago.year, one_month_ago.month
    )
    one_month_ago = one_month_ago.replace(day=last_day_of_previous_month)

    return one_month_ago
