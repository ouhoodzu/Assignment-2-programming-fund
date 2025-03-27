# Guest class stores basic information and reservation history for a guest
class Guest:
    """
    Represents a hotel guest, storing personal info and reservation history.
    """
    def __init__(self, name: str, email: str, phone_number: int, loyalty_status: str, reservation_history=None):
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._loyalty_status = loyalty_status
        self._reservation_history = reservation_history if reservation_history else []

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str) -> None:
        self._email = email

    def get_phone(self) -> int:
        return self._phone_number

    def set_phone(self, phone: int) -> None:
        self._phone_number = phone

    def get_loyalty_status(self) -> str:
        return self._loyalty_status

    def set_loyalty_status(self, status: str) -> None:
        self._loyalty_status = status

    def get_reservation_history(self) -> list:
        return self._reservation_history

    def set_reservation_history(self, history: list) -> None:
        self._reservation_history = history

    def __str__(self) -> str:
        return f"Guest(name={self._name}, email={self._email}, phone={self._phone_number}, loyalty={self._loyalty_status})"


# LoyalGuest is a subclass of Guest with additional loyalty features
class LoyalGuest(Guest):
    def __init__(self, name: str, email: str, phone_number: int, loyalty_status: str, reservation_history=None,
                 discount_rate: float = 0.0, loyalty_points: int = 0):
        super().__init__(name, email, phone_number, loyalty_status, reservation_history)
        self._discount_rate = discount_rate
        self._loyalty_points = loyalty_points
        self._loyalty_program = LoyaltyProgram()  #  Directed Association: LoyalGuest "uses" LoyaltyProgram

    def get_discount_rate(self) -> float:
        return self._discount_rate

    def set_discount_rate(self, rate: float) -> None:
        self._discount_rate = rate

    def get_loyalty_points(self) -> int:
        return self._loyalty_points

    def set_loyalty_points(self, points: int) -> None:
        self._loyalty_points = points

    def earn_loyalty_points(self):
        #  Uses the LoyaltyProgram to calculate and add points
        new_points = self._loyalty_program.calculate_points()
        self._loyalty_points += new_points

    def __str__(self) -> str:
        return f"LoyalGuest({super().__str__()}, discount_rate={self._discount_rate}, points={self._loyalty_points})"


# Booking class connects a Guest to a Room with check-in/out info
class Booking:
    def __init__(self, booking_id: str, check_in: str, check_out: str, guest: Guest, room):
        self._booking_id = booking_id
        self._check_in = check_in
        self._check_out = check_out
        self._guest = guest
        self._room = room

    def get_booking_id(self) -> str:
        return self._booking_id

    def set_booking_id(self, booking_id: str) -> None:
        self._booking_id = booking_id

    def get_check_in(self) -> str:
        return self._check_in

    def set_check_in(self, date: str) -> None:
        self._check_in = date

    def get_check_out(self) -> str:
        return self._check_out

    def set_check_out(self, date: str) -> None:
        self._check_out = date

    def get_guest(self) -> Guest:
        return self._guest

    def set_guest(self, guest: Guest) -> None:
        self._guest = guest

    def get_room(self):
        return self._room

    def set_room(self, room) -> None:
        self._room = room

    def __str__(self):
        return f"Booking(id={self._booking_id}, guest={self._guest.get_name()}, room={self._room.get_room_number()})"


# Invoice class holds billing details for a booking
class Invoice:
    def __init__(self, invoice_id: str, booking: Booking, extra_charges: float, total_amount: float):
        self._invoice_id = invoice_id
        self._booking = booking
        self._extra_charges = extra_charges
        self._total_amount = total_amount

    def get_invoice_id(self) -> str:
        return self._invoice_id

    def set_invoice_id(self, invoice_id: str) -> None:
        self._invoice_id = invoice_id

    def get_booking(self) -> Booking:
        return self._booking

    def set_booking(self, booking: Booking) -> None:
        self._booking = booking

    def get_extra_charges(self) -> float:
        return self._extra_charges

    def set_extra_charges(self, amount: float) -> None:
        self._extra_charges = amount

    def get_total_amount(self) -> float:
        return self._total_amount

    def set_total_amount(self, amount: float) -> None:
        self._total_amount = amount

    def __str__(self):
        return f"Invoice(id={self._invoice_id}, total={self._total_amount})"


