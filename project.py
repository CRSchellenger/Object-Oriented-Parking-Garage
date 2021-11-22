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

import time
class ParkingGarage():
    def __init__(self):
        self.tickets = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
        self.parkingspaces = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
        self.currentticket = {}
        self.takeTicket()
    def takeTicket(self):
        response = input('Would you like to take a ticket? Yes or No?').lower()
        if response != 'yes' and response != 'no':
            print("Please enter yes or no!")
            self.takeTicket()
        if response == 'yes':
            if len(self.parkingspaces) > 0:
                self.parkingspaces.pop()
                self.tickets.pop()
                self.PayforParking()
            else:
                print("We are full")
        if response == 'no':
            print("Please come back later")
    def PayforParking(self):
        hours_parked = int(input("Please enter how many hours you were parked for in digits! "))
        cost = hours_parked * 8
        print("Your price is " + str(cost) + "dollas")
        paymenttype = input("What method of payment are you using? Cash or Card? ").lower()
        if paymenttype == 'cash':
            payment = int(input("How much would you like to pay?" ))
            print('Please insert cash below.')
            time.sleep(0.5)
            print('One second please')
            time.sleep(2)
            if payment == cost:
                self.currentticket['paid'] = True
                print('Thanks for your payment')
                self.LeaveGarage()
            if payment > cost:
                self.currentticket['paid'] = True
                change = payment - cost
                print(f"Here, please take your {change} dollars!")
                print('Thanks for your payment')
                self.LeaveGarage()
            if payment < cost:
                self.currentticket['paid'] = False
                print("Please cover the full amount! We give change!" )
                self.PayforParking()
        if paymenttype == 'card':
                print('There is a 2\%\ fee for using card')
                cont_pay = input('Would you like to continue? Enter Yes or No ').lower()
                if cont_pay == 'yes':
                    card = input('Please enter your card number: ')
                    time.sleep(1)
                    zip = input('Please enter your zipcode: ')
                    time.sleep(0.5)
                    print('processing your payment please wait.....')
                    time.sleep(1)      #dont erase this line of code please.
                    self.currentticket['paid'] = True
                    self.LeaveGarage()
    def LeaveGarage(self):
        if self.currentticket['paid'] == True:
            print("Thank you, come again!")
            self.tickets.append('1')
            self.parkingspaces.append('1')
myticket = ParkingGarage()