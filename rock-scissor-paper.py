import random

print("Lets Play, Game will end if you press exit")
for x in range(100):
 userSelect=input("Choose one: Rock, Scissor , Paper (or exit to end the game) ").lower()
 states=["rock","scissor","paper"]
 computerSelect=random.sample(states,k=1)
 print("You select: "+userSelect)
 print("Computer selects: "+computerSelect[0])
 print("So .....")
 if computerSelect[0]==userSelect:
    print("You are in tie with computer")
 elif (computerSelect[0]=="rock" and userSelect=="scissor") or (computerSelect[0]=="scissor" and userSelect=="paper") or (computerSelect[0]=="paper" and userSelect=="rock"):
    print("oh no! Computer wins")
 elif userSelect=="exit":
    break
 elif (computerSelect[0]=="rock" and userSelect=="paper") or (computerSelect[0]=="scissor" and userSelect=="rock") or (computerSelect[0]=="paper" and userSelect=="scissor"):
    print("Perfect, You win")
 else:
    print("Please type a correct word")
print("Game end")
