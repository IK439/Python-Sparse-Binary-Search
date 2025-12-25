# Python-Sparse-Binary-Search

## Overview
This project demonstrates a **sparse binary search** implementation in Python.
Sparse search is a variation of binary search that works on sorted lists containing
empty strings (`""`) between valid values.

The project is split into two files:
- A **driver script** that tests the search function
- A **search algorithm** that performs the sparse search

---

## test.py: Driver Script

This file is responsible for testing the `sparse_search` function.

### What it does
- Imports `sparse_search` from `script.py`
- Tests the function with:
  - A sparse list of names
  - A sparse list of numeric strings
- Prints whether the value was found and at which index

### Key concepts demonstrated
- Function importing
- Handling return values
- Testing multiple datasets

---

## script.py: `sparse_search` Function

This file contains the implementation of the sparse binary search algorithm.

### Features
- Works with **strings** and **numeric strings**
- Safely skips empty strings during the search
- Returns:
  - The index of the found value
  - `-1` if the value is not found

### How it works (high level)
1. Perform a standard binary search
2. If the middle value is empty:
   - Scan left and right to find the closest non-empty value
3. Compare values using:
   - Numeric comparison when both values are numbers
   - String comparison otherwise

---

## Example Output

```
Calling sparse_search.....
Sophia found at index 16

Calling sparse_search.....
7 found at index 3
```

---

## Learning Outcomes
- Understanding sparse data structures
- Applying binary search beyond ideal datasets
- Writing reusable and testable functions

---

## Notes
- The dataset must remain **sorted** (ignoring empty strings)
- Numeric values are expected to be stored as strings
