a="Supraisthebestcarintheworldandnoonecandenythat"
b=dict()
for i in a:
    if(i in b):
        b[i] +=1
    else:
        b[i]=1
for k,l in b.items():
    print("{} harfi {} defa geçiyor.".format(k,l))