def coin_changer(amount):
    quarters = amount // 25
    dimes = (amount % 25) // 10
    nickels = (amount % 25) % 10 // 5
    pennies = (amount % 25) % 10 % 5
    return quarters, dimes, nickels, pennies

#print(coin_changer(20))#break a bill into coins    

grades = ['K', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(grades)
grades.reverse()
print(grades)

#reverse grades using slicing
grades = grades[::-1]
print(grades)

#reverse grades using reverse() method
grades.reverse()
print(grades)

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)