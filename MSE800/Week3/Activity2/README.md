# Money Exchange App – Database Design

## Overview
This project represents the database design for a money exchange app. The model represents customer accounts, how transactions are performed and how exchange rates, currencies, and fees are applied.

---

## Entities

### Customer
Stores customer/user information.

**Attributes:**
- `customer_id` (PK)
- `full_name`
- `email`
- `phone_number`
- `kyc_status`

A customer can own multiple accounts (Customer → Account 1:N).

---

### Account
Bank account/'s owned by a customer.

**Attributes:**
- `account_id` (PK)
- `customer_id` (FK → Customer)
- `account_number`
- `balance`
- `account_type`
- `account_status`

A customer account can send or receive many transactions (Account → Transaction 1 : N).

---

### Transaction
Transaction event made by the customer

**Attributes:**
- `transaction_id` (PK)
- `from_account_id` (FK → Account)
- `to_account_id` (FK → Account)
- `rate_id` (FK → Exchange Rate)
- `fee_id` (FK → Fee)
- `amount_sent`
- `amount_received`
- `status`
- `txn_date`

Each Txn debits and credits respective accounts (Transaction → Account N : 1 ).
Each transaction may use one exchange rate (Transaction → Exchange Rate N : 1).
Each transaction may include a fee (Transaction → Fee N : 1).

---

### Currency
Supported currencies for the exchange

**Attributes:**
- `currency_code` (PK)
- `currency_name`
- `country_code`
- `symbol`
- `is_active`

---

### Exchange Rate
Stores currency conversion rates

**Attributes:**
- `rate_id` (PK)
- `from_currency` (FK → Currency)
- `to_currency` (FK → Currency)
- `rate_value`
- `exchange_date`

---

### Fee
Transaction charges

**Attributes:**
- `fee_id` (PK)
- `fee_type`
- `amount`
- `from_currency` (FK → Currency)
- `to_currency` (FK → Currency)

---

