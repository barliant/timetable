''' jadwal.py

Berdasarkan data riwayat kuliah yang telah diambil oleh semua
mahasiswa, cari himpunan mata kuliah yang masih harus diambil
oleh setiap mahasiswa.

Hasilnya adalah mata kuliah yang masih harus ditawarkan,
dengan informasi siapa saja mahasiswa yang kemungkinan besar
menjadi peserta setiap mata kuliah.


Anung B. Ariwibowo (barliant@gmail.com)
20150211

* 20150211
  * Mulai dengan membaca data riwayat pengambilan mata kuliah
  * yang tersimpan dalam berkas Excel. Pembacaan dari berkas
  * Excel dibantu oleh package xlrd.
'''

__author__ = 'Anung B. Ariwibowo'


import xlrd
import xlwt
import numpy as np


def main():
    wb = xlrd.open_workbook('../raw-data/transkrip-aktif-2014-2015-1b.xls')
    wb_out = xlwt.Workbook()
    sheet_out = wb_out.add_sheet('taken')

    print wb.sheet_names()

    sheet = wb.sheet_by_index(0)
    print "name: ", sheet.name
    print "rows: ", sheet.nrows
    print "cols: ", sheet.ncols

    # extra conversion to string required for later use in record array header
    headers = [str(cell.value) for cell in sheet.row(0)]
    print headers
    # get all data except first row
    arr = []
    for rowind in range(sheet.nrows)[1:]:
        arr.append([ cell.value for cell in sheet.row(rowind)])
    data = np.rec.fromrecords(arr, names=headers)

    transkrip = {}
    for nrow in range(1, sheet.nrows-1):
        nilai_kuliah = {}
        nim = str(int(data['NIM'][nrow]))
        kode = data['Kode'][nrow]
        grade = data['Nilai'][nrow]
        status = data['Status'][nrow]
        if status in ['C']:
            nilai_kuliah[kode] = grade
            nilai_transkrip = {}
            if transkrip.has_key(nim):
                nilai_transkrip = transkrip[nim]
                if nilai_transkrip.has_key(kode):
                    nilai = nilai_transkrip[kode]
                    if lebih_baik(grade, nilai):
                        nilai_transkrip[kode] = grade
                else:
                    nilai_transkrip[kode] = grade
            else:
                transkrip[nim] = nilai_kuliah

    sheet_out.write(0, 0, 'NIM')
    sheet_out.write(0, 1, 'Kode')
    sheet_out.write(0, 2, 'Grade')

    rowidx = 1
    colidx = 0
    for student in transkrip:
        for lecture in transkrip[student]:
            grade = transkrip[student][lecture]
            print rowidx, student, lecture, grade
            sheet_out.write(rowidx, colidx+0, student)
            sheet_out.write(rowidx, colidx+1, lecture)
            sheet_out.write(rowidx, colidx+2, grade)
            rowidx = rowidx + 1
    wb_out.save('../raw-data/courses-taken.xls')
    exit()
    '''
        if len(krs[nim]) > 1:
            for kode in krs[nim]:
                for other in krs[nim]:
                    if kode != other:
                        G.add_edge(kode, other)
    '''

    print "Edges  : ", G.edges()
    print "Degrees: ", nx.degree(G)
    color_list = []
    for key, value in sorted(nx.degree(G).iteritems(), key=lambda(k, v): (v, k), reverse=True):
        color_list.append(key)
    for lecture in color_list:
        G.node[lecture]['color'] = 0
    current_color = 1
    print "Chromatic number: ", current_color-1
    for lecture in color_list:
        print lecture, G.node[lecture]['color']
    #nx.draw_networkx(G, pos=nx.spring_layout(G))
    #nx.draw_networkx(G, pos=nx.spectral_layout(G))
    nx.draw_networkx(G, pos=nx.circular_layout(G))
    plt.show()


    kelas = open("../raw-data/kelas.csv", "a")
    RPL = [ 'IUM461', 'IUM263', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IKH323', 'IKH123', 'IKH313',
        'IKH113', 'IKH351', 'IKH151', 'IKH311', 'IKH111',
        'IKL335', 'IKL135', 'IKL341', 'IKL141', 'IKL343',
        'IKS304', 'IKS104', 'IKP213', 'IKP113', 'IKP321',
        'IKS318', 'IKS118', 'IKS323', 'IKS123', 'IKS327',
        'IKS126', 'IKS301', 'IKD313', 'IKD123', 'IKD312',
        'IKD112', 'IKH331', 'IKP103', 'IKP303', 'IKP111',
        'IKP311', 'IKP302', 'IKP102', 'UBA402', 'UKW400',
        'ISM404', 'ISM403', 'IKB250', 'IKS413', 'UKT101',
        'IKB450', 'IKB451', 'IKA301', 'IKH314', 'IKH326',
        'IKP333', 'ISD312', 'ISD313', 'ISD314', 'ISM312',
        'UKT300', 'ISM317' ]
    coreRPL = [ 'IUM461', 'IUM263', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IKH323', 'IKH123', 'IKH313',
        'IKH113', 'IKH351', 'IKH151', 'IKH311', 'IKH111',
        'IKL335', 'IKL135', 'IKL341', 'IKL141', 'IKL343',
        'IKS304', 'IKS104', 'IKP213', 'IKP113', 'IKP321',
        'IKS318', 'IKS118', 'IKS323', 'IKS123', 'IKS327',
        'IKS126', 'IKS301', 'IKD313', 'IKD123', 'IKD312',
        'IKD112', 'IKH331', 'IKP103', 'IKP303', 'IKP111',
        'IKP311', 'IKP302', 'IKP102', 'UBA402', 'UKW400',
        'ISM404', 'ISM403', 'IKB250', 'IKS413', 'UKT101',
        'IKB450', 'IKB451' ]
    GK = [ 'ISM221', 'IUM461', 'IUM263', 'IKB406', 'IKB206',
        'IKB405', 'IKB411', 'ISM401', 'IKH323', 'IKH123',
        'IKH313', 'IKH113', 'IKH351', 'IKH151', 'IKH311',
        'IKH111', 'IKL335', 'IKL135', 'IKL341', 'IKL141',
        'IKS304', 'IKS104', 'IKP321', 'IKS318', 'IKS118',
        'IKS323', 'IKS123', 'IKS327', 'IKS126', 'IKS301',
        'IKD313', 'IKD123', 'IKD312', 'IKD112', 'IKG402',
        'IKG101', 'IKG321', 'IKG121', 'IKG302', 'IKG102',
        'PDU212', 'IKH342', 'IKL233', 'IKL133', 'UBA402',
        'UKW400', 'ISM404', 'ISM403', 'IKB250', 'IKS413',
        'UKT101', 'IKB450', 'IKB451', 'IKA301', 'IKG311',
        'IKH314', 'IKH326', 'IKP333', 'ISD312', 'ISD314',
        'ISM312', 'UKT300', 'IKG304', 'ISD305' ]
    coreGK = [ 'ISM221', 'IUM461', 'IUM263', 'IKB406', 'IKB206',
        'IKB405', 'IKB411', 'ISM401', 'IKH323', 'IKH123',
        'IKH313', 'IKH113', 'IKH351', 'IKH151', 'IKH311',
        'IKH111', 'IKL335', 'IKL135', 'IKL341', 'IKL141',
        'IKS304', 'IKS104', 'IKP321', 'IKS318', 'IKS118',
        'IKS323', 'IKS123', 'IKS327', 'IKS126', 'IKS301',
        'IKD313', 'IKD123', 'IKD312', 'IKD112', 'IKG402',
        'IKG101', 'IKG321', 'IKG121', 'IKG302', 'IKG102',
        'PDU212', 'IKH342', 'IKL233', 'IKL133', 'UBA402',
        'UKW400', 'ISM404', 'ISM403', 'IKB250', 'IKS413',
        'UKT101', 'IKB450', 'IKB451' ]
    KI = [ 'ISM221', 'IUM461', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IUM314', 'IKH323', 'IKH123',
        'IKH313', 'IKH113', 'IKH309', 'IKH132', 'IKH351',
        'IKH151', 'IKH311', 'IKH111', 'IKL335', 'IKL135',
        'IKL341', 'IKL141', 'IKD312', 'IKD112', 'IKH329',
        'IKH109', 'IKH310', 'IKH110', 'IKH312', 'IKH112',
        'IKH314', 'IKH114', 'IKH318', 'IKH118', 'IKH319',
        'IKH119', 'IKH326', 'IKH126', 'IKH327', 'IKH328',
        'IKH128', 'IKH316', 'IKH116', 'IKH324', 'UBA402',
        'UKW400', 'ISM404', 'ISM403', 'IKB250', 'IKS413',
        'UKT101', 'IKB450', 'IKB451', 'IKA301', 'IKG321',
        'IKP333', 'ISD312', 'ISD313', 'IKP321', 'ISM312',
        'ISM314', 'UKT300' ]
    coreKI = [ 'ISM221', 'IUM461', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IUM314', 'IKH323', 'IKH123',
        'IKH313', 'IKH113', 'IKH309', 'IKH132', 'IKH351',
        'IKH151', 'IKH311', 'IKH111', 'IKL335', 'IKL135',
        'IKL341', 'IKL141', 'IKD312', 'IKD112', 'IKH329',
        'IKH109', 'IKH310', 'IKH110', 'IKH312', 'IKH112',
        'IKH314', 'IKH114', 'IKH318', 'IKH118', 'IKH319',
        'IKH119', 'IKH326', 'IKH126', 'IKH327', 'IKH328',
        'IKH128', 'IKH316', 'IKH116', 'IKH324', 'UBA402',
        'UKW400', 'ISM404', 'ISM403', 'IKB250', 'IKS413',
        'UKT101', 'IKB450', 'IKB451' ]
    SI = [ 'ISM221', 'IUM461', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IKH323', 'IKH313', 'IKH113',
        'IKH351', 'IKH151', 'IKH311', 'IKH309', 'IKH111',
        'IKL335', 'IKL135', 'IKL341', 'IKL141', 'IKS108',
        'IKS308', 'IKS326', 'IKS328', 'ISM313', 'ISO101',
        'ISO301', 'ISM114', 'ISM314', 'IKD112', 'IKD312',
        'IKD313', 'IKD123', 'IKS323', 'IKS319', 'IKS301',
        'IKS327', 'IKS123', 'IKS126', 'ISL304', 'ISL303',
        'IIB205', 'UBA402', 'UKW400', 'ISM404', 'ISM403',
        'IKB250', 'IKS413', 'UKT101', 'IKB450', 'IKB451',
        'IKP303', 'IKP311', 'IKG311', 'ISA301', 'ISD301',
        'ISL305', 'ISM312', 'ISL302', 'ISM315', 'ISM316',
        'ISM317', 'UKT300' ]
    coreSI = [ 'ISM221', 'IUM461', 'IKB406', 'IKB206', 'IKB405',
        'IKB411', 'ISM401', 'IKH323', 'IKH313', 'IKH113',
        'IKH351', 'IKH151', 'IKH311', 'IKH309', 'IKH111',
        'IKL335', 'IKL135', 'IKL341', 'IKL141', 'IKS108',
        'IKS308', 'IKS326', 'IKS328', 'ISM313', 'ISO101',
        'ISO301', 'ISM114', 'ISM314', 'IKD112', 'IKD312',
        'IKD313', 'IKD123', 'IKS323', 'IKS319', 'IKS301',
        'IKS327', 'IKS123', 'IKS126', 'ISL304', 'ISL303',
        'IIB205', 'UBA402', 'UKW400', 'ISM404', 'ISM403',
        'IKB250', 'IKS413', 'UKT101', 'IKB450', 'IKB451' ]

    prodi = nim[:3]
    print nim

    transkripRPL = set(transkrip).intersection(RPL)
    transkripGK = set(transkrip).intersection(GK)
    transkripKI = set(transkrip).intersection(coreKI)
    transkripSI = set(transkrip).intersection(SI)
    numRPL = len(list(transkripRPL))
    numGK  = len(list(transkripGK))
    numKI  = len(list(transkripKI))
    numSI = len(list(transkripSI))
    print "RPL:", numRPL
    print "GK :", numGK
    print "KI :", numKI
    print "SI :", numSI

    if prodi == '064':
        if numRPL > numGK and numRPL > numKI:
            print "[RPL]"
            untaken = [x for x in set(coreRPL) if x not in
                transkripRPL]

        if numGK > numRPL and numGK > numKI:
            print "[GK]"
            untaken = [x for x in set(coreGK) if x not in
                transkripGK]

        if numKI > numRPL and numKI > numGK:
            print "[KI]"
            untaken = [x for x in set(coreKI) if x not in
                transkripKI]
    else:
        print "[SI]"
        untaken = [x for x in set(coreSI) if x not in
            transkripSI]
    if len(untaken) > 0:
        print nim, len(untaken)
        for lecture in untaken:
            data = "'" + nim + ";" + lecture + "\n"
            kelas.write(data)
    kelas.close()


def lebih_baik(nilai_baru, nilai_lama):
    hasil = False

    if nilai_baru in ['A']:
        hasil = True
    elif nilai_baru in ['A-'] and nilai_lama in ['A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['B+'] and nilai_lama in ['B+', 'B', 'B-', 'C+', 'C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['B'] and nilai_lama in ['B', 'B-', 'C+', 'C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['B-'] and nilai_lama in ['B-', 'C+', 'C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['C+'] and nilai_lama in ['C+', 'C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['C'] and nilai_lama in ['C', 'D', 'E']:
        hasil = True
    elif nilai_baru in ['D'] and nilai_lama in ['D', 'E']:
        hasil = True
    elif nilai_baru in ['E'] and nilai_lama in ['E']:
        hasil = True

    return hasil


if __name__ == '__main__':
    main()

