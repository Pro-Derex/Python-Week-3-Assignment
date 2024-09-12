def calculate_final_price(price, discount_percent=0):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

original_price = 3000
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_final_price(original_price, discount_percent)
print(f"The final price after applying the discount is: ${final_price:.2f}")
