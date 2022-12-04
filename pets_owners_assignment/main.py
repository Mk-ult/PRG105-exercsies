import sqlite3

def main():
    db = sqlite3.connect('pets.db')
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT
                   NULL, OwnerName TEXT, OwnerPhone TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL,
                   PetName TEXT, PetType TEXT, PetBreed TEXT, OwnerID INTEGER, FOREIGN KEY (OwnerID)
                   REFERENCES Owners(OwnerID))""") 
    
    owners_file = open('Owners.txt', 'r')
    pets_file = open('Pets.txt', 'r')
    for line in owners_file:
        data = line.split(',')
        cursor.execute("INSERT INTO Owners VALUES(?,?,?)", (None, data[0], data[1]))
    for line in pets_file:
        data = line.split(',')
        cursor.execute("INSERT INTO Pets VALUES(?,?,?,?,?)", (None, data[0], data[1], data[2], data[3]))
        
    db.commit()   
    
    cursor.execute("SELECT * FROM Owners") 
    owners = cursor.fetchall()
    print(f"Owner Name: {owners[1]}, Phone: {owners[2]}")
    cursor.execute("SELECT * FROM Pets WHERE OwnerID=?", (owners[0],))
    
    for pet in cursor.fetchall(): 
        print(f"--Pet Name: {pet[1]}, Type: {pet[2]}, Breed: {pet[3]}") 
        print()
    db.close()
main()