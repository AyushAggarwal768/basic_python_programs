#String iteration

for char in "Push-ups":
    print(char)
print("Push-ups done!")

#Average of numbers in a list

total=0
numbers=[10,20,30,40,50]
for num in numbers:
    total=total+num
avg=total/len(numbers)
print("the average of the given numbers is :",avg)

#Print all key-value pairs in the dictionary

capitals={"India":"New Delhi", "USA":"New York", "France":"Paris", "Japan":"Tokyo"}
for country,city in capitals.items():
    print("the country and its capital are {}.".format(country, city))
    

#print the keys of the dictionary

capitals={"India":"New Delhi", "USA":"New York", "France":"Paris", "Japan":"Tokyo"}
for k in capitals.keys():
    print("the capital of {} is {}.".format(k, capitals.get(k)))
    
    
#Else after for iteration

for x in range(1,5):
    print("This is iteration no {} in the 'for' loop.".format(x))
else:
    print("this is the else block in the loop.")
print("now, the loop ends.")


#Else with the while loop

x=0
while x<=5:
    x=x+1
    print("This is iteration no {} in the 'while' loop.".format(x+1))
else:
    print("this is the else block in the loop.")
print("now, the loop ends.")