def main():
    students = {
    'Alice':85,
    'Bob':90,
    'Charlie':94,
    'Diana':80,
    'Eve':81
    }
    #find the student name with the lowest Alphabetic order
    student_with_min_grade = min(students)
    print(student_with_min_grade)
    #find sudent with lowest grade
    # το παρακάτω τρέχει αλλά το κανω comment out γιατι εμφανίζεται να εχει error
    #student_with_min_grade = min(students, key=students.get)
    print(student_with_min_grade)

    #find student with shortest name length
    student_with_sortest_name = min(students, key=len)
    print(student_with_sortest_name)


if __name__ == "__main__":
    main()