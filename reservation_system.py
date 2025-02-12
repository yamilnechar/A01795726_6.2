"""
Reservation System Module
Provides classes for managing hotels, customers, and reservations.
"""

import json


class Hotel:
    """Class representing a hotel."""

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def save_to_file(self):
        """Saves the hotel data to a file."""
        try:
            with open(f"hotel_{self.hotel_id}.json", "w", encoding="utf-8") as f:
                json.dump(self.__dict__, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"Error saving hotel data: {e}")

    @classmethod
    def load_from_file(cls, hotel_id):
        """Loads the hotel data from a file."""
        try:
            with open(f"hotel_{hotel_id}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                hotel = cls(data['hotel_id'], data['name'], data['location'], data['rooms'])
                hotel.reservations = data.get('reservations', [])
                return hotel
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading hotel data: {e}")
        return None

    def reserve_room(self, customer_id):
        """Reserves a room for a customer."""
        if self.rooms > len(self.reservations):
            self.reservations.append(customer_id)
            self.save_to_file()
            return True
        return False

    def cancel_reservation(self, customer_id):
        """Cancels a customer's reservation."""
        if customer_id in self.reservations:
            self.reservations.remove(customer_id)
            self.save_to_file()
            return True
        return False


class Customer:
    """Class representing a customer."""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def save_to_file(self):
        """Saves the customer data to a file."""
        try:
            with open(f"customer_{self.customer_id}.json", "w", encoding="utf-8") as f:
                json.dump(self.__dict__, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"Error saving customer data: {e}")

    @classmethod
    def load_from_file(cls, customer_id):
        """Loads the customer data from a file."""
        try:
            with open(f"customer_{customer_id}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return cls(data['customer_id'], data['name'], data['email'])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading customer data: {e}")
        return None


class Reservation:
    """Class representing a reservation."""

    def __init__(self, reservation_id, hotel_id, customer_id):
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def save_to_file(self):
        """Saves the reservation data to a file."""
        try:
            with open(f"reservation_{self.reservation_id}.json", "w", encoding="utf-8") as f:
                json.dump(self.__dict__, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"Error saving reservation data: {e}")

    @classmethod
    def load_from_file(cls, reservation_id):
        """Loads the reservation data from a file."""
        try:
            with open(f"reservation_{reservation_id}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return cls(data['reservation_id'], data['hotel_id'], data['customer_id'])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading reservation data: {e}")
        return None
