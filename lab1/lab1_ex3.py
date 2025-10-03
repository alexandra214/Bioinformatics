from collections import Counter

def read_fasta(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    if not lines:
        raise ValueError("File is empty!")
    
    description = lines[0].strip()
    sequence = "".join(line.strip() for line in lines[1:])
    
    return description, sequence


def analyze_sequence(sequence):
    alphabet = {'A':0, 'G':0, 'C':0, 'T':0}
    total = 0
    for letter in sequence:
        if (letter in alphabet):
            alphabet[letter] += 1
            total += 1

    print("Sequence length:", total)
    print(alphabet)

    for item in alphabet:
        freq = (alphabet[item] / total) * 100
        print('The relative frequency of ' + item + ' is ' + str(freq) + '%')


if __name__ == "__main__":
    fasta_file = "lab1/influenza.fna"
    
    description, sequence = read_fasta(fasta_file)
    analyze_sequence(sequence)
    
