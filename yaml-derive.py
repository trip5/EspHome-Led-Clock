#!/usr/bin/env python3

# YAML-DERIVE 2026.01.23
#
# Command line:
#     python yaml-derive.py input.yaml "label" [output.yaml]
#
# Example:
#     python yaml-derive.py EHLClock-HA.yaml "303 Clock" EHLC-303-HA.yaml
#
# The script will search the input file looking for lines like...
#
# Sinilink XY-Clock: Keep next x lines... this will count next x lines below and delete them (because not part of the current label)
# 303 Clock: Uncomment next x lines.. this will count next x lines below and remove the '#' character if it is in the first column
# 303 Clock: Delete next x lines.. this will count next x lines below and delete them
#
# The first column MUST be a # to be considered as a command
# The characters between # and : are considered as a label
# when counting x, lines are counted absolutely - this includes blank lines or lines that don't get processed
#
# commands used before committing to the repository:
#
# python yaml-derive.py EHLClock.yaml "303 Clock" EHLClock-303.yaml
# python yaml-derive.py EHLClock-HA.yaml "303 Clock" EHLClock-303-HA.yaml

import sys
import re
import os

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: yaml-derive input.yaml 'Label' [output.yaml]")
        sys.exit(1)

    input_file = sys.argv[1]
    label = sys.argv[2].strip()
    base, ext = os.path.splitext(input_file)
    if ext.lower() not in ['.yaml', '.yml']:
        print("Input file must be .yaml or .yml")
        sys.exit(1)
    if len(sys.argv) == 4:
        output_file = sys.argv[3]
    else:
        output_file = f"{base}-{label}{ext}"

    # Regex to match command comments
    cmd_re = re.compile(r'^#\s*([^:]+):\s*(Keep|Delete|Uncomment)\s+next\s+(\d+)\s+line', re.IGNORECASE)

    with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
        # Write header line and blank line
        input_base = os.path.basename(input_file)
        fout.write(f"# Derived from {input_base} with yaml-derive.py for {label} - this file is not the master file\n\n")
        lines = fin.readlines()
        i = 0
        commands_processed = 0
        lines_deleted = 0
        lines_uncommented = 0
        while i < len(lines):
            line = lines[i]
            m = cmd_re.match(line)
            if m:
                found_label = m.group(1).strip()
                action = m.group(2).lower()
                count = int(m.group(3))
                # Only process if # is in column 1
                if line.startswith('#'):
                    # For Keep: if label does NOT match, delete next N lines
                    if action == 'keep' and found_label.lower() != label.lower():
                        commands_processed += 1
                        lines_deleted += count
                        i += 1 + count
                        continue
                    # For Delete: if label matches, delete next N lines
                    elif action == 'delete' and found_label.lower() == label.lower():
                        commands_processed += 1
                        # fout.write(line)  # Write the command line itself
                        lines_deleted += count
                        i += 1 + count
                        continue
                    # For Uncomment: if label matches, uncomment next N lines
                    elif action == 'uncomment' and found_label.lower() == label.lower():
                        commands_processed += 1
                        for j in range(1, count+1):
                            if i+j < len(lines):
                                l2 = lines[i+j]
                                if l2.startswith('#'):
                                    fout.write(l2[1:])  # Remove leading #
                                    lines_uncommented += 1
                                else:
                                    fout.write(l2)
                        i += count + 1
                        continue
            # Default: write line
            fout.write(line)
            i += 1
    # Print summary
    output_base = os.path.basename(output_file)
    print(f"yaml-derive: {output_base} derived from {input_base} - processed {commands_processed} commands, deleted {lines_deleted} lines, uncommented {lines_uncommented} lines (and added 2-line comment at top).")

if __name__ == '__main__':
    main()
