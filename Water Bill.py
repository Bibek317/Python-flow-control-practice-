no_of_liter = int(input("How much water you have used ? :"))
fixed_charge = 150
total_cost = 0
if no_of_liter <= 1000:
    total_cost = (no_of_liter / 100) * 2
elif no_of_liter <= 2000:
    first_1000 = (1000 / 100) * 2
    remaining = (no_of_liter - 1000)/100 * 3
    total_cost = first_1000 + remaining
else:
    first_1000 = 10 * 2
    next_1000 = 10 * 3
    remaining = (no_of_liter - 2000) / 100 * 5
    total_cost = first_1000 + next_1000 + remaining
 
total_cost += fixed_charge

if total_cost >= 1000 :
    discount = total_cost * 0.10
    total_cost -= discount
    print(f"Your total discount is Rs.{discount:.2f}")

print(f"Sir your total bill is Rs.{total_cost:.2f}")