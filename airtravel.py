class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code'{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number: '{}'".format(number))

        self._airlineCode = number[:2]
        self._routeNumber = number[2:]
        self._aircraft = aircraft

        rows, letters = self.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in letters} for row in rows]
        # this is a list of dictionaries, combining list and dictionary comprehensions

    def number(self):
        return self._airlineCode + self._routeNumber

    def aircraft_model(self):
        return self._aircraft.model()

    def seating_plan(self):
        return self._aircraft.seating_plan()

    def relocate_passenger(self, old_seat, new_seat, passenger):
        if not self.seat_allocated_for_passenger(old_seat, passenger):
            raise ValueError(
                "Seat: {0} is not allocated for a passenger: {1}".format(old_seat, passenger))

        if self.seat_already_allocated(new_seat):
            raise ValueError("Seat: {0} is already allocated".format(new_seat))

        self.allocate_seat(new_seat, passenger)
        self.delocate_seat(old_seat)

    def seat_allocated_for_passenger(self, seat, passenger):
        row, letter = self._parse(seat)
        return self._seating[row][letter] == passenger

    def seat_already_allocated(self, seat):
        row, letter = self._parse(seat)
        return self._seating[row][letter] != None

    def delocate_seat(self, seat):
        row, letter = self._parse(seat)
        self._seating[row][letter] = None

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse(seat)

        allocated_passenger = self._seating[row][letter]
        if allocated_passenger is not None:
            raise ValueError(
                "Seat: {0} already occupied by passenger: {1}".format(seat, allocated_passenger))

        self._seating[row][letter] = passenger

    # this is some HC shit with generator comprehensions
    def num_available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self._seating if row is not None)

    def _parse(self, seat):
        row = int(seat[:-1])
        letter = seat[-1]
        return row, letter


class Aircraft:
    def __init__(self, num_rows, num_seats_per_row):
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


def make_flight():
    f = Flight("BG101", Aircraft(12, 4))
    f.allocate_seat("1A", "Dragan")
    f.allocate_seat("2B", "Dejan")
    f.allocate_seat("3C", "Gordana")
    f.allocate_seat("4D", "Goran")
    f.allocate_seat("10A", "Jelena")
    return f
