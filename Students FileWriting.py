import csv

while True:
    print("Enter 1 to enter a student\nEnter 2 to display students")
    print("Enter 3 quit")

    choice = input('>')
    
    if choice == '1':
        students = open("students.csv","a")
        
        name = input('Enter student name: ')
        age = int( input("Enter student's age: ") )
        gender = input('Enter your gender: ')
        Phone = int( input('Enter your phone number: '))
        Favourite = input('Who is your bestfriend?: ')

        students.write("{0},{1},{2},{3},{4}\n".format(name,age,gender,Phone,Favourite))

        students.close()

    if choice == '2':
        template = "{0:<30}{1:<10}"
        
        print( template.format("Name","Age","gender","Phone number","Favourite Person",) )
        print('-'*30)
        with open("students.csv") as file:
            reader = csv.reader(file)

            for row in reader:
                print( template.format(*row) )
        
        print('-'*30)

    if choice =='3':
         exit()
