# -*- coding: utf-8 -*-
"""day 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GvvUs4_GvNgFl70ZRWgJhhTIpHK7R1oR
"""

def is_safe(report):
    """
    Checks if a given report is safe based on the conditions:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least one and at most three.
    """
    # Calculate differences between adjacent levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are either positive or negative
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def count_safe_reports(filename):
    """
    Reads the reports from the input file and counts how many are safe.
    """
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            # Convert the report to a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe
            if is_safe(report):
                safe_count += 1

    return safe_count


# Replace 'input.txt' with the path to your input file
input_file = "/content/inputday 2.txt"
safe_reports = count_safe_reports(input_file)

print(f"Number of safe reports: {safe_reports}")

def is_safe(report):
    """
    Checks if a given report is safe based on the conditions:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least one and at most three.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    """
    Checks if a report is safe when removing a single level to satisfy the safety conditions.
    """
    for i in range(len(report)):
        # Create a new report by excluding the current level
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports_with_dampener(filename):
    """
    Reads the reports from the input file and counts how many are safe,
    considering the Problem Dampener.
    """
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            # Check if the report is safe or becomes safe with the Problem Dampener
            if is_safe(report) or is_safe_with_dampener(report):
                safe_count += 1

    return safe_count


# Replace 'input.txt' with the path to your input file
input_file = "/content/input day 2 part 2.txt"
safe_reports_with_dampener = count_safe_reports_with_dampener(input_file)

print(f"Number of safe reports with the Problem Dampener: {safe_reports_with_dampener}")