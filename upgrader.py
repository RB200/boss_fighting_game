levels = [0]
money = 1000
def upgrade(level):
    global money
    if money - cost_to_upgrade(levels[level-1]) >= 0: 
        levels[level-1] += 1
        money -= cost_to_upgrade(levels[level-1]) 
        print(money)     
    else:
        print("Not enough money")

def cost_to_upgrade(level):
    return level * 1.25

while True:
    response = input("upgrade? :")
    if response == "1":
        upgrade(int(response))
