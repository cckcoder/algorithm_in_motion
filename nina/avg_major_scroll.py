from hashlib import new
import sys, csv

def avg_major(file_name):
    CSV_PATH = f"./{file_name}"
    with open(CSV_PATH, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file, delimiter=",")
        header = next(csv_reader)[1:]
        prepare_data = []
        # TODO
        # Avg of subject
        # High score of subject
        # low score of subject
        for row in csv_reader:
            for i in range(len(header)):
                print(header[i])
                print(row[i + 1])


if __name__ == "__main__":
    avg_major(sys.argv[1])
