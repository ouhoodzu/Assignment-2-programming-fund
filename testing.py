# testing.py
# Simulated full hotel system run: Royal Stay Hotel - Ahmed, Salem, Ali

from classes import Guest, LoyalGuest, RoomType, Room, Booking, Invoice, Hotel, LoyaltyProgram

# --- Hotel Initialization ---
print("\n--- Royal Stay Hotel Simulation ---")

# Create Royal Stay Hotel with 500 rooms
rooms = []
room_type = RoomType("Suite", 700.0, 2, True)
for i in range(1, 501):
    room_number = str(100 + i)
    room = Room(room_number, True, 750.0, room_type, ["Wi-Fi", "Mini Bar"])
    rooms.append(room)

hotel = Hotel("Royal Stay Hotel", "Dubai", 5.0, "contactcenterhelpdubai@royalstay.ae", rooms)
print(f"Hotel Created: {hotel}\nTotal Rooms: {len(hotel.get_rooms())}")

# --- Register Loyal Guests ---
loyalty_program = LoyaltyProgram()
ahmed = LoyalGuest("Ahmed", "ahmedali2005@hotmail.com", 5443345, "Gold", [], 0.10, 0)
salem = LoyalGuest("Salem", "salem2000@gmail.com", 544313282, "Silver", [], 0.05, 0)
ali   = LoyalGuest("Ali",   "ali1990@outlook.com", 506689883, "Bronze", [], 0.02, 0)
guests = [ahmed, salem, ali]

print("\nLoyal Guests Registered:")
for guest in guests:
    print(guest)

# --- Make Bookings ---
print("\nCreating Bookings...")
booking1 = Booking("B001", "2025-01-01", "2025-01-05", ahmed, hotel.get_rooms()[0])
booking2 = Booking("B002", "2025-01-02", "2025-01-06", salem, hotel.get_rooms()[1])
booking3 = Booking("B003", "2025-01-05", "2025-01-10", ali,   hotel.get_rooms()[2])

ahmed.set_reservation_history([booking1])
salem.set_reservation_history([booking2])
ali.set_reservation_history([booking3])

print("\nBookings Created:")
print(booking1)
print(booking2)
print(booking3)

# --- Generate Invoices ---
invoice1 = Invoice("I001", booking1, 50.0, 1450.0)
invoice2 = Invoice("I002", booking2, 30.0, 1600.0)
invoice3 = Invoice("I003", booking3, 40.0, 2000.0)

invoices = [invoice1, invoice2, invoice3]
print("\nInvoices:")
for inv in invoices:
    print(inv)

# --- Apply Loyalty Points (simulated with LoyaltyProgram) ---
print("\nApplying Loyalty Points...")
ahmed.set_loyalty_points(loyalty_program.calculate_points())
salem.set_loyalty_points(loyalty_program.calculate_points())
ali.set_loyalty_points(loyalty_program.calculate_points())

print(f"Ahmed Points: {ahmed.get_loyalty_points()} | Discount Rate: {ahmed.get_discount_rate()*100:.0f}%")
print(f"Salem Points: {salem.get_loyalty_points()} | Discount Rate: {salem.get_discount_rate()*100:.0f}%")
print(f"Ali Points:   {ali.get_loyalty_points()} | Discount Rate: {ali.get_discount_rate()*100:.0f}%")

# --- Validate Payments (simulated) ---
print("\nValidating Payments...")
for inv in invoices:
    amount_paid = inv.get_total_amount()
    print(f"Invoice {inv.get_invoice_id()}: AED {amount_paid} paid | Status: Payment Valid")

# --- Display Reservation History ---
print("\nReservation History:")
for guest in guests:
    print(f"\n{guest.get_name()}'s Reservations:")
    for b in guest.get_reservation_history():
        print(f"- {b}")

# --- Simulate Reservation Cancellation ---
print("\nReservation Cancellation Simulation:")
room_cancel = hotel.get_rooms()[3]
print(f"Before cancellation: Room {room_cancel.get_room_number()} available? {room_cancel.get_is_available()}")
room_cancel.set_is_available(True)
print(f"After cancellation:  Room {room_cancel.get_room_number()} available? {room_cancel.get_is_available()}")

