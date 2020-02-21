
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', \
              'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    
    empty=[]
    reader=csv.reader(fp)
    
    for i in range(4):
        next(reader, None)
        
    for i in reader:
        if "" not in i:
            empty.append(i)
    return (empty)

def get_totals(L):
    count=0
    for i in L:
        if i[0] == "U.S.":
            us_value = int(i[1].replace(",",""))
            
        else:
            count += int(i[1].replace(",","").strip("<"))
    
    return us_value, count

def get_largest_states(L):
    US_unauthorized = float( L[0][2].strip("%"))
    empty= []
    for i in L[1:]:
        val = float(i[2].strip("%"))
        if val > US_unauthorized:
            empty.append(i[0])
            
    empty.sort()
    return empty

def get_industry_counts(L):
    construction_counter=0
    manufacturing_counter=0
    business_services=0
    leisure_counter=0
    agriculture_counter=0
    for i in L[1:]:
        if i[9]=="Construction":
            construction_counter+=1
        if i[9]=="Manufacturing":
            manufacturing_counter+=1
        if i[9]=="Business services":
            business_services+=1
        if i[9]=="Leisure/hospitality":
            leisure_counter+=1
        if i[9]=="Agriculture":
            agriculture_counter+=1
    lists_= [["Construction",construction_counter],["Manufacturing",\
             manufacturing_counter],["Business services",business_services],\
            ["Leisure/hospitality",leisure_counter],["Agriculture",\
            agriculture_counter]]
    lists_.sort(key=itemgetter(1), reverse = True)
    return lists_


def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()    