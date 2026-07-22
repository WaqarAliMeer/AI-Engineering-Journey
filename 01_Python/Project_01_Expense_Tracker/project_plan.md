# Project Plan

## Project Name
Expense Tracker

## Objective
Build a Python console application to record income and expenses and save them in a JSON file.

## Menu
- Add income
- Add expense
- View all transactions
- Show summary
- Save data
- Exit

## Data Structure

Each transaction should contain:

- Type (Income/Expense)
- Category
- Amount
- Date

Example:

```python
{
    "type": "Expense",
    "category": "Fuel",
    "amount": 25,
    "date": "2026-07-20"
}
```

## Functions I'll Need

- add_transactions
- view_transactions()
- show_summary()
- save_data()
- load_data()
- menu()

## Challenges I Expect

- Reading and writing JSON
- Keeping the menu running
- Calculating totals