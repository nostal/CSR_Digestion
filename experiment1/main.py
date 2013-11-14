import  layout
from nltk.tokenize import sent_tokenize
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter

def txtToCSV(pdf, omit_pages):
    for i, item in enumerate(pdf):
        pages = layout.get_pages(item)
        text = []
        for index, page in enumerate(pages):
            if index+1 not in omit_pages[i]:
                text.append(page)
        text = ''.join(text)
        sents = sent_tokenize(text)
        wb = Workbook()
        ew = ExcelWriter(workbook=wb)
        dest_filename = item.split('.')[0]+'.xlsx'
        ws = wb.worksheets[0]
        for index, line in enumerate(sents):
            ws.cell(row=index, column=0).value = line
        ew.save(filename=dest_filename)

pdf_name_list = ['Coffee Bean International.pdf', 'Starbucks.pdf']
omit_pages_list = [[1, 2, 3, 5, 8, 9, 10, 11], [17]]
txtToCSV(pdf_name_list, omit_pages_list)
