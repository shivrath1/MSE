
# Parent Class
class Flight:
    # initialize flight details
    def __init__(self, flight_number, origin, destination,  duration):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.duration = duration

    # common method
    def display_flight(self):
        print("Flight Number:", self.flight_number)
        print("Departure:", self.origin)
        print("Arrival:", self.destination)

    # common method
    def check_status(self):
        print("Flight Status: Scheduled on time")

    def calculate_duration(self): 
        print(f"Estimated Duration: {self.duration}")


# child class single inheritance (Flight)
class DomesticFlight(Flight):
    # inherits attributes from the parent and add a new atrribute to get gate number
    def __init__(self, flight_number, origin, destination, duration, gate_number):
        super().__init__(flight_number, origin, destination, duration)
        self.gate_number = gate_number

    # child class method
    def display_gate(self):
        print("Gate Number:", self.gate_number)
    
    def boarding_info(self): 
        print("Boarding starts 30 minutes before departure")

    def domestic_rules(self):
        print("Valid Photo ID required")

class InternationalFlight(Flight): 
    def __init__(self, flight_number, origin, destination, duration):
        super().__init__(flight_number, origin, destination, duration)
        self.passport_required = True
        self.visa_required = True

    def check_documents(self): 
        print("Passport and Visa verification complete")

    def immigration_info(self): 
        print("Immigration clearance is required")

    def customs_info(self): 
        print("Customs declaration is mandatory")

class PremiumDomesticFlight(DomesticFlight):
    def __init__(self, flight_number, origin, destination, duration, gate_number):
        super().__init__(flight_number, origin, destination, duration, gate_number)
        self.lounge_access = True

    def access_lounge(self):
        print("Premium lounge access granted")
    
    def priority_boarding(self): 
        print("Priority boarding is enabled")
    
    def premium_services(self):
        print("Complimentary meal available")



def main():

    print("\n=== International Flight ====")
    # international flight object
    international = InternationalFlight(
        "NZ701",
        "Auckland",
        "Melbourne",
        "3 hours 30 minutes"
    )
    international.display_flight()
    international.check_status()
    international.calculate_duration()

    international.check_documents()
    international.immigration_info()
    international.customs_info()

    print("\n=== Domestic flight ===")
    # DomesticFlight object
    domestic_flight = DomesticFlight(
        "NZ109",
        "Auckland",
        "Chirstchurch",
        "2 hours",
        "A12"
    )

    # inherited methods
    domestic_flight.display_flight()
    domestic_flight.check_status()
    domestic_flight.calculate_duration()

    # child class method to dispalys the gate number
    domestic_flight.display_gate()
    domestic_flight.boarding_info()
    domestic_flight.domestic_rules()

    print("\n=== PremiumDomestic flight ===")
    # premium domestic flight 
    premium_domestic_flight = PremiumDomesticFlight(
        "NZ305",
        "Auckland",
        "Wellington",
        "1 hour 40 minutes",
        "G1"
    )
    premium_domestic_flight.display_flight()
    premium_domestic_flight.check_status()
    premium_domestic_flight.calculate_duration()
    premium_domestic_flight.access_lounge()
    premium_domestic_flight.priority_boarding()
    premium_domestic_flight.premium_services()
    
if __name__ == "__main__":
    main()