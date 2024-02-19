from dateutil.relativedelta import relativedelta


def end_of_month(date):
    return date + relativedelta(day=31)
