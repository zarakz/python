# تابع زیر محاسبه میکند که شما ماهانه چه مبلغی از وام خود را پرداخت کرده اید
def month_pay(principal, annual_interest_rate, duration):
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    if not (r == 0):
        monthly_payment = (principal * (r * pow((1 + r), n))) / (pow((1 + r), n) - 1)
    else:
        monthly_payment = principal / n

    return monthly_payment


# محاسبه میزان باقی مانده وام
def remaining_lobalance(principal, annual_interest_rate, duration, number_of_payments):
    p = int(number_of_payments)
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    if not (r == 0):
        remaining_loan_balance = (principal * (pow((1 + r), n) - pow((1 + r), p))) / (pow((1 + r), n) - 1)
    else:
        remaining_loan_balance = principal - (principal * (p / n))
    return remaining_loan_balance


loan_amount = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (percent): "))
loan_duration_in_years = int(input("Enter loan duration in years: "))
month_payment = month_pay(loan_amount, interest_rate, loan_duration_in_years)
print("LOAN AMOUNT:", loan_amount, "INTEREST RATE (PERCENT):", int(interest_rate))
print("DURATION (YEARS):", loan_duration_in_years, "MONTHLY PAYMENT:", int(month_payment))
balance = month_payment * loan_duration_in_years * 12
print(balance)
year = 1
total_payment = 0
year_payment = month_payment * 12
while year <= loan_duration_in_years:
    t = year * 12
    total_payment = total_payment + year_payment
    balance = remaining_lobalance(loan_amount, interest_rate, loan_duration_in_years, t)
    print("YEAR:", year, "BALANCE:", int(balance), "TOTAL PAYMENT", int(total_payment))
    year = year + 1
