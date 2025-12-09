
# Algorithm Name
Linear Search Algorithm

# Demo video/gif/screenshot of test
All SS can be located in the file area on the left of the screen.

# Why I Chose Linear Search

I chose to apply a linear search for a few reasons...

- Linear search is the first searching algorithm you learn, and builds a foundation before learning more advanced methods
- The process scans the list item by item, which is easy to understand, trace, and visualize
- It clearly shows how algorithmic thinking turns a simple idea such as, check every element, into a precise and repeatable procedure

This makes it a good example for demonstrating computational thinking.


## Problem Breakdown & Computational Thinking 

What the app does...

Given a list and a target value, the app runs linear search and shows each comparison step by step, then returns the index if found, or -1 if not found.


Decomposition:
- Parse user input into a list of numbers
- Read target value
- Scan the list left-to-right
- Compare each element to the target
- Stop when found, otherwise return -1 at the end

Pattern Recognition:
- The same action repeats for each element: “compare current value to target”
- The only thing that changes each step is the index/value being compared

Abstraction:
- The user doesn’t need to know Python loops—only enters a list + target
- The app shows the algorithm as simple “compare” steps instead of code

Algorithm Design:
- Input: list of numbers, target number
- Process: sequential comparisons from index 0 onward
- Output: found index (or -1) + a step-by-step trace


## Testing & Verification

I tested the app using several kinds of inputs:

Target Present in the Middle: Refer to SS Middle
- List: `4, 9, 1, 7, 3`  
- Target: `1`  
- Expected: Find `1` at index 3 after checking indices 0–3.  
- Result: App shows each step correctly and stops at index 3.

Target at the Beginning: Refer to SS Beginning
- List: `5, 10, 20`  
- Target: `5`  
- Expected: Found at index 0 on the first step.  
- Result: App reports the correct index and only one step.

Target at the End: Refer to SS End
- List: `2, 4, 6, 8`  
- Target: `8`  
- Expected: Checks indices 0–3 and finds the target at index 3.  
- Result: Output matches expectation with a full trace.

Target Not Present: Refer to SS Not Present
- List: `1, 3, 5, 7`  
- Target: `4`  
- Expected: Checks all elements and then reports that the target was not found, FAILURE  
- Result: App states that 4 is not in the list and explains that the search stops at the end

Single Element List: Refer to SS Single Element
- List: `9`  
- Target: `9`  
- Expected: First case found at index 0, second case not found.  
- Result: Correctly handles scenario

Invalid Input Handling: Refer to SS Error
- List: `1, a, 3` or an empty string  
- Expected: Error message instead of a crash.  
- Result: App shows “Input Error” with a clear explanation


## Steps to Run
```bash
pip install -r requirements.txt
python app.py

## Hugging Face Link

## Author & Acknowledgment
``` Author: Evan Zachari

This project was created for the CISC-121 Python App assignment to demonstrate a searching algorithm (Linear Search) with an interactive user interface using Gradio
'''