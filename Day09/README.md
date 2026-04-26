### Smart Inventory Mutation Tracker

## Overview

This project demonstrates how data behaves when using **shallow copy** and **deep copy** in Python. It simulates an inventory system with nested data and tracks how changes affect the original data.

## Problem Statement

* Store inventory using a list of dictionaries (nested structure)
* Create shallow and deep copies
* Modify copied data
* Compare original and modified data
* Analyze differences

## Personalization

* Roll Number: **576**
* Inventory Length: **2**
* Index Used: `576 % 2 = 0`
* Only the first item (Laptop) is modified

## Features

* Uses functions for modular design
* Applies 10% discount to selected item
* Updates stock value
* Compares original vs copied data
* Demonstrates difference between shallow and deep copy

## Technologies Used

* Python
* Lists and Dictionaries
* Functions
* Copy module (`copy`, `deepcopy`)

## How It Works

1. Create inventory data
2. Generate shallow and deep copies
3. Apply mutation based on roll number
4. Compare results
5. Display differences

## Output Summary

* Shallow copy affects original data
* Deep copy keeps original data unchanged
* Result shown as tuple: `(changed_items, unchanged_items)`

## Learning Outcome

* Understanding of shallow vs deep copy
* Handling nested data structures
* Avoiding unintended data modification


