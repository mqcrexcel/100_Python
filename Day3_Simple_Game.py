print(''',------------------------------------------.
`-----------------------------------------. |
,-----. ,-----.  ,----. ,-.  ,-.,------.  | | ,-. ,-. ,----. ,-----.  ,----.
`----. |`----. |`----. |`--` | |`------'  `-' `-' | |'----. |`----. |'------`
,-.  | |,----' |,-.  | |,---.| |,------.  ,-. ,-. | |,----' |,----' |.-----.
| |  | || ,-. < | |  | || |\ ` || ,----'  | | | | | || ,--. || ,-. <  `---. |
| `--' || |  | || `--' || | \  || `----.  | `-' `-' || |  | || |  | |.----' |
`-----' `-'  `-' `----' `-'  | |`------'  `----^----'`-'  `-'`-'  `-' `----'
                             | `--------------------------------------------.
                              `---------------------------------------------' ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step = input("Left or right? ")

if step == "Left":
    action = input("Swim or wait? ")
    if action == "wait":
        door = input("Which doors? red, blue or yellow? ")
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts.. Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")        
else:
    print("Fall into a hole. Game Over.")                     

# Commnet for develop branch
# 
#  Develop Branch    