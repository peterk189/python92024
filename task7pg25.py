fishprice = 4.50
pricechips = 2.80
vatrate = .09

portionschips = int(input("how many portion of chips? :"))

portionsfish = int(input("How many portions of fish? :"))

final_fish = fishprice * portionsfish
final_chips = pricechips * portionschips

final_amount = final_chips + final_fish

finalvat =  vatrate * final_amount

print("Order summary:")
print("Fish Portion:",portionsfish)
print("Chips Portions:",portionschips)
print("Total amount before vat", final_amount)

print("Vat", final_amount * vatrate)
print("final amount with vat", finalvat + final_amount)

