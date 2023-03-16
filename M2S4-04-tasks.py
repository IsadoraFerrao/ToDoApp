import sqlite3
conexao = sqlite3.connect('todo-db')
cursor = conexao.cursor()


cursor.execute('''CREATE TABLE if not exists TODO (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR (50) UNIQUE,
    date VARCHAR (10),
    status VARCHAR (10),
    category_id INT NOT NULL,
        PRIMARY KEY (id)
        FOREIGN KEY (category_id) REFERENCES category(id)
);''')

cursor.execute('''CREATE TABLE if not exists CATEGORY (
    id INT AUTO_INCREMENT  NOT NULL,
    name VARCHAR (50),
        PRIMARY KEY (id)
);''')


print('-' * 30)
print('-=-= TASKS =-=-')
print('1 - Create task\n2 - Update task\n3 - Delete task\n4 - List tasks\n5 - Check task')
print('-' * 30)
print('-=-= CATEGORIES =-=-')
print('6 - Create category\n7 - Update category\n8 - Delete category\n9 - List all categories')
Opt = int(input('Choose your option: '))

while True: 
    if Opt == 1:
        TaskName = str(input('Task name: '))
        TaskDate = str(input('Task date (mm/dd/yyyy):'))
        TaskStatus = str(input('Task status: '))
        TaskCateg = str(input('Task category: '))
        print(f'| {TaskName} \n| {TaskDate} \n| {TaskCateg} \n | {TaskStatus} \n| OK!' )

        data = [TaskName, TaskDate, TaskStatus, TaskCateg]
        sql_insert = 'insert into TODO(name, date, status, category_id) VALUES (?, ?, ?, ?)'
        cursor.execute(sql_insert, data)
        break
    elif Opt == 2:
        UpTask = str(input('Task name to be updated: '))
        break
    elif Opt == 3:
        DelTask = str(input('Task name to be deleted: '))
        break
    elif Opt == 4:
        print('1 - List all tasks\n2 - List by date')
        OptTasks = int(input('Choose option: '))
        if OptTasks == 1:
            print('All tasks:')
        elif OptTasks == 2:
            print('Tasks for date dd/mm/yyyy:')
        break
    elif Opt == 5:
        CheckTask = str(input('Task name to be checked: '))
        break
    elif Opt == 6:
        CreateCateg = str(input('New category name: '))
        break
    elif Opt == 7:
        UpCateg = str(input('Category name to be updated: '))
        break
    elif Opt == 8:
        DelCateg = str(input('Category name to be deleted: '))
        break
    elif Opt == 9:
        print('All categories:')
        break
    else:
        Opt = int(input('Invalid option! Try again: '))
        print('-' * 5)


conexao.commit()
conexao.close
