num_all = 0
num_ji = 0
num_ou = 0
for i in range(1,101):
    num_all  += i
    if i % 2 == 0:
        num_ou += i
    else:
        num_ji += i
print(num_all)
print(num_ji)
print(num_ou)