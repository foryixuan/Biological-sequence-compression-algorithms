import random
from copy import deepcopy
def search_seed(s_p,k,record_file):
    #获取随机的种子序列
    max_start=len(s_p)-k
    start_position = random.randint(0, max_start)
    seed=s_p[start_position:start_position+k]
    l=len(s_p)
    k=len(seed)
    result = []
    for i in range(l-k+1):
        if s_p[i:i+k] == seed:
            result.append(i)
    if len(result)==1:
        return search_seed(s_p,k,record_file)
    with open(record_file,'a')as file:
        file.write('Repeat Direction')
        file.write(str(tuple(result))+'\n')
    return seed,result


def extend_seq(seq,seed,repeat,k,record_file,mis_num):
    #对序列进行扩展
    newseq=deepcopy(seq)
    q=0
    for i in range(1,len(repeat)):
        extend_seq=[]
        
        mismatch=[]
        mis_count=0
        seed_start=repeat[0]
        repeat_start=repeat[i]
        seed_end=repeat[0]+k
        repeat_end=repeat[i]+k
        while mis_count<=mis_num and seed_start>0 and repeat_start >0:
             seed_start=seed_start-1
             repeat_start=repeat_start-1
        #向左扩展
             if seq[repeat_start]!=seq[seed_start]:
                 mis_count=mis_count+1
                 if seq[repeat_start]=='A':
                      que='00'
                 elif seq[repeat_start]=='C':
                      que='01'
                 elif seq[repeat_start]=='G':
                      que='10'
                 elif seq[repeat_start]=='T':
                      que='11'
                 
                 mismatch.append(repeat_start)
                 mismatch.append(que)
                 
                 
                 
            #向右扩展
        while mis_count<=mis_num and mis_count>2 and repeat_end<=(len(seq)):
             seed_end=seed_end+1
             repeat_end=repeat_end+1
             if repeat_end==(len(seq)):
                  break
             if seq[repeat_end]!=seq[seed_end]:
                 mis_count=mis_count+1
                 if seq[repeat_end]=='A':
                      que='00'
                 elif seq[repeat_end]=='C':
                      que='01'
                 elif seq[repeat_end]=='G':
                      que='10'
                 elif seq[repeat_end]=='T':
                      que='11' 
                 mismatch.append(repeat_end)
                 mismatch.append(que)
        length=repeat_end-repeat_start+1
        for i in range(repeat_start,repeat_end):
             newseq[i]=''
        for i in range(seed_start,seed_end+1):  
             extend_seq.append(seq[i])
        
        if mismatch:
                with open(record_file,'a')as file:
                    extend_seq=''.join(extend_seq)
                    file.write('miss'+'\t'+str(q)+'\n')
                    file.write(extend_seq+'\t')
                    file.write(str(tuple(mismatch))+'\t')
                    file.write(str(length)+'\n')
                    file.write('\n')
                    q=q+1
        
        for i in range(seed_start,seed_end+1):
             newseq[i]=''
    return newseq
       
        

     
seq=list('ATCTGTCAATATTCACACATAAACGTACGTAGGGGTTTATGTCATTAATTCGTAAGCAACTTTTGAGGTTGACACGTACGTGTACGTTTTGCATATAGATGGATAACCTAACCTATAATTCAAGAACGTACGTGTGACATCCGAGACGCACGTACGTACTTTAATAGCGTTATCAACGTACGTACGTACGTACGTACGTTTCATGCCCTATTCTTTAGATCGCCTCCATAAATAACGTACGTTAAACTCTAGTGTTACGTACGTTTAGTGACTTACCTAATGGTTTCCCTACCACTGAGACTATGTTGCCACGTACGTAGTCATAATAGCCTTATTAGTGCTACGTTTCTGCGCATCCTCACGTACGTATGATCGGCCTCTCACTCATTAATCCGGGGGATAACGTCAAACTTGGAACAGTACTGGTTGTTAGGGCAGTTCAGAGCTTGAATATCTTGTCAACCTCTCTATGGAAACAGGATTATTCAGTATAGAG')
#输入序列
seed,repeat=search_seed(seq,8,'/Users/yixuanli/Desktop/compress/record.txt')
new=extend_seq(seq,seed,repeat,8,'/Users/yixuanli/Desktop/compress/record.txt',3)
#mismatch阈值未log2(8)=3
new=''.join(new)
#new为最终解析的序列