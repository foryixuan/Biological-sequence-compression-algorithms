# 输入DNA序列
input_sequence = "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCGCGC"

# 子段选择：从输入序列中选择长度为8的子段s
def seq_compress(input_sequence,n,m):   
    segments = [input_sequence[i:i+n] for i in range(len(input_sequence)-n+1)]

    # 计算每个子段在输入序列中的出现频率f，并选择m个最频繁出现的子段
    i=1
    most_common_segments = []
    while i<=m:
      frequencies = {}
      for segment in segments:
         if segment not in most_common_segments:
             frequency = input_sequence.count(segment)
             #计算压缩比
             l=len(input_sequence)
             PCR_s=((frequency*8+n*8)/(frequency*n*8))*100
             PCR_b=((frequency*n*2)/(frequency*n*8))*100
            #压缩决策
             if PCR_s<PCR_b:
                 frequencies[segment]=frequency
                 i=i+1
                 most_common = max(frequencies, key=frequencies.get)
                 most_common_segments.append(most_common)
                 print('s',PCR_s)
                 print('b',PCR_b)
                
             else:
                 break
    return frequencies

def code(frequencies,m):
    with open ('/Users/yixuanli/Desktop/compress/codetable.txt','a')as f:
        keys=list(frequencies.keys())
        value=list(frequencies.values())
        for i in range(0,m):
            f.write(f'{i}\t{keys[i]}\n')
        
def subsititute(sequences):
    with open('/Users/yixuanli/Desktop/compress/codetable.txt','r')as file:
        data=file.readlines()
        strings=[]
        indices=[]
        for line in data:
            index,seq=line.split()
            strings.append(seq)
            indices.append(int(index))
        
        for index, string in zip(indices, strings):
            sequence = sequences.replace(string, str(index))
            print(sequence)
            return(sequence)
    
sequences=seq_compress(input_sequence,8,1)
code(sequences,1)
new=subsititute(input_sequence)