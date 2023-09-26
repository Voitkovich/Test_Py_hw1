# Задание 1.

# Условие:
# Дополнить проект фикстурой, которая после каждого 
# шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, 
# статистика загрузки процессора из файла /proc/loadavg 
# (можно писать просто всё содержимое этого файла).

# Задание 2. (дополнительное задание)

# Дополнить все тесты ключом команды 7z -t (тип архива).
# Вынести этот параметр в конфиг.
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


def write_stat(file_path, info):
    with open(file_path, 'a') as file:
        file.write(info + '\n')


def test_fixture(tmp_path):
 
    stat_file = tmp_path / "stat.txt"
    stat_file.touch()

    test_step1()
    write_stat(stat_file, "time1, files1, size1, stat1")

    test_step2()
    write_stat(stat_file, "time2, files2, size2, stat2")

    test_step3()
    write_stat(stat_file, "time3, files3, size3, stat3")

    test_step4()
    write_stat(stat_file, "time4, files4, size4, stat4")

    test_step5()
    write_stat(stat_file, "time5, files5, size5, stat5")
