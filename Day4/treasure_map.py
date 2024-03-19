line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put your treasure?") 
split_coordinates = list(position)
print(split_coordinates)

x_coordinate = split_coordinates[0]
y_coordinate= split_coordinates[1]

if y_coordinate:
    y_int = ""
    if int(y_coordinate) > len(map):
        print(f"{y_coordinate} is not an available coordinate. Please choose another.")
    else:
        y_int = int(y_coordinate)
    print(f"your latitudinal coordinate is : {y_int}")   
    

if x_coordinate:
    x_int = ""
    if x_coordinate == "A":
        x_int = 1
    elif x_coordinate == "B":
        x_int = 2
    elif x_coordinate == "C":
        x_int = 3
    else:
        print(f"{x_coordinate} is not an available coordinate. Please choose another.")
    print(f"your longitudinal coordinate is: {x_int}")

x_index = x_int - 1
y_index = y_int -1

map[y_index][x_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")