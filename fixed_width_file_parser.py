import csv

def read_spec(spec_file):
    with open(spec_file, 'r', encoding='utf-8') as file:
        spec = file.readlines()
    fields = []
    lengths = []
    for line in spec:
        name, length = line.strip().split(':')
        fields.append(name)
        lengths.append(int(length))
    return fields, lengths

def parse_fixed_width_file(fixed_width_file, fields, lengths, output_csv_file):
    with open(fixed_width_file, 'r', encoding='utf-8') as infile, open(output_csv_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fields)

        for line in infile:
            start = 0
            row = []
            for length in lengths:
                row.append(line[start:start + length].strip())
                start += length
            writer.writerow(row)

def main():
    spec_file = 'specification.txt'
    fixed_width_file = 'inputdata.txt'
    output_csv_file = 'outputfile.csv'

    fields, lengths = read_spec(spec_file)
    parse_fixed_width_file(fixed_width_file, fields, lengths, output_csv_file)

if __name__ == "__main__":
    main()
