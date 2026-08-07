names = ['Nengesha', 'Nguuma', 'Gabriel']

for name in names:
    print('------------------------------------')
    print(f"{name.upper()} is in his 20's and he is hassling in Gboko")
    names[1] = "Daniel"
print('------------------------------------')  
fav_cars = ["bmw", "suv" "Lamborghini"]
fav_cars.append("bugati")
fav_cars.insert(2, "Prado")
print('\n------------------------------------')

print("This is the list of my favorite cars")
for car in fav_cars:
    if car == "bmw" or car == "suv":
        print(car.upper())
    else:
        print(car.title())
print('------------------------------------')
  
#Names of guests
 
guests = ["Pastor Ishaku", "God", "Jesus", "Holy spirit"]

#Massages

massages = ["You are invited to preach at my wedding", 
                      "You are invited to create in me a new heart", 
                      "You are invited to Shine your light in my heart and show me my way", 
                      "You are invited to fill me with you presence"] 
print('\n------------------------------------')  

#First set of invitations

for guest, message in zip(guests, massages):
   
    print(f"\t{guest.upper()}: {message}")
print('------------------------------------')

print('\n-----------------------------------')

#Notice on the first invitation

print('Notice')
notice = (f"I am sorry to bring to your notice that {guests[0]} won't make it to the Event.")
print(notice.upper())
guests[0] = "Pastor Azuana"

print('------------------------------------')

#Second set of invitations

print('\n------------------------------------')
for guest, message in zip(guests, massages):
   
    print(f"\t{guest.upper()}: {message}")
print('------------------------------------')

#more guests because i have found a bigger dining table

print('\n------------------------------------')
print("Notice")
print("I am also to bring to your notice that there will be need for more guest due to increment in the size of the dinner table".upper())

guests.insert(1, "Mr Daniels")
guests.insert(3, "Mr Samuels")
guests.append("Mrs Rebecca")

print('------------------------------------')

#appended messages

massages. insert(1, "You are invited as the hounerable chairman")
massages.insert(3, "You are invited as the Father of the day")
massages.append("You are invited as the mother of the day")

print('\n------------------------------------')

for guest, message in zip(guests, massages):
   
    print(f"\t{guest.upper()}: {message}")
print('\n------------------------------------')

print("Quick Notice")
print("I'm sorry to inform you at this time that l can only take two guests due to the delay in bringing the dining table, I'm so sorry fro the inconvenience".upper())

print('\n------------------------------------')
print(guests.pop(), " I'm sorry I can't invite you again because of the present situation")
        
print(guests.pop(), " I'm sorry I can't invite you again because of the present situation")

print(guests.pop(), " I'm sorry I can't invite you again because of the present situation")
print(guests.pop(1), " I'm sorry I can't invite you again because of the present situation")

print(guests.pop(), " I'm sorry I can't invite you again because of the present situation\n")    

for guest, message in zip(guests, massages):
     print(f"Invitation {guest}: {message}")      
    
del guests[0]      
del guests

print("oops, guests are empty\n")                                                          
places = ["usa", "london", "china", "moon", "artic ocean"] 

for place in places:
    if place == "usa":
        print(place.upper())
    else:
        print(place.title())   
