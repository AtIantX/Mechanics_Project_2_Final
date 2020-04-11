import csv


class CSVController:

    @staticmethod
    def write_csv(csv_path, data, header):
        with open(csv_path, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            data.insert(0, header)
            for line in data:
                writer.writerow(line)
