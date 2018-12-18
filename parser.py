import requests

print ('____________________________________________________________')

timer = 0
kolvo = 40
d = open('txt.txt')
line = d.readlines()
name_of_file = "1.html"
url = ""


while timer < kolvo:
    timer+=1
    url = line[timer]

    name_of_file = "1" + name_of_file
    r = requests.get(url)
    with open(name_of_file, 'wb') as code:       
        code.write(r.content)

    
    f=open(name_of_file,'r',encoding='utf-8') #
    n = 0
    for s in f:
        i = s.find("SOLD OUT")
        if i > 0:
            n += 1


    if n >= 1:
        
        
        print('SOLD OUT - ', url)
        
    elif n == 0:
        print('Живьом - ', url)


    



f.close()
