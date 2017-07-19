## 2. Opening Files ##

a = open("test.txt", "r")
print(a)

f = open ("crime_rates.csv","r")

## 3. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(data)

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
#print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
#print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows[0:5])

## 6. Practice - Loops ##

ten_rows = rows[0:10]

for row in ten_rows:
    print(row)
    # row_splitted = row.split(",") 
    # print(row_splitted[0] + " : " + row_splitted[1])




## 7. List of Lists ##

three_rows = ["Albuquerque,749,123", "Anaheim,371,123", "Anchorage,828,123"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    
    print("row: "+row)
    print("split_list: " + str(split_list))
    final_list.append(split_list)
print("final_list: ")
print(final_list)
print(final_list[0][1])
print(final_list[1])
print(final_list[2])

## 8. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows[0:5])

final_data = []

for row in rows:
    final_data.append(row.split(","))
    
print(final_data[0:5])




## 9. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)

cities_list = []

for element in five_elements:
    cities_list.append(element[0])

    

## 10. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = []

for element in final_data:
    cities_list.append(element[0])
    
    

## 11. Challenge ##

f = open("crime_rates.csv", "r")
data = f.read()
rows = data.split("\n")
print(rows)

int_crime_rates = []
for row in rows:
    row_splitted = row.split(",")
    int_crime_rates.append(int(row_splitted[1]))

print(int_crime_rates)






