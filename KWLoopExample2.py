# While Loop
i = 1
while i <= 5:
    print("Dharmendra", i)
    i += 1

j = 5
while j > 0:
    print("Jitendra", j)
    j -= 1

# For Loop
x = ['Dharmenra', 12,23.3]

for i in x:
    print(i)

for i in range(20, 30):
    print(i)

# break continue and pass
print("**** Break Keyword Example ****")
for i in range(1, 100):
    if i % 2 == 0 or i % 5 == 0:
        break
    else:
        print(i)

print("**** Continue Keyword Example ****")
for i in range(1, 100):
    if i % 2 == 0 or i % 5 == 0:
        continue
    else:
        print(i)

print("**** Pass Keyword Example ****")
for i in range(1, 100):
    if i % 2 == 0 or i % 5 == 0:
        pass
    else:
        print(i)