''' labpyxl.py

Eksperimen membaca data dari file Excel.

Anung B. Ariwibowo (barliant@gmail.com)
20141230

* 20141230
  * Studi kasus pada penjadwalan Semester Pendek PPHB Gasal
    2014/2015.
Source:
* pip install reportlab
* http://www.devshed.com/c/a/python/python-for-pdf-generation/ 
* http://www.reportlab.com/opensource/
'''

__author__ = 'Anung B. Ariwibowo'

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

import networkx as nx
import matplotlib.pyplot as plt
import xlrd

import getpass
import gspread


def main():
    '''
    pdf = Canvas("labtest.pdf")
    pdf.setFont("Courier", 12)
    pdf.setFillColorRGB(0, 1, 1)
    pdf.drawString(2.5*cm, 3*cm, "This is a test.")
    pdf.drawCentredString(A4[0]/2, 5*cm, "CLASSIFIED")
    '''

    style = getSampleStyleSheet()
    pdf = SimpleDocTemplate("labtest.pdf", pagesize = A4)
    story = []

    pdf.showPage()
    pdf.save()
    exit()

    wb = xlrd.open_workbook('../raw-data/2014-2015-3.xls')
    print wb.sheet_names()
    sheet = wb.sheet_by_index(0)
    print "name: ", sheet.name
    print "rows: ", sheet.nrows
    print "cols: ", sheet.ncols
    for nrow in range(0, sheet.nrows):
        for ncol in range(0, sheet.ncols):
            cell = sheet.cell(nrow, ncol)
            print cell.value,
        print
    krs = {}
    for nrow in range(1, sheet.nrows):
        nim_cell = sheet.cell(nrow, 0)
        kode_cell = sheet.cell(nrow, 1)
        nim = nim_cell.value
        kode = kode_cell.value
        if krs.has_key(nim):
            krs[nim].append(kode)
        else:
            krs[nim] = [kode]
    for nim in krs:
        print nim,
        for kode in krs[nim]:
            print kode,
        if len(krs[nim]) > 1:
            for kode in krs[nim]:
                for other in krs[nim]:
                    if kode != other:
                        print "(", kode, other, ")",
        print


def coloring():
    G = nx.Graph()
    edge_list = [('IKH313', 'IKL335'), #06409002
        # 06412014
        ('IKH351', 'IUM461a'), ('IKH351', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06413018
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06508009
        ('IKH323', 'IKB411a'), ('IKH323', 'IKB411b'), ('IKB411a', 'IKB411b'),
        # 06509012
        ('IKH309', 'IKH323'),
        # 06509023
        ('IKH309', 'IKB411a'), ('IKH309', 'IKB411b'), ('IKB411a', 'IKB411b'),
        # 06509025
        ('IKH323', 'IKB411a'), ('IKH323', 'IKB411b'), ('IKB411a', 'IKB411b'),
        # 06510013
        ('IKH323', 'IKL335'),
        # 06510015
        ('IKB405a', 'IKB405b'),
        # 06512006
        ('IKH351', 'IKS323'),
        # 06512007
        ('IKH351', 'IKS323'),
        # 06513001
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06513006
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06513010
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06513012
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        # 06514020
        ('IKL341', 'IUM461a'), ('IKL341', 'IUM461b'), ('IUM461a', 'IUM461b'),
        ]
    G.add_edges_from(edge_list)
    print "Edges  : ", G.edges()
    print "Degrees: ", nx.degree(G)
    print sorted(nx.degree(G).values())
    color_list = []
    for key, value in sorted(nx.degree(G).iteritems(), key=lambda(k, v): (v, k), reverse=True):
        print key, value, sorted(G.neighbors(key))
        color_list.append(key)
    for lecture in color_list:
        G.node[lecture]['color'] = 0
    current_color = 1
    for lecture in color_list:
        if G.node[lecture]['color'] == 0:
            G.node[lecture]['color'] = current_color
            for neighbor in color_list:
                if G.node[neighbor]['color'] == 0:
                    can = True
                    for adjacent in G.neighbors(neighbor):
                        if G.node[adjacent]['color'] == current_color and G.node[adjacent]['color'] != 0:
                            can = False
                    if can:
                        G.node[neighbor]['color'] = current_color
            current_color = current_color + 1
    print "Chromatic number: ", current_color-1
    for lecture in color_list:
        print lecture, G.node[lecture]['color']
    #nx.draw_networkx(G, pos=nx.spring_layout(G))
    #nx.draw_networkx(G, pos=nx.spectral_layout(G))
    nx.draw_networkx(G, pos=nx.circular_layout(G))
    plt.show()



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

