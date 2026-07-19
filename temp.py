temprature = (33.2, 32.5, 34.1, 35.0, 36.2, 37.5, 38.0, 39.1, 40.0, 41.2)
list = 0
for ls in temprature:
    list = list + ls
average = list / len(temprature)
print(average)