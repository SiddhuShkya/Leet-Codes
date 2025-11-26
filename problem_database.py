#!/usr/bin/env python3
"""
Batch generator for detailed LeetCode main.txt files.
This script helps create comprehensive documentation faster.
"""

import os
import json
from pathlib import Path

# This file contains problem metadata to help generate detailed docs
# Format: {problem_folder: {title, difficulty, description, examples, constraints}}

PROBLEM_DATABASE = {
    "Climbing Stairs": {
        "difficulty": "EASY",
        "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "examples": [
            {"input": "n = 2", "output": "2", "explanation": "1. 1 step + 1 step\\n2. 2 steps"},
            {"input": "n = 3", "output": "3", "explanation": "1. 1 step + 1 step + 1 step\\n2. 1 step + 2 steps\\n3. 2 steps + 1 step"}
        ],
        "constraints": ["1 <= n <= 45"],
        "algorithm": "Dynamic Programming (Fibonacci sequence)",
        "time_complexity": "O(n)",
        "space_complexity": "O(n) or O(1) with optimization",
        "key_insight": "This is essentially the Fibonacci sequence. The number of ways to reach step n is the sum of ways to reach step (n-1) and step (n-2)."
    },
    "Roman To Integer": {
        "difficulty": "EASY",
        "description": "Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Given a roman numeral, convert it to an integer.",
        "examples": [
            {"input": 's = "III"', "output": "3", "explanation": "III = 3"},
            {"input": 's = "LVIII"', "output": "58", "explanation": "L = 50, V = 5, III = 3"},
            {"input": 's = "MCMXCIV"', "output": "1994", "explanation": "M = 1000, CM = 900, XC = 90, IV = 4"}
        ],
        "constraints": ["1 <= s.length <= 15", "s contains only characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')"],
        "algorithm": "Hash Map with subtraction rules",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "key_insight": "When a smaller value appears before a larger value, subtract it (e.g., IV = 4, IX = 9). Otherwise, add values."
    }
}

def generate_main_txt(problem_name, problem_data, code_content):
    """Generate a detailed main.txt file content."""
    
    title = problem_name.upper()
    difficulty = problem_data["difficulty"]
    description = problem_data["description"]
    examples = problem_data["examples"]
    constraints = problem_data["constraints"]
    
    content = f"""================================================================================
{title} - LEETCODE {difficulty}
================================================================================

PROBLEM STATEMENT:
------------------
{description}

EXAMPLES:
---------
"""
    
    for i, ex in enumerate(examples, 1):
        content += f"""Example {i}:
  Input: {ex['input']}
  Output: {ex['output']}
  Explanation: {ex['explanation']}

"""
    
    content += """CONSTRAINTS:
------------
"""
    for constraint in constraints:
        content += f"- {constraint}\n"
    
    content += f"""

================================================================================
SOLUTION APPROACH
================================================================================

ALGORITHM: {problem_data['algorithm']}

KEY INSIGHT:
{problem_data['key_insight']}

[Detailed explanation would go here - to be filled based on code analysis]


================================================================================
CODE IMPLEMENTATION
================================================================================

{code_content}


================================================================================
COMPLEXITY ANALYSIS
================================================================================

Time Complexity: {problem_data['time_complexity']}
Space Complexity: {problem_data['space_complexity']}


================================================================================
"""
    
    return content

# This is a helper - the actual generation would need to be done problem by problem
print("Problem database loaded. Use this to speed up documentation creation.")
