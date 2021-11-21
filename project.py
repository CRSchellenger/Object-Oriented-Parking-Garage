#weekend project for week 2. John and chris
#Your parking gargage class should have the following methods:
#- 1) takeTicket
#- This should decrease the amount of tickets available by 1
#- This should decrease the amount of parkingSpaces available by 1
#
#- 2) payForParking
#- Display an input that waits for an amount from the user and store it in a variable
#- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
#- This should update the "currentTicket" dictionary key "paid" to True
#
#- 3) leaveGarage
#- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- If the ticket has not been paid, display an input prompt for payment
#- Once paid, display message "Thank you, have a nice day!"
#- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#- Update tickets list to increase by 1 (meaning add to the tickets list)
#
#You will need a few attributes as well:
#- tickets -> list
#- parkingSpaces -> list
#- currentTicket -> dictionary

tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
parkingSpaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
currentTicket = {}
import math #dont remove 
import time #dont remove
import random
def taketicket():
        while True:    
            taketicket = input('Please take a ticket by entering take ticket: ')
            if taketicket == 'take ticket':
                carinfo = input('Please enter your licence plate: ')
                name = input('Please enter your name: ')
                currentTicket[name] = carinfo
                cont = input('Would you like another ticket?: ')
                tickets.pop(0)
                parkingSpaces.pop(0)
                if cont == 'yes':
                    carinfo = input('Please enter your licence plate: ')
                    name = input('Please enter your name: ')
                    currentTicket[name] = carinfo
                    tickets.pop()
                    parkingSpaces.pop()
                elif cont.lower() != 'yes':
                    break
            elif taketicket == 'quit':
                break
            elif taketicket != 'take ticket':
                print('You must take a ticket to park in this garage')
                        
          
pay_li = []      
def payforparking():
    while True:
        leave = input('Would you like to leave [Y][N]: ')
        leave_2 = leave.lower()
        if leave_2 == 'y':
            name = input('Please enter your name: ')
            if name not in currentTicket:
                print('You dont have a ticket for this garage')
            if name in currentTicket:
                totaltime = int(input('Please enter how many minutes you were parked: '))
                time_2 = (totaltime *0.25)
                print(f'Your total is ${time_2}')
                payment_type = input('Please enter how would like to pay: ')
                if payment_type == 'cash':
                    print('Please insert cash below.')
                    time.sleep(0.5)
                    print('One second please')
                    time.sleep(2)
                    print('Thanks for your payment')
                    tickets.insert(-1,+1)        
                    parkingSpaces.insert(-1,+1) 
                elif payment_type == 'card':
                    print('There is a 2\%\ fee for using card')
                    cont_pay = input('Would you like to continue? ')
                    if cont_pay == 'yes':
                        card = input('Please enter your card number: ')
                        time.sleep(1)
                        zip = input('Please enter your zipcode: ')
                        time.sleep(0.5)
                        print('processing your payment please wait.....')
                        time.sleep(1)      #dont erase this line of code please.
                        pay_confirm = random.randint(0,10000000)
                        pay_li.append(pay_confirm)
                        tickets.insert(0,+1)        
                        parkingSpaces.insert(0,+1) 
                        print(f'Thanks for your payment of ${time_2}. Your confirmation code is {pay_confirm}')
                        print(tickets)
                        print(pay_li)
                        print(currentTicket)
                        print(parkingSpaces)
                    elif cont_pay == 'no':
                        print('you may also pay with cash if you wish')
                    else:
                        print('Error-- please check input and try again')
                elif payment_type == 'check':
                    print("We do not accept checks at this time")
        elif leave_2 == 'quit':
            break
        elif leave_2 == 'no':
            print('Please come back when you are ready to leave')

def leave(pay_li):
    if pay_li == False:
        print('You must pay to leave the garage.')
    if pay_li == True:
        print ('Thanks for your businesss have a great day.')
taketicket()
print(tickets)
print(currentTicket)
print(parkingSpaces)
payforparking()
leave(pay_li)
