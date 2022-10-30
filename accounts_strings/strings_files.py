# compare the contents of two files and display customer information only for those customers whose accounts are overdue
# Read the files into two separate lists
# Print the complete customer information on the screen if the customer number is found in the overdue accounts list.
# Do error checking for file names to make sure the files exist (try and except statements.)

def main():
    total_accounts = open("accounts.txt", "r")
    account_lines = total_accounts.readlines()
    total_accounts.close()
    
    overdue_accounts = open("over90.txt", "r")
    overdue_lines = overdue_accounts.readlines()
    overdue_accounts.close()
    
    overdue_list = []
    
    for line in overdue_lines:
        line = line.strip("\n")
        acc_id = line.split()
        overdue_id = acc_id[0]
        overdue_list.append(overdue_id)
    
    account_list = []
    account_addresses = []
    
    for line in account_lines:
        line = line.strip("\n")
        address = line.split(",")
        account_id = address[0]
        account_addresses.append(address)
        if account_id in overdue_list:
            account_list.append(address)
    
    for line in account_list:
        print(*line, sep=",")

main()