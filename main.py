def calculate_discount(price, discount_percent):
   
    price = float(price)
    discount_percent = float(discount_percent)
    
    
    if discount_percent >= 20:
        discounted = price * (discount_percent / 100)
    else:
        discounted = 0

    # Calculate the final price
    final_price = price - discounted

    return final_price

price = input("Enter the price of the product: ")
discount_percent = input("Enter the discount percentage: ")

final_price = calculate_discount(price, discount_percent)


print("The final price after applying the discount is: $" + str(final_price))

