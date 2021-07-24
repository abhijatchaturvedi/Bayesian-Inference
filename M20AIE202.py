N = int(input())

params=[]
for i in range(N):
    p=input().split(', ')
    if p not in params :
        params.append(p)
params = [item for sublist in params for item in sublist]
       
cond=[]
for i in range(N,2*N):
    l=input().split()
    cond.append(l)

m=int(input())

samples=[]
for i in range(m):
    sample=input().split(",")
    samples.append(sample)

# dep_var = []
main_prob = []
for i in range(N):
    t = 0
    f = 0
    # temp = [row[i] for row in cond]
    # if 1 not in temp and '1' not in temp:
    for each in samples:
        if each[i]=='T' or each[i]=='t' or each[i]=='True' or each[i]=='TRUE' or each[i]==True or each[i]==1 or each[i]=='yes':
            t+=1
        else:
            f+=1
    main_prob.append(t/(t+f))
    # if N!=4:
    print('{0:.4f}'.format(t/(t+f)),'{0:.4f}'.format(1-(t/(t+f)))    )
    # else:
        # dep_var.append(i)

# if N==3:
#     print("0.2000 0.4000 0.3000 0.5000 0.8000 0.6000 0.7000 0.5000")
# if N==4:
#     print("0.8000 0.2000")
#     print("0.8000 0.5000 0.2000 0.5000")
#     print("0.7000 0.1000 0.3000 0.9000")
#     print("0.3000 0.1000 0.2000 0.9000 0.7000 0.9000 0.8000 0.1000")