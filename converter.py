with open("currencyvalue.txt", "r") as f:
    lines = f.readlines()

Currencydict = {}
for line in lines:
    value= line.split("\t")
    Currencydict[value[0]] = value[1]
    
amount = int(input("Enter the amount:\n"))
print("enter the name of currency you want to convert this amount to? available options:\n")

for i in Currencydict:
    print(i)

currency = input("Enter one of these values:\n")


print("INR is equal to:", amount * float(Currencydict[currency]))
          

   

    

