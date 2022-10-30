# Import Data from file, turn file into a list
# Check to see if the data is valid, if not valid, indicate to user what the bad data is
# break apart list items into individual components by splitting strings
# split strings on a symbol
# Total and average the data, display formatted results on screen




def main():
    rainfall_list = open("rainfall-totals.txt", "r")
    lines = rainfall_list.readlines()
    rainfall_list.close()
    
    
    total = 0.0
    count = 0
    month = ""
    amount = []
    
    for line in lines:
        line = line.rstrip()
        line = line.split()
        month = line[0]
        count += 1
        # print(month)
        # print(amount)
        
        try: 
            amount = float(line[1])
            total += amount
            
        
        except ValueError:
            
            print("The value for", month, "is", amount)
    print(f"Total rainfall: {total:.2f}")
    print(f"Average rainfall: {total/count:.2f}")
        
        
        
        
        
        
        

main()