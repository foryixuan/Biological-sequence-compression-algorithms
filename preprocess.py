def preprocess(sequence,output):
    sequence=[x.upper() for x in sequence]
    standard=['A','C','G','T']
    newsequence=[]
    for i in range(len(sequence)):
        if sequence[i] not in standard:
            with open (output,'a')as f:
                f.write(str(i)+'\t'+str(sequence[i])+'\n')
        else:
            newsequence.append(sequence[i])
    return newsequence