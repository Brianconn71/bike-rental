import datetime

class BikeRental:

    def __init__(self, stock=0):
        """ 
        Constructor class that instantiates bike rental shop.
        """
        self.stock = stock

    def displaystock(self):
        """
        Displays bikes currently available for hire
        """
        print(f"We have currently {self.stock} bikes available for hire")

    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on an hourly basisto a customer

        Args:
            n (_type_): _description_
        """
        if n<=0:
            print("We need a real number of bikes yyou want lad!")
            return None
        # do not rent a bike if stock is less than requested bikes
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent!")
            return None
        # Now we can rent bikes
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike/s on an hourly basistoday at {now.hour} hours")
            print("You will be charge $5 per hour per bike.")
            print("We hope you enjoy our service")

            self.stock -= n
            return now

        def rentBikeOnDailyBasis(self, n):
            """
            Rentas a bike on a daily basis to a customer

            Args:
                n (_type_): _description_
            """                           

            if n <=0:
                print("Number of bikes must be greater than 0")
                return None
            elif n > self.stock:
                print(f"Sorry! We currently have {self.stock} bikes awailable to rent")
                return None
            else:
                now = datetime.datetime.now()
                print(f"You have rented {n} bike/s on a daily basis today at {now.hour}")
                print("You will be charged $20 for each day per bike")
                print("We hope that you enjoy our service.")

                self.stock -= n
                return now
        
        def rentBikeOnWeeklyBasis(self, n):
            """
            Rents a bike on a weekly basis to a customer

            Args:
                n (_type_): _description_
            """    
            if n <=0:
                print("Number of bikes must be greater than 0")
                return None
            elif n > self.stock:
                print(f"Sorry! We currently have {self.stock} bikes awailable to rent")
                return None
            else:
                now = datetime.datetime.now()
                print(f"You have rented {n} bike/s on a weekly basis today at {now.hour}")
                print("You will be charged $60 for each week per bike")
                print("We hope that you enjoy our service.")

                self.stock -= n
                return now    

        def returnBike(self, request):
            """
            1. Accept a rented bike from a customer
            2. Replenish the inventory
            3. Return a bill

            Args:
                request (_type_): _description_
            """               
            # extract the tuple and initiate bill
            rentalTime, rentalBasis, numOfBikes = request
            bill = 0

            # issue a bill only if all three params are not null
            if rentalTime and rentalBasis and numOfBikes:
                self.stock += numOfBikes
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
            
                # hourly bill calculation
                if rentalBasis == 1:
                    bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

                # daily bill calculation
                elif rentalBasis == 2:
                    bill = round(rentalPeriod.days) * 20 * numOfBikes
                # Weekly calculation
                elif rentalBasis == 3:
                    bill = round(rentalPeriod.days) * 20 * numOfBikes
                # family discount calculation
                if (3 <= numOfBikes <=5):
                    print("You are eligible for a family discount of 30%")
                    bill = bill * 0.7

                print("Thanks for returning your bike. I hope you enjoyed your ride ;)")
                print(f"That will be ${bill}")
                return bill
            else:
                print("Are you sure you rented a bike with us pal?")
                return None


class Customer:
    def __init__(self):
        """
        constructor method to instantiate various customer objects
        """
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        """
        Takes a request from customer for amount of bikess
        """
        bikes = input("How many sir?")

        # Logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError as e:
            print("Thats not a valid input please add a number greater than zero.")
            return -1
        
        if bikes < 1:
            print("Invalid input. Number of bikes must be greater than zero.")
            return -1
        else:
            self.bikes = bikes
    
    def returnBike(self):
        """
        Allows customers to return their bikes to the renatl shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0        