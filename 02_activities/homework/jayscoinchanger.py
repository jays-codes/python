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