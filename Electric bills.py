consumed_unit = int(input("Enter your conusmed unit:"))
fixed_charge = 100
total_cost = 0
if consumed_unit <= 100:
    total_cost = consumed_unit * 5
elif consumed_unit <= 200:
   first_100 = 100 *5
   remaining = (consumed_unit - 100) * 7
   total_cost = first_100 + remaining 
else:
    first_100 = 100 * 5
    next_100 = 100 * 7
    remaining = (consumed_unit - 200) * 10
    total_cost =first_100 + next_100 + remaining
    
total_cost += fixed_charge
if total_cost > 2000:
    discount = total_cost * 0.05
    total_cost -= discount
    print(f"Your discount is Rs.{discount}")
    
  
print(f"Your total bill is Rs.{total_cost}")
