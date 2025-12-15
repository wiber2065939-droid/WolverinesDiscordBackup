#!/usr/bin/env python3
"""
Discord Export Renamer
----------------------
Strips the channel ID from DiscordChatExporter JSON filenames.

DiscordChatExporter format:
  Wolverines Official - Category Name - channel-name [1234567890123456789].json
                                                     ^----- Channel ID -----^

This script renames to:
  Wolverines Official - Category Name - channel-name.json

Usage:
  python rename_exports.py [directory]
  
If no directory specified, uses current directory.

The script will:
1. Find all .json files matching the pattern
2. Show you what will be renamed
3. Ask for confirmation before renaming
"""

import os
import re
import sys

def get_new_filename(filename):
    """
    Strip the channel ID from the filename.
    Pattern: space[numbers].json at the end
    Example: Wolverines Official - Family-Council - council-voting [650388552785592341].json
    """
    # Match the pattern: space[numbers].json
    pattern = r' \[\d+\]\.json$'
    if re.search(pattern, filename):
        return re.sub(pattern, '.json', filename)
    return None

def main():
    # Get directory from args or use current
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        sys.exit(1)
    
    # Find files to rename
    files_to_rename = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            new_name = get_new_filename(filename)
            if new_name:
                files_to_rename.append((filename, new_name))
    
    if not files_to_rename:
        print("No files found matching the DiscordChatExporter pattern.")
        print("Expected pattern: *[channel_id].json")
        print("")
        print("Example: 'Wolverines Official - Stock Market - stock-talk [940999329613754429].json'")
        sys.exit(0)
    
    # Show what will be renamed
    print(f"Found {len(files_to_rename)} file(s) to rename:\n")
    for old, new in files_to_rename[:10]:  # Show first 10
        print(f"  {old}")
        print(f"  -> {new}\n")
    
    if len(files_to_rename) > 10:
        print(f"  ... and {len(files_to_rename) - 10} more files\n")
    
    # Ask for confirmation
    response = input("Proceed with renaming? (y/N): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    # Rename files
    renamed = 0
    skipped = 0
    for old, new in files_to_rename:
        old_path = os.path.join(directory, old)
        new_path = os.path.join(directory, new)
        
        if os.path.exists(new_path):
            print(f"  Skipped (already exists): {new}")
            skipped += 1
        else:
            os.rename(old_path, new_path)
            print(f"  Renamed: {old} -> {new}")
            renamed += 1
    
    print(f"\nDone! Renamed: {renamed}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
