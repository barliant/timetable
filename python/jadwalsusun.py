''' jadwalsusun.py

Membaca data jadwal kuliah dalam berkas excel.

Anung B. Ariwibowo
barliant@gmail.com
20130206
'''

import xlrd
import sqlite3


def main():
  bacafile()


def bacafile():
  book = xlrd.open_workbook('jadwal-susun.xls')

  print "The number of worksheet is", book.nsheets
  print "Worksheet name(s):", book.sheet_names()

  for sh_idx in range(book.nsheets):
    sh = book.sheet_by_index(sh_idx)

  sh = book.sheet_by_index(0)
  print "Name\tRows\tCols"
  msg = sh.name + "\t" + str(sh.nrows) + "\t" + str(sh.ncols)
  print msg

  # get field names
  print '-- field names --'
  f_names = []
  for idx in range(sh.ncols):
    f_names.append(sh.cell_value(rowx=0, colx=idx))
  print f_names

  # get field types
  print '-- field types --'
  f_types = []
  for idx in range(sh.ncols):
    if sh.cell_type(rowx=1, colx=idx) == 1:
      f_types.append('TEXT')
    elif sh.cell_type(rowx=1, colx=idx) == 2:
      f_types.append('NUMBER')
    else:
      type_name = 'OTHER: ' + str(sh.cell_type(rowx=1, colx=idx))
      f_types.append(type_name)
  print f_types

  list_day = []
  for idx_row in range(1, sh.nrows):
    if sh.cell_value(rowx=idx_row, colx=3) not in list_day:
      list_day.append(sh.cell_value(rowx=idx_row, colx=3))
  print list_day

  for idx_row in range(1, 5):
    for idx_col in range(sh.ncols):
      print sh.cell_value(rowx=idx_row, colx=idx_col),
    print

  '''
  for rx in range(sh.nrows):
    print type(sh.row(rx)), sh.row(rx)
  '''

  print "Cell A2 is", sh.cell(rowx=1, colx=0)
  print "Cell A2's value is", sh.cell_value(rowx=1, colx=0)
  print "Cell A2's type is", sh.cell_type(rowx=1, colx=0)
  print "Cell D2's type is", sh.cell_type(rowx=1, colx=3)


if __name__ == '__main__':
  main()

