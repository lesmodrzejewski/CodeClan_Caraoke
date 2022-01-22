class Room:
    def __init__(self, room_number, space):
        self.room_number = room_number
        self.space = space
        self.guests = []

    def add_guest_to_room(self, guest):
        self.guests.append(guest)
    
    def count_guests(self, guests):
        return len(guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self):
        self.guests.pop()
    
    def is_enough_space(self, guests):
        if self.count_guests(guests) <= self.space:
            return True
        else:
            return False
