
# Parent Class
class Flight:
    # initialize flight details
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination

    # common method
    def display_flight(self):
        print("Flight Number:", self.flight_number)
        print("Departure:", self.origin)
        print("Arrival:", self.destination)

    # common method
    def check_status(self):
        print("Flight Status: Scheduled on time")


# child class single inheritance (Flight)
class DomesticFlight(Flight):
    # inherits attributes from the parent and add a new atrribute to get gate number
    def __init__(self, flight_number, origin, destination, gate_number):
        super().__init__(flight_number, origin, destination)
        self.gate_number = gate_number

    # child class method
    def display_gate(self):
        print("Gate Number:", self.gate_number)


def main():
    # DomesticFlight object
    domestic_flight = DomesticFlight(
        "NZ109",
        "Auckland",
        "Chirstchurch",
        "A12"
    )

    # inherited methods
    domestic_flight.display_flight()
    domestic_flight.check_status()

    # child class method to dispalys the gate number
    domestic_flight.display_gate()

if __name__ == "__main__":
    main()