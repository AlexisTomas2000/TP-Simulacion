s1=1234
s2=2934
s0=6153
n=10000
numbers=[]
pn=int(abs(s2-s0))
numbers.insert(0,pn)

def fg(na):
    fnn=int(abs(n-(na*1.99)))
    return fnn

for i in range(1,1000):
    numbers.insert(i,fg(numbers[i-1]))