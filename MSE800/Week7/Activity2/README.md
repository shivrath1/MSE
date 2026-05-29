# Auckland Aquarium Management System

## Overview

This project is a simple Aquarium Management System developed using Python and SQLite.

The system manages different fish types available in an aquarium located in Auckland, including:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

---

# Features

- Add fish into the aquarium system
- Display fish category information
- Store aquarium data using SQLite
- Manage fish counts
- Use design patterns for clean architecture

---

# Design Patterns Used

## 1. Factory Pattern

The Factory Pattern is used to create fish objects dynamically based on user input.

Instead of directly creating objects such as:

```python
Shark()
Goldfish()
```

## 2. Singleton Pattern
The Singleton Pattern ensures that only one instance of a class exists throughout the application.

In this project, the AquariumManager class uses the Singleton Pattern to maintain a single centralized aquarium management system.
This prevents the creation of multiple aquarium manager objects and ensures that all fish management operations are handled consistently through one shared instance.
