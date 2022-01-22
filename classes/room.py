class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guests = []

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
    
    def count_guests(self, guests):
        return len(guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self):
        self.guests.pop()