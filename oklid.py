import math
def euclideanDistance(nokta1,nokta2):
    return math.sqrt((nokta2[0]-nokta1[0])**2+(nokta2[1]-nokta1[1])**2)



noktalar=[(25,150),(250,33),(10,5),(15,17),(350,40)]

mesafeler=[]
for i in range(len(noktalar)):
    for j in range (i+1,len(noktalar)):
        mesafe=euclideanDistance(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)
        
minimum_mesafe=min(mesafeler)
print("Minimum mesafe:",minimum_mesafe)

