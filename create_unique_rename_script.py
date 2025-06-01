#!/usr/bin/env python3
"""
Create a safe renaming script that ensures unique filenames for all workflows.
This script fixes the filename collision issue by adding numeric suffixes.
"""

import json
import os
from collections import defaultdict

def create_unique_filenames():
    """Create unique filenames by adding suffixes to duplicates"""
    
    # Load the analysis data
    with open('enhanced_workflow_analysis.json', 'r') as f:
        data = json.load(f)
    
    # Track filename usage to add suffixes for duplicates
    filename_counts = defaultdict(int)
    filename_mapping = {}
    
    # First pass: count all suggested filenames
    suggested_filenames = []
    for workflow in data['workflows']:
        suggested_filenames.append(workflow['suggested_filename'])
    
    # Count occurrences
    from collections import Counter
    name_counter = Counter(suggested_filenames)
    
    # Second pass: assign unique names with suffixes
    filename_usage = defaultdict(int)
    
    for workflow in data['workflows']:
        original_filename = workflow['original_filename']
        suggested_filename = workflow['suggested_filename']
        
        # If this filename has duplicates, add a suffix
        if name_counter[suggested_filename] > 1:
            filename_usage[suggested_filename] += 1
            # Add numeric suffix (starting with 1, not 0)
            base_name, ext = os.path.splitext(suggested_filename)
            unique_filename = f"{base_name}_{filename_usage[suggested_filename]}{ext}"
        else:
            unique_filename = suggested_filename
        
        filename_mapping[original_filename] = unique_filename
    
    return filename_mapping

def create_rename_script():
    """Create a bash script with unique filename mappings"""
    
    print("Creating unique filename mappings...")
    filename_mapping = create_unique_filenames()
    
    # Verify uniqueness
    unique_targets = set(filename_mapping.values())
    total_mappings = len(filename_mapping)
    
    print(f"Total workflows: {total_mappings}")
    print(f"Unique target filenames: {len(unique_targets)}")
    
    if len(unique_targets) != total_mappings:
        print("ERROR: Still have duplicate filenames!")
        return False
    
    # Create the rename script
    script_content = """#!/bin/bash

# Safe workflow renaming script with collision prevention
# Generated to ensure unique filenames for all 2,050 workflows

set -e  # Exit on any error

echo "Starting safe workflow renaming..."
echo "Total workflows to rename: """ + str(total_mappings) + """"

WORKFLOW_DIR="workflows"
BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"

# Create backup
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory: $BACKUP_DIR"
    cp -r "$WORKFLOW_DIR" "$BACKUP_DIR"
    echo "Backup created successfully"
fi

cd "$WORKFLOW_DIR" || exit 1

renamed_count=0
skipped_count=0

"""

    # Add individual rename commands
    for original_filename, new_filename in sorted(filename_mapping.items()):
        # Escape filenames for bash
        original_escaped = original_filename.replace("'", "'\"'\"'")
        new_escaped = new_filename.replace("'", "'\"'\"'")
        
        script_content += f"""
# Rename: {original_filename} -> {new_filename}
if [ -f '{original_escaped}' ]; then
    if [ ! -f '{new_escaped}' ]; then
        mv '{original_escaped}' '{new_escaped}'
        ((renamed_count++))
        echo "Renamed: {original_filename} -> {new_filename}"
    else
        echo "SKIPPED (target exists): {original_filename} -> {new_filename}"
        ((skipped_count++))
    fi
else
    echo "NOT FOUND: {original_filename}"
    ((skipped_count++))
fi"""

    script_content += """

echo ""
echo "Renaming completed!"
echo "Files renamed: $renamed_count"
echo "Files skipped: $skipped_count"

# Verify final count
final_count=$(ls -1 | wc -l)
echo "Final file count: $final_count"

if [ "$final_count" -eq """ + str(total_mappings) + """ ]; then
    echo "SUCCESS: All files preserved!"
else
    echo "WARNING: File count mismatch! Expected """ + str(total_mappings) + """, found $final_count"
fi
"""

    # Write the script
    with open('rename_workflows_safe.sh', 'w') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod('rename_workflows_safe.sh', 0o755)
    
    print("Safe rename script created: rename_workflows_safe.sh")
    print("✅ All filenames are now unique!")
    
    return True

def create_filename_report():
    """Create a detailed report of the filename changes"""
    
    filename_mapping = create_unique_filenames()
    
    # Count how many files got suffixes
    suffixed_count = 0
    for fname in filename_mapping.values():
        base_without_ext = fname.replace('.json', '')
        if '_' in base_without_ext:
            parts = base_without_ext.split('_')
            if parts[-1].isdigit():
                suffixed_count += 1
    
    report = f"""# Filename Collision Resolution Report

## Summary
- Total workflows: {len(filename_mapping)}
- Unique target filenames: {len(set(filename_mapping.values()))}
- Files requiring suffixes: {suffixed_count}
- Files with original names: {len(filename_mapping) - suffixed_count}

## Resolution Strategy
- Original suggested filenames are preserved when unique
- Duplicate filenames get numeric suffixes (_1, _2, _3, etc.)
- All 2,050 workflows will have unique target filenames
- No data loss will occur during renaming

## Examples of Resolved Duplicates
"""

    # Find examples of duplicates that got resolved
    from collections import defaultdict
    base_names = defaultdict(list)
    
    for original, target in filename_mapping.items():
        # Extract base name without suffix
        base_name = target
        if '_' in target.replace('.json', '') and target.replace('.json', '').split('_')[-1].isdigit():
            parts = target.replace('.json', '').split('_')
            if parts[-1].isdigit():
                base_name = '_'.join(parts[:-1]) + '.json'
        
        base_names[base_name].append((original, target))
    
    # Show examples of resolved duplicates
    example_count = 0
    for base_name, files in base_names.items():
        if len(files) > 1 and example_count < 5:
            report += f"\n### Base: {base_name}\n"
            for original, target in files:
                report += f"- {original} → {target}\n"
            example_count += 1
    
    with open('filename_collision_report.md', 'w') as f:
        f.write(report)
    
    print("Collision resolution report created: filename_collision_report.md")

if __name__ == "__main__":
    print("🔧 Creating safe workflow renaming solution...")
    
    if create_rename_script():
        create_filename_report()
        print("\n✅ Solution completed successfully!")
        print("📁 Files created:")
        print("  - rename_workflows_safe.sh (executable script)")
        print("  - filename_collision_report.md (detailed report)")
        print("\n⚠️  Next steps:")
        print("  1. Review the report to understand changes")
        print("  2. Test the script on a small subset if desired")
        print("  3. Run ./rename_workflows_safe.sh when ready")
    else:
        print("❌ Failed to create safe renaming solution")