from hashlib import new
import sys, csv

def avg_major(file_name):
    CSV_PATH = f"./{file_name}"
    with open(CSV_PATH, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file, delimiter=",")
        header = next(csv_reader)[1:]
        prepare_data = []
        for h in header:
            prepare_data.append({h: []})

        for row in csv_reader:
            for p in range(len(prepare_data)):
                prepare_data[p][header[p]].append(int(row[p + 1]))

        # TODO
        # Avg of subject
        # High score of subject
        # low score of subject
        for i in ['avg', 'high', 'low']:
            print(i, end="\n")
            for d in prepare_data:
                key = list(d.keys())[0]
                if i == 'avg':
                    output = sum(list(d.values())[0]) / len(list(d.values())[0])
                elif i == 'high':
                    output = max(list(d.values())[0])
                else:
                    output = min(list(d.values())[0])
                print(f"  {key}: {output}")


if __name__ == "__main__":
    avg_major(sys.argv[1])