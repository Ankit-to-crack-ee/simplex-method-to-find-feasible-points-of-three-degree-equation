import numpy as np
def zi(ci,l1,n):
    cf=[]
    cr=[]
    for i in range(2*n):
        sum=0
        for j in range(n):
            x=ci[j]*l1[j][i]
            sum=sum+x
        cf.append(sum)
    for i in range(2*n):
        cr.append(cf[i]-cb[i])
    print('zi-cf:',cr)
    return cr
def minratio(s,l1,n,ind):
    row=[]
    for i in range(n):
        ratio=9999999
        if l1[i][ind]>0:
            ratio=s[i]/l1[i][ind]
        row.append(ratio)
        minimum=min(row)
        minr=row.index(minimum)
    return minr
def soln(l1,s,index,ind,n):
    num=l1[index][ind]
    if num!=0:
           s[index]=s[index]/num
    for i in range(n-1,index,-1):
        num=l1[i][ind]
        s[i]=s[i]-num*s[index]
    for i in range(0,index):
        num=l1[i][ind]
        s[i]=s[i]-num*s[index]
    return s
def unitmat(l1,index,ind,n):
    num=l1[index][ind]
    for i in range(2*n):
                if num!=0:
                    l1[index][i]=l1[index][i]/num
    for i in range(n-1,index,-1):
        num=l1[i][ind]
        for j in range(2*n):
            
            if (l1[i][j]>=0 and num*l1[index][j]>=0)or(l1[i][j]<=0 and num*l1[index][j]<=0):
                 l=True
            
        for j in range(2*n):
             if l==True:
               l1[i][j]=l1[i][j]-(num*l1[index][j])
             else:
                l1[i][j]=l1[i][j]+(num*l1[index][j])
                
    for i in range(0,index):
        num=l1[i][ind]
        for j in range(2*n):
            
            if (l1[i][j]>=0 and num*l1[index][j]>=0)or (l1[i][j]<=0 and num*l1[index][j]<=0):
                l=True
        for j in range(2*n):
            if l==True:
              l1[i][j]=l1[i][j]-(num*l1[index][j])
            else:
                l1[i][j]=l1[i][j]+(num*l1[index][j])
           
    return l1
def rec(cr,n):
    for i in range(2*n):
        if cr[i]>=0:
          return False
        else:
            return True

def fun(l1,cb,ci,s,count):
    cr=zi(ci,l1,n)
    k=rec(cr,n)
    if k==False:
        print("simplex method reached its optimal solution as no negative in zi-cf")
        for i in range(n):
           if(ci[i]==0):
               s[i]=0
        print('final solution value:',s)
    else:          
       
       piv=min(cr)
       print('min value of zi-cf',piv)
       count+=1
       ind=cr.index(piv)
       print('minratio:',minratio(s,l1,n,ind))
       index=minratio(s,l1,n,ind)
       s=soln(l1,s,index,ind,n)
       l1=unitmat(l1,index,ind,n)
       print('------------------------------------------------------------------')
       l1arr=np.array(l1)
       sarr=np.array(s)
       cbarr=np.array(cb)
       print('new matrix:')
       print(l1arr)
       print('solution value',sarr)
       print('cb:',cbarr)
       ci[index]=cb[ind]
       print(ci)
       fun(l1,cb,ci,s,count)

        
print('enter the no. of unknows 2 or 3')   
n=int(input())
l1=[]
cb=[]
s=[]
if n==3:
    print('enter the coef. of main equation')
    x1=int(input('x1:'))
    x2=int(input('x2:'))
    x3=int(input('x3:'))
    cb.append(x1)
    cb.append(x2)
    cb.append(x3)
    cb.append(0)
    cb.append(0)
    cb.append(0) 
    for i in range(n):
        l=[]
        x1=int(input('coef.of x1:'))
        x2=int(input('coef.of x2:'))
        x3=int(input('coef.of x3:'))
        c=int(input('soln.value:'))
        l.append(x1)
        l.append(x2)
        l.append(x3)
        s.append(c)
        l1.append(l)

for i in range(n):
        for j in range(n):
              if j==i:
                   l1[i].append(1)
              else:
                   l1[i].append(0)
l1arr=np.array(l1)
sarr=np.array(s)
cbarr=np.array(cb)
print('matrix:')
print(l1arr)
print('solution value',sarr)
print('cb:',cbarr)
 
ci=[]
for i in range(n):
    ci.append(cb[n+i])
print(ci)
count=0
fun(l1,cb,ci,s,count)




                   
        
    
    
