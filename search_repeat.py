import random
def search_seed(s_p,k):
    #获取随机的种子序列
    max_start=len(s_p)-k
    start_position = random.randint(0, max_start)
    return s_p[start_position:start_position+k]

def search_repeat(seed,s_p):
    l=len(s_p)
    k=len(seed)
    result = []
    for i in range(l-k+1):
        if s_p[i:i+k] == seed:
            result.append(i)
    return result
def extend_seq(seed,i):
    pass

seq=['A','C','G','G','A','C','G','T','A','C','G','T']
seed=search_seed(seq,3)
print(seed)
repeat=search_repeat(seed,seq)
print(repeat)
