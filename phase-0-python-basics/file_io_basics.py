"""
FILE I/O DEMONSTRATION PROGRAM (WITH PRACTICAL SCENARIOS)

This program demonstrates real-world file operations:

1. Creating a file
2. Writing data
3. Appending new records
4. Reading full file
5. Reading line by line
6. Searching inside a file
7. Deleting a file

Think of this as a small "Student Record System".
"""

import os   # OS module helps interact with the operating system (delete files, check existence)

# Name of the file that will store student data
FILE_NAME = "student_records.txt"


# ---------------------------------------------------
# 1. CREATE FILE AND WRITE INITIAL DATA
# ---------------------------------------------------

def create_file():
    """
    Situation:
    A college admin is creating the first database of student records.
    The system must generate the file and insert initial data.

    Mode "w" = write mode
    - If file doesn't exist → create it
    - If file exists → overwrite everything
    """

    with open(FILE_NAME, "w") as file:
        # Writing initial student data in CSV format
        file.write("101,Rahul,Computer Science\n")
        file.write("102,Sneha,Mechanical\n")
        file.write("103,Amit,Electronics\n")

    print("File created and initial records written.\n")


# ---------------------------------------------------
# 2. APPEND DATA TO FILE
# ---------------------------------------------------

def add_student(student_id, name, department):
    """
    Situation:
    A new student enrolls in the college.
    Instead of rewriting the whole file, we just append the new record.

    Mode "a" = append mode
    - Keeps existing data safe
    - Adds new data at the end
    """

    with open(FILE_NAME, "a") as file:
        record = f"{student_id},{name},{department}\n"
        file.write(record)

    print(f"Student {name} added successfully.\n")


# ---------------------------------------------------
# 3. READ ENTIRE FILE
# ---------------------------------------------------

def read_all_records():
    """
    Situation:
    The admin wants to see the entire student database.

    read() loads the whole file content into memory.
    This works for small files but is dangerous for huge datasets.
    """

    if not os.path.exists(FILE_NAME):
        print("File does not exist.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.read()

    print("Full File Content:\n")
    print(data)


# ---------------------------------------------------
# 4. READ FILE LINE BY LINE
# ---------------------------------------------------

def read_line_by_line():
    """
    Situation:
    The admin wants to process each record individually.

    Reading line-by-line is better for large files
    because it doesn't load the entire file into memory.
    """

    if not os.path.exists(FILE_NAME):
        print("File does not exist.\n")
        return

    print("Reading file line by line:\n")

    with open(FILE_NAME, "r") as file:

        for line in file:

            # Remove newline characters
            clean_line = line.strip()

            # Split CSV record into fields
            student_id, name, department = clean_line.split(",")

            # Print formatted output
            print("Student ID:", student_id)
            print("Name:", name)
            print("Department:", department)
            print("---------------------")


# ---------------------------------------------------
# 5. SEARCH FOR A STUDENT
# ---------------------------------------------------

def search_student(name_to_search):
    """
    Situation:
    Admin wants to find a student by name.

    This function scans the file line by line
    and compares names.
    """

    if not os.path.exists(FILE_NAME):
        print("File does not exist.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:

        for line in file:

            # Extract fields
            student_id, name, department = line.strip().split(",")

            # Compare names (case-insensitive search)
            if name.lower() == name_to_search.lower():
                print("Student Found:")
                print("ID:", student_id)
                print("Name:", name)
                print("Department:", department)
                print()
                found = True

    if not found:
        print("Student not found.\n")


# ---------------------------------------------------
# 6. DELETE FILE
# ---------------------------------------------------

def delete_file():
    """
    Situation:
    Suppose the system is being reset or data is no longer needed.

    os.remove() deletes the file permanently.
    """

    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("File deleted successfully.\n")
    else:
        print("File does not exist.\n")


# ---------------------------------------------------
# MAIN PROGRAM EXECUTION
# ---------------------------------------------------

if __name__ == "__main__":

    print("\n--- FILE I/O DEMONSTRATION ---\n")

    # Step 1: Create file
    create_file()

    # Step 2: Add new students
    add_student(104, "Priya", "Civil")
    add_student(105, "Arjun", "Information Technology")

    # Step 3: Read full file
    read_all_records()

    # Step 4: Read line by line
    read_line_by_line()

    # Step 5: Search a student
    search_student("Priya")

    # Step 6: Delete file (dangerous operation)
    delete_file()


# ---------------------------------------------------
# SITUATIONAL QUESTIONS AND ANSWERS
# ---------------------------------------------------

"""
Q1: When should we use 'w' mode?

Answer:
Use 'w' when you want to completely rewrite the file.
Example:
Generating a fresh report every day.

---------------------------------------------------

Q2: When should we use 'a' mode?

Answer:
Use 'a' when you want to preserve old data and add new entries.

Example:
Log files
User activity tracking
Student registrations

---------------------------------------------------

Q3: Why read files line-by-line instead of read()?

Answer:
Because large files may consume huge memory.

Example:
Processing a 5GB log file.

---------------------------------------------------

Q4: Why check os.path.exists() before reading?

Answer:
If the file does not exist, Python throws FileNotFoundError.

Checking existence prevents program crashes.

---------------------------------------------------

Q5: Why store records in CSV format?

Answer:
Because CSV is easy to:
- read
- parse
- import into spreadsheets
- import into databases
"""a