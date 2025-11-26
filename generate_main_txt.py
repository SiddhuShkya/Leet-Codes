#!/usr/bin/env python3
"""
Automation script to standardize LeetCode problem structure.
Creates main.txt files and removes ques.txt files.
"""

import os
import glob
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent
DIFFICULTIES = ['Easy', 'Medium', 'Hard']

def read_file_safe(filepath):
    """Safely read file content, return empty string if file doesn't exist."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return ""

def write_file_safe(filepath, content):
    """Safely write content to file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  ❌ Error writing {filepath}: {e}")
        return False

def extract_problem_name(folder_path):
    """Extract problem name from folder path."""
    return os.path.basename(folder_path)

def determine_difficulty(folder_path):
    """Determine difficulty from folder path."""
    if '/Easy/' in str(folder_path):
        return 'EASY'
    elif '/Medium/' in str(folder_path):
        return 'MEDIUM'
    elif '/Hard/' in str(folder_path):
        return 'HARD'
    return 'UNKNOWN'

def generate_main_txt(problem_folder):
    """Generate main.txt for a problem folder."""
    problem_name = extract_problem_name(problem_folder)
    difficulty = determine_difficulty(problem_folder)
    
    # Find ques.txt or ques.md
    ques_file = None
    for ext in ['txt', 'md']:
        potential_file = os.path.join(problem_folder, f'ques.{ext}')
        if os.path.exists(potential_file):
            ques_file = potential_file
            break
    
    # Find main.py
    main_py = os.path.join(problem_folder, 'main.py')
    
    # Read content
    problem_statement = read_file_safe(ques_file) if ques_file else "Problem statement not available."
    code_implementation = read_file_safe(main_py) if os.path.exists(main_py) else "# Code not available"
    
    # Clean up problem statement (remove extra newlines)
    problem_statement = problem_statement.strip()
    
    # Generate main.txt content
    content = f"""{'='*80}
{problem_name.upper()} - LEETCODE {difficulty}
{'='*80}

PROBLEM STATEMENT:
------------------
{problem_statement}


{'='*80}
SOLUTION APPROACH
{'='*80}

[This section can be enhanced with detailed explanation]

Algorithm:
1. Analyze the problem requirements
2. Implement the solution
3. Test with examples


{'='*80}
CODE IMPLEMENTATION
{'='*80}

{code_implementation}


{'='*80}
COMPLEXITY ANALYSIS
{'='*80}

Time Complexity: O(?)
  - [To be analyzed based on the implementation]

Space Complexity: O(?)
  - [To be analyzed based on the implementation]


{'='*80}
"""
    
    return content

def process_problem_folder(problem_folder):
    """Process a single problem folder."""
    problem_name = extract_problem_name(problem_folder)
    
    # Check if main.txt already exists
    main_txt_path = os.path.join(problem_folder, 'main.txt')
    if os.path.exists(main_txt_path):
        print(f"  ⏭️  Skipping {problem_name} (main.txt already exists)")
        return {'status': 'skipped', 'reason': 'main.txt exists'}
    
    # Check if main.py exists
    main_py_path = os.path.join(problem_folder, 'main.py')
    if not os.path.exists(main_py_path):
        print(f"  ⚠️  Warning: {problem_name} has no main.py")
        # Continue anyway to create main.txt from ques.txt
    
    # Generate main.txt
    content = generate_main_txt(problem_folder)
    
    # Write main.txt
    if write_file_safe(main_txt_path, content):
        print(f"  ✅ Created main.txt for {problem_name}")
        return {'status': 'created', 'path': main_txt_path}
    else:
        return {'status': 'failed', 'reason': 'write error'}

def remove_ques_files(problem_folder):
    """Remove ques.txt and ques.md files from problem folder."""
    removed = []
    for ext in ['txt', 'md']:
        ques_file = os.path.join(problem_folder, f'ques.{ext}')
        if os.path.exists(ques_file):
            try:
                os.remove(ques_file)
                removed.append(f'ques.{ext}')
                print(f"  🗑️  Removed ques.{ext}")
            except Exception as e:
                print(f"  ❌ Error removing {ques_file}: {e}")
    return removed

def main():
    """Main execution function."""
    print("="*80)
    print("LEETCODE PROBLEM STRUCTURE STANDARDIZATION")
    print("="*80)
    print()
    
    stats = {
        'total_processed': 0,
        'created': 0,
        'skipped': 0,
        'failed': 0,
        'ques_removed': 0
    }
    
    # Process each difficulty level
    for difficulty in DIFFICULTIES:
        difficulty_path = BASE_DIR / difficulty
        
        if not difficulty_path.exists():
            print(f"⚠️  {difficulty} directory not found, skipping...")
            continue
        
        print(f"\n{'='*80}")
        print(f"Processing {difficulty} Problems")
        print(f"{'='*80}\n")
        
        # Find all problem folders (directories with main.py)
        problem_folders = []
        for item in difficulty_path.iterdir():
            if item.is_dir():
                problem_folders.append(item)
        
        problem_folders.sort()
        
        for problem_folder in problem_folders:
            stats['total_processed'] += 1
            
            # Process main.txt creation
            result = process_problem_folder(problem_folder)
            
            if result['status'] == 'created':
                stats['created'] += 1
            elif result['status'] == 'skipped':
                stats['skipped'] += 1
            elif result['status'] == 'failed':
                stats['failed'] += 1
    
    # Now remove all ques.txt files
    print(f"\n{'='*80}")
    print("Removing ques.txt files")
    print(f"{'='*80}\n")
    
    for difficulty in DIFFICULTIES:
        difficulty_path = BASE_DIR / difficulty
        
        if not difficulty_path.exists():
            continue
        
        print(f"\nCleaning {difficulty}...")
        
        for problem_folder in difficulty_path.iterdir():
            if problem_folder.is_dir():
                removed = remove_ques_files(problem_folder)
                stats['ques_removed'] += len(removed)
    
    # Print summary
    print(f"\n{'='*80}")
    print("SUMMARY REPORT")
    print(f"{'='*80}\n")
    print(f"Total problems processed: {stats['total_processed']}")
    print(f"  ✅ main.txt created: {stats['created']}")
    print(f"  ⏭️  Skipped (already exists): {stats['skipped']}")
    print(f"  ❌ Failed: {stats['failed']}")
    print(f"  🗑️  ques.txt files removed: {stats['ques_removed']}")
    print(f"\n{'='*80}")
    print("✨ Standardization complete!")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
