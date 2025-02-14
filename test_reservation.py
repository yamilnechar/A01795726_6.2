import unittest
from reservation_system import Hotel  

class TestHotel(unittest.TestCase):
    """Tests for the Hotel class."""  

    def test_create_hotel(self):
        hotel = Hotel(1, "Hotel Test", "City X", 10)
        self.assertEqual(hotel.name, "Hotel Test")

    def test_reserve_room(self):
        hotel = Hotel(1, "Hotel Test", "City X", 2)
        result = hotel.reserve_room(101)
        self.assertTrue(result)

    def test_cancel_reservation(self):
        hotel = Hotel(1, "Hotel Test", "City X", 2)
        hotel.reserve_room(101)
        result = hotel.cancel_reservation(101)
        self.assertTrue(result)


if __name__ == "__main__":
    with open("test_results.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)
