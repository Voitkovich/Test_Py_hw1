# Написать функцию на Python, которой передаются в качестве 
# параметров команда и текст. Функция должна возвращать True, 
# если команда успешно выполнена и текст найден в её выводе и 
# False в противном случае. Передаваться должна только одна 
# строка, разбиение вывода использовать не нужно.
import subprocess

def check_command_output(command, text):
    try:
        output = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        return text in output
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

    command = "cd"
    text = "jammy"
    result = check_command_output(command, text)
    print(result)
