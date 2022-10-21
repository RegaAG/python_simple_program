import random
import string

amount = 3
committee = ['A', 'B', 'C', "D"]
Possibility_First = []
Possibility_Second = []
Possibility_Third = []

for i in range(amount):
    Possibility_First.append(random.choice(committee))
    Possibility_Second.append(random.choice(committee))
    Possibility_Third.append(random.choice(committee))

print("committee : A B C D")
print(f"Possibility First {Possibility_First}")
print(f"Possibility Second {Possibility_Second}")
print(f"Possibility Third {Possibility_Third}")