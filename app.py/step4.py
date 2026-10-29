def calculate_mortgage(price, downpayment, rate=9, years=19):
    loan_amount= price - downpayment
    monthly_rate= (rate / 100) / 12
    total_months= years * 12

    monthly_payment= loan_amount * (monthly_rate * (1 + monthly_rate)**total_months)/((1 + monthly_rate)**total_months - 1)
    return monthly_payment

apartment_price_1= calculate_mortgage(20000000, 5000000)
apartment_price_2= calculate_mortgage(25000000, 7000000)

print(f'Ежемесячный платеж за квартиру стоимостью 20,000,000 тенге с первоначальным взносом 5,000,000 тенге составляет: {apartment_price_1:.2f} тенге')
print(f'Ежемесячный платеж за квартиру стоимостью 25,000,000 тенге с первоначальным взносом 7,000,000 тенге составляет: {apartment_price_2:.2f} тенге')