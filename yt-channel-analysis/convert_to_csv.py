import json
import csv

# Load JSON data from a file
with open("videos_list.json", "r") as json_file:
    data = json.load(json_file)

with open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write header (keys of the first dictionary in the JSON array)
    if isinstance(data, list) and len(data) > 0:
        header = ["url", "title", "description", "duration", "thumbnail"]
        # header = data[0].keys()
        csv_writer.writerow(header)

        # Write data rows
        for row in data:
            thumbnail = row["thumbnails"][-1]["url"]
            curr_row_data = [row[i] for i in header if i in row.keys()] + [thumbnail]
            csv_writer.writerow(curr_row_data)
