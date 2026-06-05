# Air New Zealand Flight Management System

## Overview

This project demonstrates the use of **Hybrid Inheritance** in Python through a simple Air New Zealand flight management system.

The system includes a parent class (`Flight`) and multiple child classes that inherit and extend its functionality.

## Classes

### Flight (Parent Class)

Stores common flight information and methods shared by all flights.

**Attributes**
- flight_number
- origin
- destination
- airline_name

**Methods**
- display_flight()
- check_status()
- calculate_duration()

---

### DomesticFlight (Child Class)

Inherits from `Flight` and adds domestic flight features.

**Additional Attributes**
- gate_number

**Methods**
- display_gate()
- boarding_info()
- domestic_rules()

---

### InternationalFlight (Child Class)

Inherits from `Flight` and adds international flight features.

**Additional Attributes**
- passport_required
- visa_required

**Methods**
- check_documents()
- immigration_info()
- customs_info()

---

### PremiumDomesticFlight (Grandchild Class)

Inherits from `DomesticFlight`.

**Additional Attributes**
- lounge_access

**Methods**
- access_lounge()
- priority_boarding()
- premium_services()

---

## Inheritance Structure

```text
Flight
├── DomesticFlight
│   └── PremiumDomesticFlight
└── InternationalFlight
```