# Room class stores info about individual hotel rooms
class Room:
    def __init__(self, room_number: str, is_available: bool, nightly_rate: float, room_type, amenities: list):
        self._room_number = room_number
        self._is_available = is_available
        self._nightly_rate = nightly_rate
        self._room_type = room_type
        self._amenities = amenities

    def get_room_number(self) -> str:
        return self._room_number

    def set_room_number(self, number: str) -> None:
        self._room_number = number

    def get_is_available(self) -> bool:
        return self._is_available

    def set_is_available(self, status: bool) -> None:
        self._is_available = status

    def get_nightly_rate(self) -> float:
        return self._nightly_rate

    def set_nightly_rate(self, rate: float) -> None:
        self._nightly_rate = rate

    def get_amenities(self) -> list:
        return self._amenities

    def set_amenities(self, list_: list) -> None:
        self._amenities = list_

    def __str__(self):
        return f"Room(number={self._room_number}, type={self._room_type.get_type_name()}, available={self._is_available})"


# RoomType is a subclass with extra room info
class RoomType:
    def __init__(self, type_name: str, base_price: float, occupancy: int, has_balcony: bool):
        self._type_name = type_name
        self._base_price = base_price
        self._occupancy = occupancy
        self._has_balcony = has_balcony

    def get_type_name(self) -> str:
        return self._type_name

    def set_type_name(self, name: str) -> None:
        self._type_name = name

    def get_base_price(self) -> float:
        return self._base_price

    def set_base_price(self, price: float) -> None:
        self._base_price = price

    def get_occupancy(self) -> int:
        return self._occupancy

    def set_occupancy(self, capacity: int) -> None:
        self._occupancy = capacity

    def is_has_balcony(self) -> bool:
        return self._has_balcony

    def set_has_balcony(self, value: bool) -> None:
        self._has_balcony = value

    def __str__(self):
        return f"RoomType(name={self._type_name}, base_price={self._base_price}, balcony={self._has_balcony})"


# Hotel class stores general info and rooms list
class Hotel:
    def __init__(self, name: str, location: str, rating: float, contact_info: str, rooms: list):
        self._name = name
        self._location = location
        self._rating = rating
        self._contact_info = contact_info
        self._rooms = rooms

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_location(self) -> str:
        return self._location

    def set_location(self, location: str) -> None:
        self._location = location

    def get_rating(self) -> float:
        return self._rating

    def set_rating(self, rating: float) -> None:
        self._rating = rating

    def get_contact_info(self) -> str:
        return self._contact_info

    def set_contact_info(self, info: str) -> None:
        self._contact_info = info

    def get_rooms(self) -> list:
        return self._rooms

    def set_rooms(self, rooms: list) -> None:
        self._rooms = rooms

    def __str__(self):
        return f"Hotel(name={self._name}, rating={self._rating})"


# ServiceRequest class holds any guest requests like cleaning, food, etc.
class ServiceRequest:
    def __init__(self, request_type: str, description: str, status: str, request_date: str):
        self._request_type = request_type
        self._description = description
        self._status = status
        self._request_date = request_date

    def get_request_type(self) -> str:
        return self._request_type

    def set_request_type(self, type_: str) -> None:
        self._request_type = type_

    def get_description(self) -> str:
        return self._description

    def set_description(self, desc: str) -> None:
        self._description = desc

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: str) -> None:
        self._status = status

    def get_request_date(self) -> str:
        return self._request_date

    def set_request_date(self, date: str) -> None:
        self._request_date = date

    def __str__(self):
        return f"ServiceRequest(type={self._request_type}, status={self._status})"


# LoyaltyProgram is a simple utility class to calculate points
class LoyaltyProgram:
    def calculate_points(self) -> int:
        # Placeholder for actual logic to calculate points based on bookings
        return 100

