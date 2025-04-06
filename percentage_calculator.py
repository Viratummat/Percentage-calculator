product_1 = float(input("What is your number:\n"))
product_2 = float(input("How much percentage you want to find:\n"))
# It is my answer which I got by using my probability formula
percentage_ans = round(product_1 * product_2 / 100 ,2)
print(f"{product_2}% of {product_1} is {percentage_ans}.")