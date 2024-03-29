import shutil
import os
import zipfile
import pytest


@pytest.fixture(scope="session", autouse=True)
def test_create_file():
    os.chdir('resources')
    with (zipfile.ZipFile('arch.zip', 'w') as arch):
        arch.write('AByteofPythonRussian-2.02.pdf')
        arch.write('Excel.xlsx')
        arch.write('sample-heavy-1.xls')
        arch.write('text.txt')

    if not os.path.isdir('../tmp'):
        os.mkdir('../tmp')
    shutil.move('arch.zip', os.path.join('../tmp', 'arch.zip'))
    yield
