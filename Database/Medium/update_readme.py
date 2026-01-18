import os

def parse_main_txt(txt_content):
    lines = txt_content.split('\n')
    
    table_schema = []
    problem_desc = []
    input_example = []
    output_example = []
    
    # Identify the start of the example section
    example_start_idx = len(lines)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('Example 1:') or stripped.startswith('Input:'):
            example_start_idx = i
            break
            
    pre_example_lines = lines[:example_start_idx]
    example_lines = lines[example_start_idx:]
    
    # In pre-example text, identify tables
    for line in pre_example_lines:
        stripped = line.strip()
        # Filter out the unwanted sentence
        if stripped.lower().rstrip('.') == 'the result format is in the following example':
            continue
            
        if stripped.startswith('Table:') or stripped.startswith('+') or stripped.startswith('|'):
            table_schema.append(line)
        elif stripped == '' and table_schema and (table_schema[-1].strip().startswith('+') or table_schema[-1].strip().startswith('|')):
            table_schema.append(line)
        elif stripped != '':
            problem_desc.append(line)

    # Simple example parsing
    current_section = 'input'
    for line in example_lines:
        stripped = line.strip()
        # Skip Example headings
        if stripped.lower().startswith('example'):
            continue
            
        if stripped.startswith('Input:'):
            current_section = 'input'
            continue
        elif stripped.startswith('Output:'):
            current_section = 'output'
            continue
        
        if current_section == 'input':
            input_example.append(line)
        elif current_section == 'output':
            # Stop if Explanation is found
            if stripped.lower().startswith('explanation:'):
                current_section = 'skip'
                continue
            output_example.append(line)

    return {
        'schema': '\n'.join(table_schema).strip(),
        'problem': '\n'.join(problem_desc).strip(),
        'input': '\n'.join(input_example).strip(),
        'output': '\n'.join(output_example).strip()
    }

def generate_readme():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(base_dir, 'README.md')
    
    header = """## Database | Medium 

This readme file contains solved SQL problems from LeetCode,from the Medium category.

Each problem includes:

- ✅ Table Schema
- ✅ Problem Description
- ✅ Input example
- ✅ Correct SQL solution
- ✅ Output example

---
"""
    
    sections = []
    
    # Get all subdirectories, sorted
    dirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    
    for d in dirs:
        problem_dir = os.path.join(base_dir, d)
        txt_file = os.path.join(problem_dir, 'main.txt')
        sql_file = os.path.join(problem_dir, 'main.sql')
        
        if os.path.exists(txt_file) and os.path.exists(sql_file):
            with open(txt_file, 'r') as f:
                txt_content = f.read()
            with open(sql_file, 'r') as f:
                sql_content = f.read().strip()
            
            parsed = parse_main_txt(txt_content)
            
            section = f"""
### <div align="center">{d}</div>

> Table 

```text
{parsed['schema']}
```

> Problem 

{parsed['problem']}

> Input Example

```text
{parsed['input']}
```

> SQL Query **Solution**

```sql
{sql_content}
```

> Output Example

```text
{parsed['output']}
```

---
"""
            sections.append(section)
            
    with open(readme_path, 'w') as f:
        f.write(header + '\n'.join(sections))

if __name__ == "__main__":
    generate_readme()
