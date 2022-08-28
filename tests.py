import unittest
from datetime import datetime, timedelta
from main import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):

    def test_Bike_Rental_Displays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEquals(shop1.displaystock(), 0)
        self.assertEquals(shop2.displaystock(), 10)
    
    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)
    
    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(0), None)
    
    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        now = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, now)
    
    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(11), None)
    
    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)
    
    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0), None)
    
    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)
    
    def test_rentBikeOnDailyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(11), None)
    
    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)
    
    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0), None)
    
    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        now = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, now)
    
    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(11), None)
    
    def test_renturnBike_for_invalid_rentalTime(self):
        # Create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()
        
        # Let customer not rent a bike and try to return a bike
        request = customer.returnBike()
        self.
        