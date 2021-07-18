import csv , math
with open("Data1.csv",newline='')as file:
    print(file)
    file_data = csv.reader(file)
    print(file_data) 
    data = list(file_data)
    print(data)
fullData = data[0]
print(fullData)
n = len(fullData)
print(n)
sum = 0
print(sum)
for i in fullData:
    print(i)
    sum += int(i)
    print(sum)
mean = sum/n
print(mean)
square_list = []
print(square_list)
for i in fullData:
    print(i)
    dif = int(i)-mean
    print(dif)
    sq = dif*dif
    print(sq)
    square_list.append(sq)
    print(square_list)
sum1 = 0
print(sum1)
for i in square_list:
    print(i)
    sum1 += int(square_list)
    print(sum1)
sum2 = sum1/(n-1)
print(sum2)
st_diveation = math.sqrt(sum2)
print(st_diveation)