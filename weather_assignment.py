# Part 1 
import json

with open ("precipitation.json") as file:
    data = json.load(file) 

rainfall_per_month=[0]*12

for measurement in data:
    if measurement["station"]=="GHCND:US1WAKG0038":
        value=measurement["value"]
        month=int(measurement["date"].split("-")[1])        
        rainfall_per_month[month-1]+=value

print(rainfall_per_month)
#Part 2
print(sum(rainfall_per_month))

Annual_Rainfall=sum(rainfall_per_month)
#Part 2.2
percentage= []
for total_per_month in rainfall_per_month:
        percentage.append(total_per_month/Annual_Rainfall)
     
print(percentage)
