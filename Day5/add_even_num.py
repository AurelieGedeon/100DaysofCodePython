target = 4
total = 0

for even_number in range(0, target+1):
    if (even_number % 2) == 0:
        total += even_number

print(total)

# or

# even_total = 0
# for number in range(2, target + 1, 2):
#     even_total += number
# print(even_total)