import sqlite3

def main():
    my_db = None
    try:
        my_db = sqlite3.connect('coffee.db')
        my_cursor = my_db.cursor()
        table_structure = """CREATE TABLE IF NOT EXISTS Coffee
                        (ProductID INTEGER PRIMARY KEY NOT NULL,
                        Product TEXT, Category TEXT, Supplier TEXT)"""
        my_cursor.execute(table_structure)
        my_db.commit()
        
        try:
            data_file = open("coffeehouse_supplies.csv", "r")
            count = 0
            for line in data_file:
                data = line.strip().split(",")
                my_cursor.execute("""INSERT INTO Coffee (Product, Category, Supplier)
                                  VALUES (?, ?, ?)""", (data[0], data[1], data[2]))
                count += 1
            print(f"{count} records added to the database.")
            data_file.close()
            my_db.commit()
        except IndexError:
            print("%Error: Datafile is not in the correct format")
        except IOError:
            print("%Error: Unable to add data to the database")
        except sqlite3.Error:
            print("%SQL error encountered.")
    
    except sqlite3.Error:
        print("%Error: Unable to connect to the database")
    finally:
        if my_db is not None:
            my_db.close()   
main() 