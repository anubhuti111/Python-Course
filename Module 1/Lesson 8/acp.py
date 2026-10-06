print("=== GROCERY COST COMPARISON TOOL ===")

rice_price = 12 
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

# Then work out basket_cost_per_person:
#   add the three prices together, multiply by the number of baskets,
#   divide by the number of family members.

basket_cost_per_person = ((rice_price + milk_price + fruit_price) * number_of_baskets)//family_members

print("\nBasket_cost_per_person: ", basket_cost_per_person)

total_items = int(input("Enter the total number of items: "))
people = int(input("Enter number of people: "))

if people == 0:
    print("Cannot be shared in 0 person")
else:
    share=total_items%people
    if share==0:
        print("Can be shared equally in ", total_items//people, "parts")
    else:
        print("Cannot be shared equally. Remainder is: ", share)

recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

recorded = (recorded_average*total_weeks) - wrong_week_cost + correct_week_cost
new_recorded_avg = recorded//total_weeks

print("\nRecorded Average is: ", new_recorded_avg)

store_a_average = 70
store_b_average = 75
store_c_average = 80

if new_recorded_avg>store_a_average and new_recorded_avg>store_b_average and new_recorded_avg>store_c_average:
    verdict = "New Average is greater than all other stores"
elif new_recorded_avg>store_a_average and new_recorded_avg>store_b_average :
    verdict = "New Average is greater than a and b stores"
elif new_recorded_avg>store_b_average and new_recorded_avg>store_c_average :
    verdict = "New Average is greater than b and c stores"
elif new_recorded_avg>store_a_average and new_recorded_avg>store_c_average :
    verdict = "New Average is greater than a and c stores"
elif new_recorded_avg>store_a_average:
    verdict = "New Average is greater than store a only"
elif new_recorded_avg>store_b_average:
    verdict = "New Average is greater than store b only"
elif new_recorded_avg>store_c_average:
    verdict = "New Average is greater than store c only"
else:
    verdict = "Invalid values"

print(verdict)

print("\n\n=========SUMMARY=============\n")
print("Basket_cost_per_person: ", basket_cost_per_person)
print("Recorded Average is: ", new_recorded_avg)
print(verdict)