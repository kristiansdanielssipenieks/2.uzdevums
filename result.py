import pandas
get_info=input()  #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

area = 0
for row in info_list:
    if row[1] == get_info: 
        area = row[0] 
        if area == 0:
            print("0"),
            exit
            break
        
geo_file = pandas.read_csv("data.csv")
geo_list = geo_file.values.tolist()
geo_count = 0

for row in geo_list: 
    if row [1] == area:
        geo_count += row[3]
print(geo_count)
exit

    







