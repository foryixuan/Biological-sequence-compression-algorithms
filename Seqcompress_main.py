def seq_compress(input_sequence, n, m):   
    segments = [input_sequence[i:i+n] for i in range(len(input_sequence)-n+1)]

    # 计算每个子段在输入序列中的出现频率f，并选择m个最频繁出现的子段
    most_common_segments = []
    frequencies = {}
    
    while len(most_common_segments) < m:
        max_frequency = 0
        max_segment = ""
        
        for segment in segments:
            if segment not in most_common_segments:
                frequency = input_sequence.count(segment)
                
                if frequency > max_frequency:
                    max_frequency = frequency
                    max_segment = segment
        
        if max_segment != "":
            
            
            # 计算压缩比
            PCR_s = ((max_frequency * 8 + n * 8) / (max_frequency * n * 8)) * 100
            PCR_b = ((max_frequency * n * 2) / (max_frequency * n * 8)) * 100
            
            if PCR_s < PCR_b:
                most_common_segments.append(max_segment)
                frequencies[max_segment] = max_frequency
                print('s', PCR_s)
                print('b', PCR_b)

        
    return frequencies

def code(frequencies, outputcode):
    with open(outputcode, 'w') as f:
        for index, segment in enumerate(frequencies):
            f.write(f'{index}\t{segment}\n')

def substitute(sequences, outputcode):
    with open(outputcode, 'r') as file:
        data = file.readlines()
        strings = []
        indices = []
        
        for line in data:
            index, seq = line.split()
            strings.append(seq)
            indices.append(int(index))
        
        for index, string in zip(indices, strings):
            sequences = sequences.replace(string, str(index))
            
        return sequences

input_sequence = "ATCTGTCAATATTCACACATAAACGTACGTAGGGGTTTATGTCATTAATTCGTAAGCAACTTTTGAGGTTGACACGTACGTGTACGTTTTGCATATAGATGGATAACCTAACCTATAATTCAAGAACGTACGTGTGACATCCGAGACGCACGTACGTACTTTAATAGCGTTATCAACGTACGTACGTACGTACGTACGTTTCATGCCCTATTCTTTAGATCGCCTCCATAAATAACGTACGTTAAACTCTAGTGTTACGTACGTTTAGTGACTTACCTAATGGTTTCCCTACCACTGAGACTATGTTGCCACGTACGTAGTCATAATAGCCTTATTAGTGCTACGTTTCTGCGCATCCTCACGTACGTATGATCGGCCTCTCACTCATTAATCCGGGGGATAACGTCAAACTTGGAACAGTACTGGTTGTTAGGGCAGTTCAGAGCTTGAATATCTTGTCAACCTCTCTATGGAAACAGGATTATTCAGTATAGAG"
print(len(input_sequence))
sequences = seq_compress(input_sequence, 8, 1)
code(sequences, '/Users/yixuanli/Desktop/compress/code.txt')
new = substitute(input_sequence, '/Users/yixuanli/Desktop/compress/code.txt')
print(new)
print(len(new))