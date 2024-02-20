import difflib
import sqlite3

connection = sqlite3.connect('toxic_plants.sqlite')
cursor = connection.cursor()

def find_closest_match(plant_name):
    # Fetch all plant names from the database
    cursor.execute('SELECT name FROM plants')
    plant_names = [row[0] for row in cursor.fetchall()]

    # Find the closest match using difflib
    closest_match = difflib.get_close_matches(plant_name, plant_names, n=1)
    # Check if there is a close match
    if closest_match:

        suggestion = closest_match[0]
        print(f"Did you mean {suggestion}? Y/N")
        Name_Correct = input()
        if Name_Correct.lower() == "y":
            print(f"{suggestion}: Toxic to Cats!")
        else:
            print(f"{plant_name}: Kitty approved")
    else:
        print(f"{plant_name}: Kitty approved")


    return None

def is_safe_for_cat(plant_name):
    cursor.execute('SELECT COUNT(*) FROM plants WHERE name = ?', (plant_name.lower(),))
    count = cursor.fetchone()[0]
    return count == 0

def main():

    print("Enter the name of the houseplant:")
    plant_name = input().strip()

    if is_safe_for_cat(plant_name):
        find_closest_match(plant_name)
    else:
        print(f"{plant_name}: Toxic to Cats!")
    connection.close()

if __name__ == "__main__":
    main()
