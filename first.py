# lets practice and learn python
# Lists:
names=["Sara", "Mina","Jack"]
family=["Pete","Kley"]
for x in names:
    for y in family:
        print(x,y)

# Count how many "a" in a text
txt='This HG is a very important part of the turbine. Because basement of bearing No1 is inside of this HG. And also air will goes inside the machine from this HG. many sensors are located in this part. Rotor of Gas generator will adapts its own axial displacement from this part. passage of Lubrication of bearing No1 are located inside of this HG. this part has a role for making many measurements during assembly of gas generator. And also has a important role for sealing of bearing No1. if you have a deeper look in to this part, you will notify that from the manufacturing view, this part has many casting parts, forges part. After welding HG 4210 has a huge machining and very restricted tolerances. So it means even during handling and lifting of this Hg you should care about the way of this handlings.'
i=0
for x in txt:
    if x=="a":
        i+=1
print(i)

#Define a simple shop
goods={
    "Shirt":28,
    "Coat":90,
    "Glass":24,
    "Scarf":12,
    "Shoes":15
}
def ordergood():
   order=input("What do you want to buy?(Shirt,Coat,Glass,Scarf,Shoes)")
   if order in goods:
    price="The {} is {} Dollars."
    print(price.format(order,goods[order]))
    want=input("Do you want it or not?Y,N  ")
    if want=="Y":
        print("Great,Send me Email")
        another1=input("Do you want Another goods?Y,N  ")
        if another1=="Y":
          ordergood()
        else:
          print("OK,Maybe next time")
    elif want=="N":
       another=input("Do you want Another goods?Y,N  ")
       if another=="Y":
          ordergood()
       else:
          print("OK,Maybe next time")

ordergood()
