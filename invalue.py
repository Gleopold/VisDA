import csv
from datetime import datetime

class CSVDateExtractor:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def extract_dates(self, date_column_name):
        dates = []
        try:
            with open(self.csv_file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    date_str = row.get(date_column_name)
                    if date_str:
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%d')
                            dates.append(date)
                        except ValueError:
                            print(f"Skipping invalid date: {date_str}")
        except FileNotFoundError:
            print(f"File not found: {self.csv_file_path}")

        return dates

if __name__ == "__main__":
    # Replace 'your_data.csv' with the path to your CSV file
    csv_file_path = 'your_data.csv'
    date_column_name = 'date_column_name'  # Replace with the actual column name

    date_extractor = CSVDateExtractor(csv_file_path)
    extracted_dates = date_extractor.extract_dates(date_column_name)

    if extracted_dates:
        print("Dates extracted from CSV:")
        for date in extracted_dates:
            print(date.strftime('%Y-%m-%d'))
    else:
        print("No valid dates found in the CSV.")
