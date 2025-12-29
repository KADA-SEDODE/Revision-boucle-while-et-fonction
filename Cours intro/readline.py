f = open("voitures.txt" , "r")

# LECTURE  LIGNE  ITERATIVEMENT
while True : 
    s = f.readline()
    if s!="":
        print(s,end = "")
    else :
        break     
f.close()    