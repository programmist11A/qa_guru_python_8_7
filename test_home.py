import zipfile
from PyPDF2 import PdfReader
import xlrd
from openpyxl import load_workbook


def test_txt():
    with zipfile.ZipFile('tmp/arch.zip', 'r') as arch:
        with arch.open('text.txt') as text:
            assert text.read().decode('utf-8') == '1'
