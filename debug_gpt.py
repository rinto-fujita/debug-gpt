import subprocess     
def read_file(file_name):
    with open(file_name,"r") as file:
        content = file.read()
        content = int(content)
        return content

def write_file(file_name):
    with open(file_name , 'w') as file:
        file.write('0')

def debug_file():
    content = read_file("num.txt")
    if content == 0:
        with open("num.txt", "w") as file:
            file.write("1")
        subprocess.run(["python3", "make_message.py"])
    else:
        write_file('num.txt')

def quit_code():
    stop_code = read_file("final.txt")
    if stop_code == 1:
        write_file('final.txt')
        quit()


debug_file()
quit_code()