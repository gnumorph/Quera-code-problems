#https://quera.org/problemset/20256

jadval=input().strip()
#to know number of each color
red=jadval.count("R")
yello=jadval.count("Y")
green=jadval.count("G")

if red>=3 or (red>=2 and yello>=2) or green==0:
    print("nakhor lite")
else:
    print("rahat baash")

