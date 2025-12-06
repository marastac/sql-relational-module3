import sqlite3

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

DB_NAME = "students.db"


def create_connection():
    """
    Create and return a connection to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)


def initialize_database():
    """
    Create the students table if it does not already exist.
    This function is called once at the beginning of the program.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL,
                grade REAL NOT NULL
            );
            """
        )
        conn.commit()


# -------------------------------------------------------
# CRUD operations (Create, Read, Update, Delete)
# -------------------------------------------------------

def add_student(name: str, age: int, email: str, grade: float) -> None:
    """
    Insert a new student record into the database.
    This demonstrates an INSERT statement.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, age, email, grade) VALUES (?, ?, ?, ?)",
            (name, age, email, grade),
        )
        conn.commit()


def update_student_grade(student_id: int, new_grade: float) -> None:
    """
    Update the grade of an existing student.
    This demonstrates an UPDATE statement.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE students SET grade = ? WHERE id = ?",
            (new_grade, student_id),
        )
        conn.commit()


def delete_student(student_id: int) -> None:
    """
    Delete a student record from the database.
    This demonstrates a DELETE statement.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()


def fetch_all_students():
    """
    Retrieve all student records from the database.
    This demonstrates a SELECT statement.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, email, grade FROM students ORDER BY id")
        return cur.fetchall()


def fetch_student_by_id(student_id: int):
    """
    Retrieve a single student by id, or None if it does not exist.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, name, age, email, grade FROM students WHERE id = ?",
            (student_id,),
        )
        return cur.fetchone()


# -------------------------------------------------------
# Aggregate functions (COUNT and AVG)
# -------------------------------------------------------

def get_student_count() -> int:
    """
    Return the total number of students.
    Uses the COUNT aggregate function.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM students")
        (count,) = cur.fetchone()
        return count


def get_average_grade() -> float:
    """
    Return the average grade of all students.
    Uses the AVG aggregate function.
    """
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT AVG(grade) FROM students")
        (avg,) = cur.fetchone()
        return avg if avg is not None else 0.0


# -------------------------------------------------------
# Helper to print results
# -------------------------------------------------------

def print_students_table(rows) -> None:
    """
    Pretty-print a list of student records to the console.
    """
    if not rows:
        print("\nNo students found.\n")
        return

    print("\nID  | Name                 | Age | Email                     | Grade")
    print("-" * 70)
    for student_id, name, age, email, grade in rows:
        print(f"{student_id:<3} | {name:<20} | {age:<3} | {email:<25} | {grade:>5.2f}")
    print()


# -------------------------------------------------------
# Text menu (user interface)
# -------------------------------------------------------

def menu() -> None:
    """
    Display a simple text menu and handle user choices.
    """
    while True:
        print("\n=== Student Database Menu ===")
        print("1. Add new student")
        print("2. Show all students")
        print("3. Update student grade")
        print("4. Delete student")
        print("5. Show statistics (COUNT and AVG)")
        print("6. Find student by ID")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            # Create (INSERT)
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            email = input("Email: ").strip()
            grade = float(input("Grade (0-20 or 0-100, you decide): ").strip())
            add_student(name, age, email, grade)
            print("Student added successfully.")

        elif choice == "2":
            # Read (SELECT all)
            rows = fetch_all_students()
            print_students_table(rows)

        elif choice == "3":
            # Update (UPDATE)
            student_id = int(input("Enter the student ID to update: ").strip())
            new_grade = float(input("New grade: ").strip())
            if fetch_student_by_id(student_id) is None:
                print("No student found with that ID.")
            else:
                update_student_grade(student_id, new_grade)
                print("Grade updated successfully.")

        elif choice == "4":
            # Delete (DELETE)
            student_id = int(input("Enter the student ID to delete: ").strip())
            if fetch_student_by_id(student_id) is None:
                print("No student found with that ID.")
            else:
                delete_student(student_id)
                print("Student deleted successfully.")

        elif choice == "5":
            # Aggregate functions (COUNT and AVG)
            count = get_student_count()
            avg = get_average_grade()
            print(f"\nTotal number of students: {count}")
            print(f"Average grade: {avg:.2f}\n")

        elif choice == "6":
            # Search by ID
            student_id = int(input("Enter the student ID to search: ").strip())
            row = fetch_student_by_id(student_id)
            if row is None:
                print("No student found with that ID.")
            else:
                print_students_table([row])

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 7.")


# -------------------------------------------------------
# Main entry point
# -------------------------------------------------------

def main() -> None:
    """
    Entry point of the program.
    Initializes the database and starts the menu.
    """
    print("Initializing database...")
    initialize_database()
    menu()


if __name__ == "__main__":
    main()
