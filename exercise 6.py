#Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5

def checking(divisible_by_5_or_not):
    if divisible_by_5_or_not % 5 == 0:
        print(divisible_by_5_or_not, "is divisible by 5")

    
number_list = [10, 20, 33, 46, 55]
print(number_list)
for i in range(0,5):
    checking(number_list[i])
