print ("Hello and Welcome to our shop")

computer=1000

keyboard=500

mouse=100

printer=700

ups=200
amount= 0
print("we have computer, keyboard, mouse, printer, ups,")

print ("what whould you like to buy : ")
c1= input("")
if c1== "computer":
    print ("that would be: "+str(computer))
    amount=int(input("please enter the amount :"))
    if amount==computer :
        print("Thank you for shoppping with us")
    if amount < computer:
        print("sorry sir if you want to buy this product so you need : " +str(computer - amount ))
    if amount > computer :
        print("Thankyou for shopping here is your remaing money : " +str( amount -  computer))

if c1== "keyboard":
    print("that would be: "+str(keyboard))
    amount=int(input("please enter the amount: "))
    if amount==keyboard:
        print("Thank you for shoppping with us")
    if amount < keyboard:
        print("sorry sir if you want to buy this product so you need" +str(keyboard - amount))
    if amount > keyboard :
        print("Thankyou for shopping here is your remaing money : " +str(amount - keyboard ))


   
    
if c1== "mouse":
    print ("that would be: "+str(mouse))
    amount=int(input("please enter the amount : "))
    if amount==mouse:
        print("Thank you for shoppping with us")
    if amount < mouse:
        print("sorry sir if you want to buy this product so you need : " +str(mouse-amount  ))
    if amount > mouse :
        print("Thankyou for shopping here is your remaing money : " +str(amount - mouse ))


   




if c1== "printer":
    print ("that would be: "+str(printer))
    amount=int(input("please enter the amount : "))
    if amount==printer:
        print("Thank you for shoppping with us")

    if amount < printer:
        print("sorry sir if you want to buy this product so you need : " +str( printer - amount ))
    if amount > printer :
        print("Thankyou for shopping here is your remaing money : " +str( amount - printer ))




if c1== "ups":
    print ("that would be: "+str(ups))
    amount=int(input("please enter the amount : "))
    if amount==ups:
        print("Thank you for shoppping with us")

    if amount < ups:
        print("sorry sir if you want to buy this product so you need : " +str(ups - amount ))
    if amount > ups :
        print("Thankyou for shopping here is your remaing money : " +str(amount - ups ))

