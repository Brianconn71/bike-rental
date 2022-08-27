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
        print(f"We have currently {self.stock} bikes available for hire.")

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
                self.stock += 