# Code to determine the Top Scorer from a csv file/text file
# Author : Lutendo Mulaisi
# Date   : 19/09/2023
# Version: 2
import sys

def read_csv_from_input():
    """Read CSV data from standard input."""
    try:
        csv_data = sys.stdin.read().strip()
        if not csv_data:
            raise ValueError("Input file data is empty.")
        return csv_data
    except Exception as e:
        print(f"Error reading CSV data: {e}")
        sys.exit(1)

def parse_csv(csv_data):
    """Parse CSV data into a list of dictionaries."""
    try:
        lines = csv_data.split('\n')
        if len(lines) < 2:
            raise ValueError("CSV data must have at least one header and one data row.")
        
        headers = lines[0].split(',')
        data = []

        for line in lines[1:]:
            values = line.split(',')
            if len(values) != len(headers):
                raise ValueError("CSV data has inconsistent columns.")
            row_dict = {headers[i]: values[i] for i in range(len(headers))}
            data.append(row_dict)

        return headers, data
    except Exception as e:
        print(f"Error parsing CSV data: {e}")
        sys.exit(1)

def find_top_scorers(data):
    """Find indices of top scorers in the CSV data."""
    scores = [person['Score'] for person in data]
    max_score = max(scores)
    top_scorers_indices = [i for i, score in enumerate(scores) if score == max_score]
    return top_scorers_indices

def sort_data_alphabetically(data):
    """Sort data alphabetically based on 'First Name' and 'Second Name'."""
    return sorted(data, key=lambda x: (x['First Name'], x['Second Name']))

def display_person_info(person):
    """Display the name of a person."""
    print(f"{person['First Name']} {person['Second Name']}")
    

def main():
    csv_data = read_csv_from_input()
    headers, data = parse_csv(csv_data)
    
    top_scorers_indices = find_top_scorers(data)
    top_scorers = [data[i] for i in top_scorers_indices]
    
    sorted_top_scorers = sort_data_alphabetically(top_scorers)
    
    for person in sorted_top_scorers:
        display_person_info(person)
    print(f"Score: {sorted_top_scorers[0]['Score']}")
if __name__ == "__main__":
    main()
