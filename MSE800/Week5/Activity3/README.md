# Brief Description

The activity diagram represents the activity of a clinic management system using three swimlanes: **Patient**, **System**, and **Clinic Staff/Pharmacy**.

## Appointment Phase
1. The patient requests an appointment.
2. The system checks slot availability.
3. If no slot is available, the patient is notified.
4. If a slot is free, the system confirms the appointment.
5. The patient receives the confirmation.

## Payment Phase
6. The patient proceeds with the booking payment.
7. The system processes the payment.
8. If the payment fails, the patient retries.
9. If successful, the system issues a receipt and updates the clinic schedule.

## Medication Phase
10. The system checks whether the patient wants to order medication.
11. The patient selects medication and the system validates the prescription.
12. If the prescription is invalid, the patient reselects medication.
13. If valid, the medication order is confirmed.
14. The clinic staff or pharmacy dispenses the medication.
15. Finally, the patient receives the medication and the process ends.

The diagram represents the interaction between the patient, the clinic system, and the clinic staff through the appointment booking, payment processing, and medication handling processes.