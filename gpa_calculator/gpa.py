import re
from collections import defaultdict

# UCSC Grade → Grade Point Mapping
GRADE_POINTS = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}


def parse_results(text):
    """
    Parses pasted UCSC results text and returns:
    {
        year_number: [(credits, grade), ...]
    }
    """
    year_data = defaultdict(list)
    current_year = None

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        # Detect Year headers
        year_match = re.match(r"Year\s+(\d)", line)
        if year_match:
            current_year = int(year_match.group(1))
            continue

        if current_year is None:
            continue

        # Extract credits and grade at end of line
        # Example line:
        # SCS1202 Programming Using C [19] [1] 3 A+
        match = re.search(r"\s(\d+)\s+(A\+|A-|A|B\+|B-|B|C\+|C-|C|D|F)\s*$", line)

        if match:
            credits = int(match.group(1))
            grade = match.group(2)

            if credits > 0:
                year_data[current_year].append((credits, grade))

    return year_data


def calculate_gpa(subjects):
    total_credits = 0
    weighted_sum = 0.0

    for credits, grade in subjects:
        gp = GRADE_POINTS.get(grade)
        if gp is not None:
            total_credits += credits
            weighted_sum += credits * gp

    if total_credits == 0:
        return 0.0, 0

    return round(weighted_sum / total_credits, 3), total_credits


def main():
    print("UCSC GPA Calculator (Paste Results Mode)")
    print("======================================")
    print("Paste your UCSC results below.")
    print("Type 'END' on a new line when finished.\n")

    pasted_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        pasted_lines.append(line)

    pasted_text = "\n".join(pasted_lines)

    year_data = parse_results(pasted_text)

    if not year_data:
        print("\nNo valid subjects found. Please check the pasted format.")
        return

    print("\n--- GPA Summary ---")
    all_subjects = []

    for year in sorted(year_data.keys()):
        gpa, credits = calculate_gpa(year_data[year])
        print(f"Year {year}: GPA = {gpa} | Credits = {credits}")
        all_subjects.extend(year_data[year])

    overall_gpa, total_credits = calculate_gpa(all_subjects)
    print("\nCumulative GPA")
    print(f"GPA = {overall_gpa} | Total Credits = {total_credits}")


if __name__ == "__main__":
    main()
