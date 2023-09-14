# Создать отдельный файл для негативных тестов.
# Функцию проверки вынести в отдельную библиотеку.
# Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки (e)

from checks import checkout_negative
import pytest


folderin = '/home/user/test'
folderout = '/home/user/out'
folderext = '/home/user/folder1'


def test_step1():
    assert checkout_negative(f'cd {folderout}; 7z e arh1.7z -o{folderext}', 'ERROR'), 'test_step1 FAIL'

# def test_step2():
#     assert checkout(f'cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL'

# #
def test_step3():
    assert checkout(f'cd {folderext}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test_step2 FAIL'



if __name__ == '__main__':
    pytest.main(['-vv'])

