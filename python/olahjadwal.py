''' olahjadwal.py

Mengolah data jadwal kesediaan mengajar dari spreadsheet di Google
Drive.

Anung B. Ariwibowo (barliant@gmail.com)
20130127
http://goo.gl/4EiC5

20130207 def interaktif()
'''

__author__ = 'Anung B. Ariwibowo'


import getpass
import gspread


def main():
  username = interaktif('Username [barliant@gmail.com]: ')
  passwd = getpass.getpass()
  doc_name = interaktif('Spreadsheet name [KesediaanMengajar-2013-2014-1]: ')
  doc_name = contain_space(doc_name)
  sudah_mengisi = process(username, passwd, doc_name)
  csv_dosen = interaktif('Data dosen [namaDosen.csv]: ')
  daftar_dosen = db_dosen(csv_dosen)
  belum_mengisi(daftar_dosen, sudah_mengisi)
  susun_jadwal(username, passwd, doc_name)


def interaktif(mesg):
  ignore, defanswer = mesg.split('[')
  defanswer, ignore = defanswer.split(']')
  answer = raw_input(mesg)
  if len(answer) == 0:
    answer = defanswer
  return answer


def db_dosen(csv_dosen):
  dosen = open(csv_dosen)
  data_dosen = dosen.readlines()
  dict_dosen = {}
  for idx in range(1, len(data_dosen)):
    data = data_dosen[idx]
    (nik, nama) = data.split(' - ')
    dict_dosen[nik] = nama
  dosen.close()
  return dict_dosen


def belum_mengisi(db, daftar):
  for nik in db.iterkeys():
    if nik not in daftar:
      print nik, db[nik]


def process(username, passwd, doc_name):
  print 'Logging in ...'
  gc = gspread.login(username, passwd)
  print 'Opening spreadsheet ...'
  wks = gc.open(doc_name).sheet1
  print 'Retrieving Dosen ...'
  lecturers = wks.col_values(2)
  list_nik = []
  for idx in range(1,len(lecturers)):
    dosen = lecturers[idx]
    (nik, nama) = dosen.split(' - ')
    print nik, nama
    list_nik.append(nik)

  '''
  print 'Retrieving all data ...'
  matrix = wks.get_all_values()
  for row in matrix:
    for item in row:
      print item
    print '---'
  '''

  return list_nik


def contain_space(word):
  flag = False
  result = word
  for letter in word:
    if letter == ' ' or letter == '\t':
      flag = True
  if flag:
    result = '"' + word + '"'
  return result


def susun_jadwal(user, pwd, doc):
  print 'Logging in ...'
  gc = gspread.login(username, passwd)
  print 'Opening spreadsheet ...'
  wks = gc.open(doc_name).sheet1

  lecturers = wks.col_values(2)
  course1 = wks.col_values(6)
  course2 = wks.col_values(7)
  course3 = wks.col_values(8)
  course4 = wks.col_values(9)
  day_sen = wks.col_values(10)
  day_sel = wks.col_values(11)
  day_rab = wks.col_values(12)
  day_kam = wks.col_values(13)
  day_jum = wks.col_values(14)
  day_sab = wks.col_values(15)

  for idx in range(1,len(lecturers)):
    dosen = lecturers[idx]
    (nik, nama) = dosen.split(' - ')
    kode1, kuliah1 = courses1.split(' - ')
    kode2, kuliah2 = courses2.split(' - ')
    kode3, kuliah3 = courses3.split(' - ')
    kode4, kuliah4 = courses4.split(' - ')
    senin = olah_waktu(day_sen)
    print nik, nama


def olah_waktu(daftar):
  list_pilihan = daftar.split(',')
  list_waktu = []
  for item in list_pilihan:
    mulai, selesai = item.split(' - ')
    waktu_mulai = peta_waktu(mulai)
    list_waktu.append(waktu_mulai)


def peta_waktu(pukul):
  jam, menit = pukul.split('.')
  angka = ( ( int(jam) * 60 + int(menit) ) - 400 ) / 50
  return angka


if __name__ == '__main__':
  main()

