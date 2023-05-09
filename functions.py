FILEPATH = r"C://Users//gostapenko//PycharmProjects//Python_Mega_Course//3_ToDo_Web_App//todos.txt"


def file_read(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def file_rewrite(data, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(data)


def file_add(data, filepath=FILEPATH):
    with open(filepath, 'a+') as file:
        file.write(data)

