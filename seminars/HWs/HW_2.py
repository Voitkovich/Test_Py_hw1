"""Задание 1.
Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
и разархивирования с путями (x)."""
import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


folderin = '/home/user/folder1'
folderout = '/home/user/out'
folderext = '/home/user/folder'


def test_step1():
    # test1
    assert checkout(f"cd	{folderext};	7z	a	{folderout}", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout(f"cd	{folderout};	7z	e	arx2.7z	-o/{folderin} -y",
                    "Everything is Ok"), "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd	{folderout};	7z	t	arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "Name\n----"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {folderout}; 7z x arx2.7z -o{folderin} -y", "Everything is Ok"), "test5 FAIL"
