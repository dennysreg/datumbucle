def comb(a, i, k, candidates, result):
    if i == k:
        result.append(a[:k])
        return
    for j in range(len(candidates)):
        item=candidates[j]
        if item not in a[:i]:
            a[i]=item
            comb(a,i+1,k, candidates, result)


if __name__ == '__main__':
    candidates=list('152')
    k=2
    r=[]
    a=[0]*k
    comb(a,0,k,candidates,r)
    print(len(r),r)
