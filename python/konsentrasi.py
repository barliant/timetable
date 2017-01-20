''' konsentrasi.py

Diberikan daftar mata kuliah yang diambil oleh seorang
mahasiswa, tentukan apa konsentrasinya. Khusus untuk mahasiswa
Program Studi TIF (064*).


Anung B. Ariwibowo (barliant@gmail.com)
20141227

* 20141227
  * Mulai dengan mengumpulkan daftar mata kuliah untuk setiap
  * konsentrasi: RPL, KI, dan GK (GrafKom).
'''

__author__ = 'Anung B. Ariwibowo'


import xlrd
import numpy as np


def main():
    wb = xlrd.open_workbook('../raw-data/courses-taken.xls')
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

    # transkrip hanya memuat nim: list_of_lectures
    # transkrip_nilai memuat nim: dict_of_lectures{kode: grade}
    transkrip = {}
    transkrip_nilai = {}
    for nrow in range(1, sheet.nrows-1):
        kuliah = []
        nilai_kuliah = {}
        nim = str(int(data['NIM'][nrow]))
        kode = data['Kode'][nrow]
        grade = data['Grade'][nrow]

        if transkrip.has_key(nim):
            lectures = transkrip[nim]
            lectures.append(kode)
            nilai = transkrip_nilai[nim]
            nilai[kode] = grade
        else:
            kuliah.append(kode)
            transkrip[nim] = kuliah
            nilai_kuliah[kode] = grade
            transkrip_nilai[nim] = nilai_kuliah


        '''
        if grade in ['']:
            print nrow, nim, kode
        '''

    print len(transkrip), len(transkrip_nilai)

    kelas = open("../raw-data/kelas.csv", "w")
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

    ditawarkan = [ 'ISL304', 'ISM314', 'IKS327', 'IKH328',
        'IKG402', 'IKH313', 'ISM401', 'IKH329', 'ISO301',
        'IKG321', 'IKH311', 'IKB451', 'IKH318', 'IKS323',
        'IKH323', 'IKH323', 'IKB250', 'IKD312', 'IKS304',
        'IKH316', 'IKL233', 'ISM313', 'IKH326', 'IKS308',
        'IKH314', 'IUM461', 'IKB450', 'IKS318', 'IKS326',
        'IKL343', 'ISM221', 'ISM403', 'IKH327', 'UKT101',
        'IKP321', 'UKW400', 'IKP302', 'IKP311', 'IKH342',
        'IKB405', 'ISM114', 'IKS126', 'IKH128', 'IKG101',
        'IKH113', 'IKH110', 'IKP102', 'IKP111', 'IKH109',
        'ISO101', 'IKG121', 'IKH111', 'IKL141', 'IKH118',
        'ISM404', 'IKH310', 'IKL341', 'IKS413' ]

    rowidx = 1
    colidx = 0

    for student in transkrip:
        data = transkrip[student]
        data_nilai = transkrip_nilai[student]
        lecture = [x for x in data_nilai if data_nilai[x] not in ['', 'D', 'E']]
        prodi = student[:2]
        #print prodi, student

        transkripRPL = set(data).intersection(RPL)
        transkripGK = set(data).intersection(GK)
        transkripKI = set(data).intersection(coreKI)
        transkripSI = set(data).intersection(SI)
        numRPL = len(list(transkripRPL))
        numGK  = len(list(transkripGK))
        numKI  = len(list(transkripKI))
        numSI = len(list(transkripSI))
        print "RPL:", numRPL, "GK :", numGK, "KI :", numKI, "SI :", numSI,

        if prodi == '64':
            if numRPL > numGK and numRPL > numKI:
                print "[RPL]"
                untaken = [x for x in set(coreRPL) if x not in lecture]

            if numGK > numRPL and numGK > numKI:
                print "[GK]"
                untaken = [x for x in set(coreGK) if x not in lecture]

            if numKI > numRPL and numKI > numGK:
                print "[KI]"
                untaken = [x for x in set(coreKI) if x not in lecture]
        else:
            print "[SI]"
            untaken = [x for x in set(coreSI) if x not in lecture]

        if len(untaken) > 0:
            print student, len(untaken)
            for kode in untaken:
                if kode in ditawarkan:
                    data = "'" + student + ";" + kode + "\n"
                    kelas.write(data)

        fail_lectures = [x for x in data_nilai if data_nilai[x] not in ['', 'D', 'E']]
        if len(fail_lectures) > 0:
            print student, len(fail_lectures)
            for kode in fail_lectures:
                if kode in ditawarkan:
                    data = "'" + student + ";" + kode + "\n"
                    kelas.write(data)

        rowidx = rowidx + 1
        
        '''
        if rowidx > 5:
            exit()
        '''

    kelas.close()


if __name__ == '__main__':

    main()

