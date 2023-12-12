import json
import csv

def json_to_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)

        if isinstance(data, list):
            keys = data[0].keys()
        else:
            keys = data.keys()

        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            
            writer.writeheader()

            if isinstance(data, list):
                writer.writerows(data)
            else:
                writer.writerow(data)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    input_file_name = "input.json"
    output_file_name = "output.csv"

    json_to_csv(input_file_name, output_file_name)
