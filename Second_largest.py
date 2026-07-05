number=[45,69,7,98,2]
largest=number[0]
second_largest=number[0]

for i in number:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i != largest:
        second_largest=i
print("Largest=",largest)
print("Second Largest=",second_largest)


