import random
import string

stations=[
    'Shyambazar',
    'Bakkhali',
    'Mandarmani',
    'Bandel',
    'Murshidabad',
    'Howrah',
    'Purulia',
    'Asansol',
    'Siliguri',
    'Kharagpur'
]
routes={}

for i in range(10):
    for j in range(10):
        if i==j:
            continue
        else:
            n=random.randint(1,3)
            l=[]
            for k in range(n):
                a=random.randint(1,99)
                b=random.choice(string.ascii_uppercase)
                c=random.choice(string.ascii_uppercase)
                l.append(str(a)+b+'/'+c)
            routes[stations[i]+'-'+stations[j]]=l

print(routes)
print(len(routes))
            
