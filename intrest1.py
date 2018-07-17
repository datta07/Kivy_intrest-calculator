import time
def time1(p,date,month,year,no):
            a=list(map(int,p.split('-')))
            b=[int(date),int(month),int(year)]
            c=[]
            for k in range(0,3):
                  c.append(a[k]-b[k])
            c[2]=12*c[2]  
            c[2]=c[2]+c[1] 
            if (c[0]<0):
                  c[2]-=1
                  c[0]+=30  
            s= str(c[2])+' months & '+str(c[0])+' days'
            if (no==1):
                 return s  
            c[0]=float(c[0])
            if c[0]==0 :
                return c[2]-1
            return c[2]+(c[0]/30)
def intrest(p,t,i):
            p=int(p)
            t1=t//6
            t1=t1*6
            t2=t%6
            t=0
            while (t<t1):
                      p=p*(1+i*6)
                      t=t+6
            p=p*(1+(i*(t2)))
            return str(p)+'/-'
def intrest1(p,t,i):
            p=int(p)
            p=p*(1+(i*t))
            return str(p)+'/-'