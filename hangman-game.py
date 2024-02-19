print("Lets play Hangman")
u1=input("User1 please select a word: ")
l1=len(u1)
x=[]
for i in range(l1):
    x.append("-")
fact="The word has {} letters"
print(fact.format(l1))
print(x)

letters = [x for x in u1]
for y in range(l1+5):
 g=input("Guess the letter: ")

 i=0
 while i<l1:
    if letters[i]==g:
        x[i]=g
   
    i=i+1
 print(x)
 if "-" not in x:
    break
print("well done")