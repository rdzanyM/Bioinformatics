import numpy as np
def make_alignment(s1, s2, match, mismatch, gap):
    s = np.zeros((len(s1)+1,len(s2)+1)) # score
    d = np.zeros((len(s1)+1,len(s2)+1), dtype=int) # direction 1=left 2=diag 3=up
    s[0,:] = [i*gap for i in range(0,len(s2)+1)] 
    s[:,0] = [i*gap for i in range(0,len(s1)+1)] 
    d[0,1:],d[1:,0] = 1,3
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            b = s[i-1,j-1] + (match if s1[i-1] == s2[j-1] else mismatch)
            if s[i-1,j] > s[i,j-1]:
                a = s[i-1,j] + gap
                if a > b:
                    s[i,j],d[i,j] = a,3
                    continue
            else:
                a = s[i,j-1] + gap
                if a > b:
                    s[i,j],d[i,j] = a,1
                    continue
            s[i,j],d[i,j] = b,2
    i,j = len(s1),len(s2)
    a1,a2 = [],[]
    while i+j > 0:
        a = d[i,j]
        if a > 1: i-=1; a1.append(s1[i])
        else: a1.append('-')
        if a < 3: j-=1; a2.append(s2[j])
        else: a2.append('-')
    return ''.join(a1[::-1]), ''.join(a2[::-1]), s[-1,-1]