needed_data =int(input("How much data needed for you per month in Gb:"))
monthly_budget = int(input("plz enter your budget:"))
roaming = input("Do you need international roaming?(Yes/No):")
if needed_data <= 5 and monthly_budget >= 300 and roaming == "No":
    print("Sir basic plan will be good for you")
elif needed_data <= 20 and monthly_budget >= 700 and roaming == "Yes" or "No":
    print("Sir standard plan will be good for you ")
elif needed_data > 20 and monthly_budget >= 1200 and roaming == "yes":
    print("Sir permium plan will be good for you")
else:
    print("Sorry sir no plan is matched for you . you have to increase your budget ")