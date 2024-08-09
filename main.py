import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Введіть ім'я студента")
        age = int(input("Введіть ім'я"))
        major = input("Введіть спеціальність студента")

        cursor.execute('INSERT INTO students (name, age, major) VALUSES ?, ?, ?',(name, age, major))
        conn.commit()

    elif choice == "2":
        course = input("Введіть назву курсу")
        instructor = input("Введіть ім'я викладача")
        cursor.execute('INSERT INTO courses (course, instructor) VALUSES ?, ?',(course, instructor))

    elif choice == "3":
        cursor.execute(''' SELECT * FROM students''')
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("False")
     
    elif choice == "4":
        cursor.execute(''' SELECT * FROM courses''')
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("False")

    elif choice == "5":
        course_id = int(input("Введіть ID курсу"))
        student_id = int(input("Введіть ім'я викладача"))
        cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUSES ?, ?',(student_id, course_id))

    elif choice == "6":
        course_id = int(input("Введіть ID курсу"))

        query = '''
            SELECT * FROM students, student_courses
            WHERE student_courses.course_id==?
            AND students.id == student_courses.student_id:
        '''
        cursor.execute(query, (course_id))

        result = cursor.fetchall()
        if result:
            print(result)
        else: 
            print("Таблиця порожня")
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")


conn.close()
cursor.close()