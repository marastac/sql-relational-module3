Author: Mario Alberto Astonitas Acuña
Course: CSE 310 – Module 3

Overview

For this module I created a small student management system using Python and SQLite.
The program builds a relational database where I can store basic student information and interact with it through a simple menu in the terminal.

The software includes the main SQL operations (insert, update, delete, select) and also uses a couple of aggregate functions to summarize the data.

Project Objectives

This project was designed to meet all the Module 3 requirements:

1. SQL Database Creation

The program creates a file called students.db and builds the students table if it does not already exist.

2. CRUD Operations

The system supports:

Create: Add a new student

Read: Show all students or find one by ID

Update: Change a student’s grade

Delete: Remove a student from the database

3. Aggregate Functions

The project uses:

COUNT() → to know how many students are registered

AVG() → to calculate the average grade

Database Structure

The table contains the following fields:

Column Type Description
id INTEGER (PK) Auto-generated student ID
name TEXT Student’s name
age INTEGER Student’s age
email TEXT (UNIQUE) Student email
grade REAL Student’s grade
How to Run the Program

Make sure Python 3 is installed.

Open a terminal inside the folder that contains the project.

Run the script:

python student_database.py

Use the menu to interact with the system.

Menu Options
Option Description
1 Add a new student
2 Show all students
3 Update a student’s grade
4 Delete a student
5 Show COUNT and AVG statistics
6 Search for a student by ID
7 Exit
What I Learned

While working on this module, I was able to understand:

How SQLite works inside Python

How SQL queries are built and executed

How to organize data using a relational database

How CRUD operations interact with the stored records

The usefulness of aggregate functions like COUNT and AVG

Demo Video

Here is the video demonstrating the program:

https://youtu.be/_yHWI_HTW4s

Final Notes

This project completes the SQL Relational Databases module requirements.
The program works in the terminal, handles all required SQL operations, and keeps the database updated as the user interacts with it.
