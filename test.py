#백준 5543
def smaller(a,b):
    if a > b:
        return b
    else:
        return a
burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
drink1 = int(input())
drink2 = int(input())

cheap_burger = 0
cheap_drink = 0

cheap_burger = smaller(burger1,burger2)
cheap_burger = smaller(cheap_burger,burger3)
cheap_drink = smaller(drink1,drink2)

print(cheap_burger+cheap_drink - 50)

burger = []
drink = []
for i in range(3):
    b = int(input())
    burger.append(b)

for i in range(2):
    d = int(input())
    drink.append(d)

burger.sort()
drink.sort()
print(burger[0]+drink[0]-50)
