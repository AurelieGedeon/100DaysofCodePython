import random
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe', 'Stubbs']

number_of_names = len(names)

list_index = number_of_names - 1

random_number = random.randint(0, list_index)

bill_payer = names[random_number]
print(f"{bill_payer} is going to buy the meal today!")


fruits =["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)