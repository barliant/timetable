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

peserta = { '06408021': 'Indra Ramadhan', '06408032':
'Muhammad Yazid', '06409017': 'Fahim Alawi', '06409019':
'Gilang Parananda Ramitan', '06409022': 'Moh. Rizki Yuliansyah',
'06409025': 'Nishaizaty', '06409032': 'Tommy Akhmadi',
'06409033': 'Tri Endah Sari', '06409036': 'Bhismi Alham',
'06409045': 'Sarah Sitha Azzahra', '06410002': 'Defry Tri Hendra',
'06410005': 'Bintang Winandito', '06410008':
'Widhah Insani Wahdjudi', '06410010': 'Ayu Permata Sary',
'06410013': 'Stefanus Joko Tri Anggoro',
'06410023': 'Laras Okty Hanifah', '06410027': 'Maradondi T',
'06508007': 'Wiwiet Agung', '06509012': 'Muhammad Rifki',
'06509013': 'Murti Januarti', '06510007': 'Rifky Fahyudi',
'06510012': 'Benna Anggriawan', '06509110': 'Putu Hardja Sugaray',
'06411007': 'Dewi Wulan Cempaka Ayu' }


coursedict = { 'IEB232': 'Teknik Komunikasi Data', 'IFI301':
'Fisika I', 'IFI302': 'Fisika II', 'IIB205': 'Perilaku Organisasi ',
'IIS201': 'Penelitian Operasiaonal', 'IKA301':
'Kecerdasan Buatan', 'IKA312': 'Sistem Jaringan Syaraf',
'IKA321': 'Komputasi Bergerak',
'IKB205': 'Metodologi Penelitian dan Penulisan Ilmiah',
'IKB206': 'Kreativitas dan Inovasi', 'IKB250': 'Kuliah Kerja Profesi',
'IKB405': 'Penulisan ilmiah dan Laporan',
'IKB406': 'Metodologi Penelitian ',
'IKB411': 'Konsep Teknologi Informasi dan Keamanan',
'IKB450': 'Tugas Akhir I', 'IKB451': 'Tugas Akhir II',
'IKD112': 'Praktikum Manajemen Data dan Informasi',
'IKD123': 'Praktikum Manajemen Data dan Informasi Lanjut',
'IKD312': 'Manajemen Data dan Informasi',
'IKD313': 'Manajemen Data dan Informasi Lanjut',
'IKG101': 'Praktikum Grafika Komputer',
'IKG102': 'Praktikum Pengolahan Citra',
'IKG121': 'Praktikum Rekayasa Sistem Multimedia',
'IKG301': 'Grafika Komputer', 'IKG302': 'Pengolahan Citra',
'IKG304': 'Seni Animasi', 'IKG311': 'Sistem Informasi Geografi',
'IKG321': 'Rekayasa Sistem Multimedia', 'IKG402': 'Grafika Komputer',
'IKH109': 'Praktikum Pengelolaan Keamanan Informasi',
'IKH110': 'Praktikum Keamanan Jaringan Komputer',
'IKH111': 'Praktikum Sistem Operasi',
'IKH112': 'Praktikum Keamanan Sistem Operasi',
'IKH113': 'Praktikum Jaringan Komputer dan Keamanan',
'IKH114': 'Praktikum Sistem Pengendalian Akses',
'IKH116': 'Praktikum Model dan Arsitektur Keamanan Informasi',
'IKH117': 'Praktikum Desain Keamanan Informasi',
'IKH118': 'Praktikum Verifikasi dan Validasi Keamanan Informasi',
'IKH119': 'Praktikum Keamanan Operasional',
'IKH123': 'Praktikum Keamanan Informasi',
'IKH126': 'Praktikum Perencanaan Kontinyuitas Bisnis',
'IKH128': 'Praktikum Forensik Komputer dan Jaringan',
'IKH132': 'Praktikum Pengelolaan Jaringan Komputer',
'IKH151': 'Praktikum Organisasi dan Arsitektur Komputer',
'IKH203': 'Arsitektur Komputer', 'IKH300': 'Pengantar Sistim Digital',
'IKH303': 'Arsitektur Komputer', 'IKH306': 'Pemrograman Jaringan',
'IKH309': 'Pengelolaan Jaringan Komputer',
'IKH310': 'Sistem Keamanan Jaringan', 'IKH311': 'Sistem Operasi',
'IKH312': 'Keamanan Sistem Operasi',
'IKH313': 'Jaringan Komputer dan Keamanan',
'IKH314': 'Sistem Pengendalian Akses',
'IKH316': 'Model dan Arsitektur Keamanan Informasi',
'IKH317': 'Desain Keamanan Informasi',
'IKH318': 'Verifikasi dan Validasi Keamanan Informasi',
'IKH319': 'Keamanan Operasional',
'IKH321': 'Sistem Keamanan Komputer', 'IKH323': 'Keamanan Informasi',
'IKH324': 'Keamanan Pengembangan Aplikasi',
'IKH326': 'Perencanaan Kontinyuitas Bisnis', 'IKH327': 'Keamanan Fisik',
'IKH328': 'Forensik Komputer dan Jaringan',
'IKH329': 'Pengelolaan Keamanan Informasi', 'IKH330': 'Bahasa Rakitan',
'IKH331': 'Sistem Terdistribusi', 'IKH342': 'Pengolahan Sinyal Digital',
'IKH351': 'Organisasi dan Arsitektur Komputer',
'IKL133': 'Praktikum Pemodelan Geometri',
'IKL135': 'Praktikum Dasar Pemrograman',
'IKL141': 'Praktikum Struktur Data dan Algoritma',
'IKL232': 'Model Dan Simulasi', 'IKL233': 'Pemodelan Geometri',
'IKL335': 'Dasar Pemrograman', 'IKL341': 'Struktur Data dan Algoritma',
'IKL343': 'Desain dan Analisis Algoritma',
'IKP102': 'Praktikum Pemrograman Berbasis Komponen',
'IKP103': 'Praktikum Mobile Programming',
'IKP111': 'Praktikum Pemrograman Berbasis Web',
'IKP113': 'Praktikum Bahasa Pemrograman', 'IKP213': 'Bahasa Pemrograman',
'IKP301': 'Desain dan Implementasi Program',
'IKP302': 'Pemrograman Berbasis Komponen', 'IKP303': 'Mobile Programming',
'IKP311': 'Pemrograman Berbasis Web',
'IKP321': 'Manajemen dan Kualitas Perangkat Lunak',
'IKP333': 'Cloud Computing',
'IKS104': 'Praktikum Metode Berorientasi Objek',
'IKS108': 'Praktikum Sistem Informasi Manajemen',
'IKS118': 'Praktikum Verifikasi dan Validasi Perangkat Lunak',
'IKS123': 'Praktikum Analisis dan Pemodelan Perangkat Lunak',
'IKS126': 'Praktikum Desain Perangkat Lunak',
'IKS201': 'Arsitektur Perangkat Lunak',
'IKS212': 'Computer Aided Software Engineering',
'IKS213': 'Kewirausahaan Telematika',
'IKS301': 'Interaksi Manusia dan Komputer', 'IKS302': 'Sistem Informasi',
'IKS304': 'Metode Berorientasi Objek',
'IKS308': 'Sistem Informasi Manajemen',
'IKS318': 'Verifikasi dan Validasi  Perangkat Lunak',
'IKS319': 'Verifikasi dan Validasi Sistem Informasi',
'IKS323': 'Analisis dan Pemodelan Perangkat Lunak',
'IKS326': 'Arsitektur Enterprise ', 'IKS327': 'Desain Perangkat Lunak ',
'IKS328': 'ITSM (Information Technology Service Management)',
'IKS413': 'Technopreneurship', 'ISA301': 'Bisnis Berbasis Internet',
'ISD301': 'Data Warehouse', 'ISD305': 'Rekayasa Data dan Pengetahuan',
'ISD312': 'Information Retrieval', 'ISD313': 'Virtualisasi',
'ISD314': 'Teknik Data Mining', 'ISL302': 'Komunikasi Bisnis dan Teknis',
'ISL303': 'Pengetahuan Bisnis', 'ISL304': 'Analisa Proses Bisnis (MPK)',
'ISL305': 'Business Intelligence',
'ISM114': 'Praktikum Audit Sistem Informasi',
'ISM202': 'Manajemen Pengetahuan', 'ISM221': 'Ekonomi Informasi',
'ISM302': 'Manajemen Konfigurasi',
'ISM303': 'Komunikasi Interpersonal & Etika Profesi',
'ISM312': 'Manajemen Pengetahuan',
'ISM313': 'Pengantar Audit Sistem Informasi (MPK)',
'ISM314': 'Audit Sistem Informasi', 'ISM315': 'Manajemen Keuangan',
'ISM316': 'Manajemen Pemasaran IT', 'ISM317': 'Manajemen Dokumen',
'ISM401': 'Manajemen Proyek Teknologi Informasi',
'ISM403': 'Etika, Agama, Profesionalisme dan Legal',
'ISM404': 'Proyek Rekayasa',
'ISO101': 'Praktikum Pengelolaan Sistem Informasi',
'ISO301': 'Pengelolaan Sistem Informasi (MPK)',
'IUM263': 'Struktur Diskrit II', 'IUM314': 'Kalkulus',
'IUM331': 'Kalkulus I', 'IUM332': 'Kalkulus II',
'IUM333': 'Kalkulus Lanjut', 'IUM341': 'Aljabar Linier',
'IUM351': 'Statistik Dasar', 'IUM461': 'Struktur Diskrit I',
'PDU212': 'Teori Warna', 'PMA331': 'Kalkulus I', 'PMA332': 'Kalkulus II',
'UAG201': 'Pendidikan Agama Islam', 'UAG202': 'Pendidikan Agama Kristen',
'UAG203': 'Pendidikan Agama Katolik', 'UAG204': 'Pendidikan Agama Budha',
'UAG205': 'Pendidikan Agama Hindu', 'UBA201': 'Bahasa Inggris I',
'UBA202': 'Bahasa Inggris II', 'UBA402': 'Internasionalisasi',
'UBN200': 'Bahasa Indonesia', 'UKD200': 'Keadilan, Demokrasi & HAM',
'UKT101': 'Kuliah Kerja Lapangan',
'UKT200': 'Kuliah Usaha Mandiri Ilmu Teknik Terapan',
'UKT300': 'Kuliah Usaha Mandiri Ilmu Teknik Terapan',
'UKW400': 'Pancasila dan Kewarganegaraan',
'UPA200': 'Pendidikan Pancasila', 'EAU300': 'Pengantar Akuntansi',
'EMU302': 'Pengantar Manajemen Umum', 'IFI103': 'Praktikum Fisika Dasar',
'III202': 'Konsep Teknologi', 'IKB301': 'Pengantar Teknologi Informasi',
'IKB350': 'Riset Teknologi Informasi', 'IKD302': 'Basis Data',
'IKD303': 'Sistem Basis Data', 'IKG303': 'Grafika Komputer Lanjut',
'IKG323': 'Disain Implemantasi Multimedia',
'IKH100': 'Praktikum Pengantar Sistem Digital',
'IKH104': 'Praktikum Jaringan Komputer',
'IKH118': 'Praktikum Verifikasi dan Validasi Keamanan Informasi',
'IKH151': 'Praktikum Organisasi dan Arsitektur Komputer',
'IKH232': 'Pengelolaan Jaringan Komputer', 'IKH301': 'Organisasi Komputer',
'IKH304': 'Jaringan Komputer',
'IKL141': 'Praktikum Struktur Data dan Algoritma',
'IKL332': 'Pemodelan Geometri', 'IKL333': 'Algoritma dan Pemrograman',
'IKL341': 'Struktur Data dan Algoritma',
'IKL343': 'Desain dan Analisis Algoritma',
'IKS101': 'Praktikum Pemrograman Berorientasi Objek',
'IKS102': 'Praktikum Pemrograman Terstruktur',
'IKS103': 'Praktikum Rekayasa Perangkat Lunak',
'IKS214': 'Komputer dan Masyarakat', 'IKS303': 'Rekayasa Perangkat Lunak',
'IKS306': 'Analisa dan Disain Sistem', 'IKS307': 'Teknik Pengujian Sistem',
'IKS314': 'Manajemen Keamanan Sitem Informasi',
'IKS315': 'Sistem Informasi Akuntansi',
'IKS316': 'Pemrograman Berorientasi Objek',
'IKS321': 'Pemrograman Terstruktur', 'ISD201': 'Teknik Data Mining',
'ISK201': 'Konsep Sistem Informasi I',
'ISK202': 'Konsep Sistem Informasi II',
'ISL301': 'Pengembangan Aplikasi Berbasis Web',
'ISM301': 'Manajemen Proyek Teknologi Informasi',
'ISM321': 'Ekonomi Informasi', 'IUM362': 'Logika Matematika',
'UKW200': 'Kewiraan' }


def main(nim_mhs):
    # SIS: wb = xlrd.open_workbook('../raw-data/transkrip-aktif-2014-2015-1.xls')
    # UPTF
    wb = xlrd.open_workbook('../raw-data/Nilai-Pra-Yudisium-2014-gasal-TIF-SI.xls')
    print wb.sheet_names()

    sheet = wb.sheet_by_index(0)
    print "name: ", sheet.name
    print "rows: ", sheet.nrows
    print "cols: ", sheet.ncols
    transkrip = []
    transkrip_lulus = {}
    transkrip_fail = {}
    for nrow in range(1, sheet.nrows):
        nim_cell = sheet.cell(nrow, 0)
        kode_cell = sheet.cell(nrow, 1)
        nilai_cell = sheet.cell(nrow, 3)
        nim = nim_cell.value
        kode = kode_cell.value
        grade = nilai_cell.value
        if nim == nim_mhs:
            transkrip.append(kode)
            if grade not in ['D', 'E']:
                transkrip_lulus[kode] = grade
            else:
                transkrip_fail[kode] = grade
    print len(transkrip), len(transkrip_lulus), len(transkrip_fail)
    print set(transkrip)
    print set(transkrip_lulus.keys())
    print set(transkrip_fail.keys())
    set_transkrip = set(transkrip)
    print len(set_transkrip)
    set_lulus = set(transkrip_lulus.keys())
    set_fail = set(transkrip_fail.keys())
    should_be_empty = set_lulus & set_fail
    print should_be_empty


    kelas = open("../raw-data/prayudisium-UPTF.csv", "a")
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

    prodi = nim_mhs[:3]
    print "nim:", nim_mhs
    print "prodi:", prodi

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

    konsentrasi = ''
    # must be initialized first, just in case nilainya udah nggak bermasalah.
    untaken = []
    if prodi == '064':
        if numRPL > numGK and numRPL > numKI:
            konsentrasi = 'RPL'
            untaken = [x for x in set(coreRPL) if x not in
                transkripRPL]

        if numGK > numRPL and numGK > numKI:
            konsentrasi = 'GK'
            untaken = [x for x in set(coreGK) if x not in
                transkripGK]

        if numKI > numRPL and numKI > numGK:
            konsentrasi = 'KI'
            untaken = [x for x in set(coreKI) if x not in
                transkripKI]
    else:
        konsentrasi = 'SI'
        untaken = [x for x in set(coreSI) if x not in
            transkripSI]
    if len(set_fail) > 0:
        print nim_mhs, konsentrasi, len(set_fail)
        for lecture in set_fail:
            data = "'" + nim_mhs + ";" + peserta[nim_mhs] + ";" + konsentrasi + ";" + lecture + ";" + coursedict[lecture] + ";" + transkrip_fail[lecture] + "\n"
            kelas.write(data)
    if len(untaken) > 0:
        print nim_mhs, konsentrasi, len(untaken)
        for lecture in untaken:
            data = "'" + nim_mhs + ";" + peserta[nim_mhs] + ";" + konsentrasi + ";" + lecture + ";" + coursedict[lecture] + ";" + "\n"
            kelas.write(data)
    kelas.close()


if __name__ == '__main__':

    ''' belum ada data transkrip:

06?13*
06?14*
 
    transkrip06407046 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKL135', 'IKL335', 'IUM461',
        'UBA402', 'IKB405', 'IKH313', 'IKS413', 'UKT101',
        'IKH329', 'IKD112', 'IKD312', 'IKH323', 'IKS301',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'ISM221',
        'ISM403', 'IKB450', 'IKD313', 'IKH314', 'IKH326',
        'IUM314', 'IKH109', 'IKH110', 'IKH128', 'IKH328',
        'IKH119', 'IKH126', 'IKH319', 'IKH327', 'IKG321',
        'IKH316', 'IKH329', 'IUM332', 'IFI302', 'IKH300',
        'IKH314', 'IKH326', 'IKG321' ]
    transkrip06407004 = [ 'UAG201', 'IUM362', 'IUM332',
        'IFI103', 'UBA201', 'IFI302', 'UBA202', 'UBN200',
        'IKL333', 'IUM361', 'UKW200', 'UPA200', 'IUM331',
        'IFI301', 'IUM341', 'III202', 'IKH301', 'IKB301',
        'IKH300', 'IKH100', 'IKH111', 'IKD302', 'IKP301',
        'IKL232', 'IUM333', 'IKH304', 'IEB232', 'ISM303',
        'IKB350', 'ISM321', 'IKS306', 'IKB205', 'ISM301',
        'IKD303', 'IKS303', 'IUM351', 'IKL343', 'IKL341',
        'IKH311', 'IKS301', 'IKS304', 'IKP302', 'IKG321',
        'IKH342', 'IKG302', 'IKG311', 'IKG301', 'IKL332',
        'IKG303', 'IKG323', 'IKL232', 'IKD303', 'IKP302',
        'IKG321', 'IKG302', 'PDU212', 'IKG301' ]
    transkrip06507005 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH323', 'IKS301', 'IKS323', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'ISM221',
        'ISM403', 'IKB250', 'IKB450', 'IKD313', 'IKD123',
        'ISM314', 'ISL303', 'IIB205', 'IKS108', 'IKS308',
        'ISL304', 'ISO301', 'ISO101', 'ISM313', 'IKS319',
        'IKS326', 'ISM114', 'IKS328', 'ISA301', 'ISL301' ]
    transkrip06508009 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IUM461', 'IKB405',
        'IKH311', 'IKH313', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH323', 'IKS123', 'IKS301', 'IKS323',
        'IKS126', 'IKS327', 'ISM401', 'UKW400', 'IKB206',
        'ISM221', 'ISM403', 'IKD313', 'IKD123', 'ISL303',
        'IIB205', 'IKS108', 'IKS308', 'ISL304', 'IKS326',
        'IKS328', 'IKS304', 'IKP311' ]
    transkrip06408029 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS104', 'IKS123',
        'IKS301', 'IKS304', 'IKS323', 'IUM263', 'IKP102',
        'IKP111', 'IKP302', 'IKP311', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKH331',
        'IKP103', 'IKP113', 'IKP303', 'IKS118', 'IKS318',
        'ISM221', 'IKP321', 'ISM404', 'IKB250', 'IKB450',
        'IKD313', 'IKD123', 'IKP213', 'IKH314', 'IKL232',
        'IUM332', 'IFI302', 'IEB232', 'IKH300', 'IKP321',
        'IKH314' ]
    transkrip06408018 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKH329', 'IKL343',
        'IKD112', 'IKD312', 'IKH123', 'IKH323', 'IKS301',
        'IKS304', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'ISM404', 'IKB450', 'IKH314', 'IKH326',
        'IKH112', 'IKH114', 'IKH312', 'IUM314', 'IKH109',
        'IKH110', 'IKH128', 'IKH310', 'IKH328', 'IKH119',
        'IKH126', 'IKH319', 'IKH118', 'IKH318', 'IKH327',
        'IKH132', 'IKH324', 'IKH316', 'IKH329', 'IUM332',
        'IFI302', 'IEB232', 'IKH300', 'IKH314', 'IKH326',
        'IKG311', 'IKH203' ]
    transkrip06508006 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'IKH113', 'IKH311', 'IKH313',
        'IKS413', 'UKT101', 'IKD112', 'IKD312', 'IKH323',
        'IKS123', 'IKS301', 'IKS126', 'IKS327', 'ISM401',
        'UKW400', 'IKB206', 'IKB406', 'ISM221', 'ISM403',
        'ISM404', 'IKB250', 'IKB450', 'IKD313', 'IKD123',
        'ISM314', 'ISL303', 'IIB205', 'IKS108', 'IKS308',
        'ISL304', 'ISO301', 'ISO101', 'ISM313', 'IKS319',
        'IKS326', 'ISM114', 'IKS328', 'IKH104', 'ISA301',
        'ISL305', 'ISL301', 'ISM316' ]
    transkrip06508007 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH113',
        'IKH311', 'IKH313', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH323', 'IKS123', 'IKS301', 'IKS323',
        'IKS126', 'IKS327', 'ISM401', 'UKW400', 'IKB206',
        'IKB406', 'ISM221', 'ISM403', 'ISM404', 'IKB250',
        'IKB450', 'IKD313', 'IKD123', 'ISM314', 'ISL303',
        'IIB205', 'IKS108', 'IKS308', 'ISL304', 'ISO301',
        'ISO101', 'ISM313', 'IKS319', 'IKS326', 'ISM114',
        'IKS328', 'IKP303', 'ISA301', 'ISL305', 'ISL301' ]
    transkrip06408021 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD312', 'IKH123',
        'IKH323', 'IKS104', 'IKS123', 'IKS301', 'IKS304',
        'IKS323', 'IUM263', 'IKP311', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKS118',
        'IKS318', 'ISM221', 'IKP321', 'ISM403', 'ISM404',
        'IKB450', 'IKD313', 'IKD123', 'IKG321', 'IKG101',
        'IKH342', 'IKG102', 'IKL133', 'IKL233', 'PDU212',
        'IKG121', 'IKG402', 'IUM332', 'IFI302', 'IKH300',
        'IKP321', 'IKG321', 'IKG311', 'IKG304' ]
    transkrip06408032 = [ 'IKH111', 'IKL341', 'IKL141',
        'IKB411', 'IKL135', 'IKL335', 'IUM461', 'UBA402',
        'IKB405', 'IKH311', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH123', 'IKS104', 'IKS123', 'IKS301',
        'IKS304', 'IKS323', 'IUM263', 'IKP102', 'IKP111',
        'IKP311', 'IKS126', 'IKS327', 'ISM401', 'UKW400',
        'IKB206', 'IKB406', 'IKH331', 'IKP103', 'IKP113',
        'IKP303', 'IKS118', 'IKS318', 'ISM221', 'IKP321',
        'ISM404', 'IKB250', 'IKB450', 'IKD313', 'IKD123',
        'IKP213', 'IKH314', 'IKH326', 'IFI302', 'IKH300',
        'IKP321', 'IKH314', 'IKH326', 'IKP333', 'ISD312',
        'IKG311' ]
    transkrip06409002 = [ 'IKH351', 'IKL341', 'IKL141',
        'IKB411', 'IKH151', 'IKL135', 'IKL335', 'IUM461',
        'UBA402', 'IKH113', 'IKS413', 'UKT101', 'IKH329',
        'IKD112', 'IKD312', 'IKH123', 'IKS301', 'UKW400',
        'IKH112', 'IKH312', 'IUM314', 'IKH329', 'IUM332',
        'IFI302', 'IKH300' ]
    transkrip06509006 = [ 'IKH351', 'IKL341', 'IKL141',
        'IKB411', 'IKH151', 'IKL135', 'IKL335', 'IUM461',
        'UBA402', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH323', 'IKS123', 'IKS301', 'ISM401', 'IKB206',
        'IKB406', 'ISM403', 'ISM404', 'IKB250', 'IKD313',
        'IKD123', 'ISM314', 'ISL303', 'IKS308', 'ISL304',
        'ISM313', 'IKS319', 'IKS326', 'ISM114', 'IKS328',
        'IKH123', 'IKS304', 'ISM316' ]
    transkrip06509023 = [ 'IKH309', 'IKH351', 'IKL341',
        'IKL141', 'IKB411', 'IKL135', 'IKL335', 'IUM461',
        'UBA402', 'IKH113', 'IKS413', 'IKD112', 'IKD312',
        'IKS123', 'IKS301', 'IKS323', 'IKS327', 'ISM401',
        'UKW400', 'IKB206', 'IKB406', 'ISM221', 'ISM404',
        'IKD313', 'IKD123', 'ISM314', 'ISL303', 'IIB205',
        'IKS108', 'IKS308', 'ISL304', 'ISO301', 'ISO101',
        'ISM313', 'IKS319', 'IKS326', 'ISM114', 'IKS328',
        'IKP311', 'IKP303', 'ISA301' ]
    transkrip06409032 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS104', 'IKS123',
        'IKS301', 'IKS304', 'IKS323', 'IUM263', 'IKP102',
        'IKP111', 'IKP302', 'IKP311', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKH331',
        'IKP103', 'IKP113', 'IKP303', 'IKS118', 'IKS318',
        'ISM221', 'IKP321', 'ISM404', 'IKB250', 'IKB450',
        'IKD313', 'IKD123', 'IKP213', 'IKH314', 'IUM332',
        'IFI302', 'IKH300', 'IKP321', 'IKH314' ]
    transkrip06509017 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKS123', 'IKS301', 'IKS323', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'ISM221',
        'ISM404', 'ISM314', 'ISL303', 'IIB205', 'IKS108',
        'IKS308', 'ISL304', 'ISO301', 'ISO101', 'ISM313',
        'IKS319', 'IKS326', 'ISM114', 'IKS328', 'IKP311',
        'IKP303', 'ISA301', 'ISM316' ]
    transkrip06509110 = [ 'Unauthorized access' ]
    transkrip06409025 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS104', 'IKS123',
        'IKS301', 'IKS304', 'IKS323', 'IUM263', 'IKP102',
        'IKP111', 'IKP302', 'IKP311', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKH331',
        'IKP103', 'IKP113', 'IKP303', 'IKS118', 'IKS318',
        'ISM221', 'IKP321', 'ISM404', 'IKB250', 'IKB450',
        'IKD313', 'IKD123', 'IKP213', 'IKH314', 'IUM332',
        'IFI302', 'IKH300', 'IKP321', 'IKH314' ]
    transkrip06409042 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'IKB405', 'IKH113', 'IKH311', 'IKH313',
        'IKS413', 'UKT101', 'IKL343', 'IKD112', 'IKD312',
        'IKH123', 'IKH323', 'IKS104', 'IKS123', 'IKS301',
        'IKS304', 'IKS323', 'IUM263', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKS118',
        'IKS318', 'ISM221', 'IKP321', 'ISM404', 'IKB450',
        'IKD313', 'IKD123', 'IKH314', 'IKG321', 'IKG101',
        'IKH342', 'IKG102', 'IKG302', 'IKL133', 'IKL233',
        'PDU212', 'IKG121', 'IKG402', 'IUM332', 'IFI302',
        'IKH300', 'IKP321', 'IKH314', 'IKG321', 'IKG304' ]
    transkrip06409036 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKH329', 'IKL343',
        'IKD112', 'IKD312', 'IKH123', 'IKH323', 'IKS301',
        'IKS304', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'ISM404', 'IKB250', 'IKB450', 'IKH314',
        'IKH326', 'IKH112', 'IKH114', 'IKH312', 'IUM314',
        'IKH109', 'IKH110', 'IKH128', 'IKH310', 'IKH328',
        'IKH119', 'IKH126', 'IKH319', 'IKH118', 'IKH318',
        'IKH327', 'IKH132', 'IKH324', 'IKH316', 'IKH329',
        'IUM332', 'IFI302', 'IKH300', 'UKT300', 'IKH314',
        'IKH326' ]
    transkrip06409045 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH123', 'IKH323', 'IKS104', 'IKS123', 'IKS301',
        'IKS304', 'IKS323', 'IUM263', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKS118',
        'IKS318', 'ISM221', 'IKP321', 'ISM403', 'ISM404',
        'IKB450', 'IKD313', 'IKD123', 'IKH326', 'IKG321',
        'IKG101', 'IKH342', 'IKG102', 'IKG302', 'IKL133',
        'IKL233', 'PDU212', 'IKG121', 'IKG402', 'IUM332',
        'IFI302', 'IKH300', 'IKP321', 'IKH326', 'IKG321',
        'IKG304', 'ISD305' ]
    transkrip06509012 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKL135', 'IKL335',
        'IUM461', 'IKB405', 'IKH113', 'IKH311', 'IKH313',
        'IKS413', 'UKT101', 'IKD112', 'IKD312', 'IKH323',
        'IKS301', 'IKS323', 'IKS126', 'IKS327', 'ISM401',
        'UKW400', 'IKB206', 'IKB406', 'ISM221', 'ISM404',
        'IKB250', 'IKB450', 'IKD313', 'IKD123', 'ISM314',
        'ISL303', 'IIB205', 'IKS108', 'IKS308', 'ISL304',
        'ISO301', 'ISO101', 'ISM313', 'IKS319', 'IKS326',
        'ISM114', 'IKS328', 'IKP303', 'ISA301', 'ISL302',
        'ISM316' ]
    transkrip06409033 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS104', 'IKS123',
        'IKS301', 'IKS304', 'IKS323', 'IUM263', 'IKS126',
        'IKS327', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'IKS118', 'IKS318', 'ISM221', 'IKP321', 'ISM404',
        'IKB250', 'IKB450', 'IKD313', 'IKD123', 'IKH314',
        'IKH326', 'IKG321', 'IKG101', 'IKH342', 'IKG102',
        'IKG302', 'IKL133', 'IKL233', 'PDU212', 'IKG121',
        'IKG402', 'IUM332', 'IFI302', 'IKH300', 'IKP321',
        'IKH314', 'IKH326', 'ISD312', 'IKG321', 'IKG304' ]
    transkrip06509010 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH323', 'IKS123', 'IKS301', 'IKS323', 'IKS126',
        'IKS327', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'ISM403', 'ISM404', 'IKD313', 'IKD123',
        'ISM314', 'ISL303', 'IIB205', 'IKS308', 'ISL304',
        'ISO301', 'ISO101', 'ISM313', 'IKS319', 'IKS326',
        'ISM114', 'IKS328', 'IKP311', 'IKP303', 'ISL305',
        'ISM316' ]
    transkrip06409022 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH123', 'IKH323', 'IKS104', 'IKS123', 'IKS301',
        'IKS304', 'IKS323', 'IUM263', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'IKS118',
        'IKS318', 'ISM221', 'IKP321', 'ISM404', 'IKB250',
        'IKB450', 'IKD313', 'IKD123', 'IKG321', 'IKG101',
        'IKH342', 'IKG102', 'IKG302', 'IKL133', 'IKL233',
        'PDU212', 'IKG121', 'IKG402', 'IFI302', 'IKH300',
        'IKP321', 'IKG321', 'IKG311', 'ISD305' ]
    transkrip06409004 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKH329', 'IKL343',
        'IKD112', 'IKD312', 'IKH123', 'IKH323', 'IKS301',
        'IKS304', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'ISM404', 'IKB250', 'IKB450', 'IKH314',
        'IKH326', 'IKH112', 'IKH114', 'IKH312', 'IUM314',
        'IKH109', 'IKH110', 'IKH128', 'IKH310', 'IKH328',
        'IKH119', 'IKH126', 'IKH319', 'IKH118', 'IKH318',
        'IKH327', 'IKH132', 'IKH324', 'IKH316', 'IKH329',
        'IUM332', 'IFI302', 'IKH300', 'UKT300', 'IKH314',
        'IKH326' ]
    transkrip06409003 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKH329', 'IKL343',
        'IKD112', 'IKD312', 'IKH123', 'IKH323', 'IKS301',
        'IKS304', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'IKP321', 'ISM404', 'IKB250', 'IKB450',
        'IKH314', 'IKH326', 'IKH112', 'IKH114', 'IKH312',
        'IUM314', 'IKH109', 'IKH110', 'IKH128', 'IKH310',
        'IKH328', 'IKH119', 'IKH126', 'IKH319', 'IKH118',
        'IKH318', 'IKH327', 'IKH132', 'IKH324', 'IKH316',
        'IKH329', 'IUM332', 'IFI302', 'IKH300', 'IKP321',
        'IKH314', 'IKH326' ]
    transkrip06509008 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH113',
        'IKH311', 'IKH313', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH323', 'IKS123', 'IKS301', 'IKS323',
        'IKS126', 'IKS327', 'ISM401', 'UKW400', 'IKB206',
        'IKB406', 'ISM221', 'ISM403', 'ISM404', 'IKB250',
        'IKB450', 'IKD313', 'IKD123', 'ISM314', 'ISL303',
        'IIB205', 'IKS108', 'IKS308', 'ISL304', 'ISO301',
        'ISO101', 'ISM313', 'IKS319', 'IKS326', 'ISM114',
        'IKS328', 'UKT300', 'IKP311', 'ISL305', 'ISM316' ]
    transkrip06509025 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH113',
        'IKH311', 'IKH313', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH323', 'IKS123', 'IKS301', 'IKS323',
        'IKS126', 'IKS327', 'ISM401', 'UKW400', 'IKB206',
        'IKB406', 'ISM221', 'ISM403', 'IKB250', 'IKB450',
        'IKD313', 'IKD123', 'ISM314', 'ISL303', 'IIB205',
        'IKS108', 'IKS308', 'ISL304', 'ISO301', 'ISO101',
        'ISM313', 'IKS319', 'IKS326', 'ISM114', 'IKS328',
        'IKP311', 'IKP303', 'ISA301' ]
    transkrip06509013 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH323', 'IKS123', 'IKS301', 'IKS323', 'IKS126',
        'IKS327', 'ISM401', 'UKW400', 'IKB206', 'IKB406',
        'ISM221', 'ISM403', 'ISM404', 'IKB250', 'IKB450',
        'IKD313', 'IKD123', 'ISM314', 'ISL303', 'IIB205',
        'IKS108', 'IKS308', 'ISL304', 'ISO301', 'ISO101',
        'ISM313', 'IKS319', 'IKS326', 'ISM114', 'IKS328',
        'IKS304', 'IKP303', 'ISM312', 'ISL305', 'ISM316' ]
    transkrip06509105 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKD112', 'IKD312',
        'IKH323', 'IKS123', 'IKS301', 'IKS323', 'IKS126',
        'IKS327', 'ISM401', 'UKW400', 'IKB406', 'ISM221',
        'ISM403', 'ISM404', 'IKB450', 'IKD313', 'IKD123',
        'ISM314', 'ISL303', 'IIB205', 'IKS108', 'IKS308',
        'ISL304', 'ISO301', 'ISO101', 'ISM313', 'IKS319',
        'IKS326', 'IKS328', 'IKH104', 'IKS304', 'IKP303',
        'ISA301', 'ISL302', 'ISL305', 'ISL301', 'IKS314' ]
    transkrip06509005 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL341', 'IKL141', 'IKB411', 'IKH151', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH113',
        'IKH311', 'IKH313', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKH323', 'IKS123', 'IKS301', 'IKS323',
        'IKS126', 'IKS327', 'ISM401', 'UKW400', 'IKB206',
        'IKB406', 'ISM221', 'ISM403', 'ISM404', 'IKB250',
        'IKB450', 'IKD313', 'IKD123', 'ISM314', 'ISL303',
        'IIB205', 'IKS108', 'IKS308', 'ISL304', 'ISO301',
        'ISO101', 'ISM313', 'IKS319', 'IKS326', 'ISM114',
        'IKS328', 'IKS304', 'IKP311', 'IKP303', 'ISL302',
        'ISM316' ]
    transkrip06409040 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKH329', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS301', 'IKS304',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'ISM221',
        'ISM403', 'ISM404', 'IKB250', 'IKB450', 'IKH314',
        'IKH326', 'IKH112', 'IKH312', 'IUM314', 'IKH109',
        'IKH110', 'IKH128', 'IKH310', 'IKH328', 'IKH126',
        'IKH118', 'IKH318', 'IKH327', 'IKH132', 'IKH324',
        'IKG321', 'IKH316', 'IKH329', 'IKH300', 'IKH314',
        'IKH326', 'IKP333', 'IKG321', 'ISM314' ]
    transkrip06409017 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD112',
        'IKD312', 'IKH123', 'IKH323', 'IKS104', 'IKS123',
        'IKS301', 'IKS304', 'IKS323', 'IUM263', 'IKP102',
        'IKP111', 'IKP311', 'IKS126', 'IKS327', 'ISM401',
        'UKW400', 'IKB206', 'IKB406', 'IKH331', 'IKP103',
        'IKP113', 'IKP303', 'IKS118', 'IKS318', 'ISM221',
        'IKP321', 'ISM404', 'IKB250', 'IKB450', 'IKP213',
        'IKH314', 'IKH326', 'IKH312', 'IUM314', 'IKH128',
        'IKH328', 'IKH119', 'IKH327', 'IUM332', 'IKH300',
        'IKP321', 'IKH314', 'IKH326', 'ISD314' ]
    transkrip06409019 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL135', 'IKL335',
        'IUM461', 'UBA402', 'IKB405', 'IKH113', 'IKH311',
        'IKH313', 'IKS413', 'UKT101', 'IKL343', 'IKD312',
        'IKH123', 'IKH323', 'IKS104', 'IKS123', 'IKS301',
        'IKS304', 'IKS323', 'IUM263', 'IKP102', 'IKP111',
        'IKP311', 'IKS126', 'IKS327', 'ISM401', 'UKW400',
        'IKB206', 'IKB406', 'IKH331', 'IKP103', 'IKP113',
        'IKP303', 'IKS118', 'IKS318', 'ISM221', 'IKP321',
        'ISM404', 'IKB250', 'IKB450', 'IKP213', 'IKH314',
        'IKH326', 'IUM314', 'IKH119', 'IKH300', 'IKP321',
        'IKH314', 'IKH326', 'IKP333', 'ISD314' ]
    transkrip06510001 = [ 'IKB411', 'IKL335', 'IKS413',
        'IKS126' ]
    transkrip06510015 = [ 'IKL335', 'IKS413', 'UKT101' ]
    transkrip06410004 = [ 'IKH111', 'IKL341', 'IKL141',
        'UBA402', 'IKH311', 'IKS413', 'UKT101', 'IKD112',
        'IKD312', 'IKS104', 'IKS301', 'IKS323', 'IUM263',
        'ISM401', 'IKS118', 'IKS318', 'ISM221', 'ISM403',
        'IKG101', 'IKG302', 'PDU212', 'IKH300' ]
    transkrip06510013 = [ 'IKH351', 'IKB411', 'IKL135',
        'IKL335', 'IUM461', 'UBA402', 'IKB405', 'IKH313',
        'IKS413', 'UKT101', 'IKD112', 'IKD312', 'IKH323',
        'IKS123', 'IKS301', 'IKS323', 'IKD313', 'ISM314',
        'ISL303', 'IKS108', 'IKS308', 'ISL304', 'ISM313',
        'IKS326', 'ISM316' ]
    transkrip06510008 = [ 'IKH351', 'IKH111', 'IKL341',
        'IKL141', 'IKB411', 'IKH151', 'IKL335', 'IUM461',
        'UBA402', 'IKH311', 'IKS413', 'UKT101', 'IKS301',
        'IKS323', 'IKS126', 'IKS327', 'ISM401', 'UKW400',
        'IKB206', 'ISM403', 'ISM404', 'IKD123', 'ISM314',
        'ISL304', 'ISO301', 'ISO101', 'ISM313', 'IKS319',
        'IKS326', 'IKB150' ]
    transkrip06510004 = [ 'IKH309', 'IKH351', 'IKH111',
        'IKL141', 'IKB411', 'IKL135', 'IKL335', 'IUM461',
        'UBA402', 'IKB405', 'IKH311', 'IKH313', 'IKS413',
        'IKD112', 'IKD312', 'IKS301', 'IKS126', 'IKS327',
        'ISM401', 'UKW400', 'IKB206', 'IKB406', 'ISM221',
        'ISM403', 'ISM404', 'IKD313', 'IKD123', 'ISM314',
        'ISL303', 'IKS308', 'ISL304', 'ISO301', 'ISO101',
        'ISM313', 'IKS319', 'IKS326', 'ISM114', 'IKS328',
        'ISA301', 'ISL302', 'ISM316' ]

    main('06407046', transkrip06407046)
    #main('06407004', transkrip06407004)
    main('06408018', transkrip06408018)
    main('06408021', transkrip06408021)
    main('06408029', transkrip06408029)
    main('06408032', transkrip06408032)
    main('06409002', transkrip06409002)
    main('06409003', transkrip06409003)
    main('06409004', transkrip06409004)
    main('06409017', transkrip06409017)
    main('06409019', transkrip06409019)
    main('06409022', transkrip06409022)
    main('06409025', transkrip06409025)
    main('06409032', transkrip06409032)
    main('06409033', transkrip06409033)
    main('06409036', transkrip06409036)
    main('06409040', transkrip06409040)
    main('06409042', transkrip06409042)
    main('06409045', transkrip06409045)
    main('06410004', transkrip06410004)
    main('06507005', transkrip06507005)
    main('06508006', transkrip06508006)
    main('06508007', transkrip06508007)
    main('06508009', transkrip06508009)
    main('06509005', transkrip06509005)
    main('06509006', transkrip06509006)
    main('06509008', transkrip06509008)
    main('06509010', transkrip06509010)
    main('06509012', transkrip06509012)
    main('06509013', transkrip06509013)
    main('06509017', transkrip06509017)
    main('06509023', transkrip06509023)
    main('06509025', transkrip06509025)
    main('06509105', transkrip06509105)
    main('06510001', transkrip06510001)
    main('06510004', transkrip06510004)
    main('06510008', transkrip06510008)
    main('06510013', transkrip06510013)
    main('06510015', transkrip06510015)
    '''

    daftarmhs = [ '06408021', '06408032', '06409017', '06409019', '06409022', '06409025', '06409032', '06409033', '06409036', '06409045', '06410002',
        '06410005', '06410008', '06410010', '06410013', '06410023', '06410027', '06508007', '06509012', '06509013', '06510007', '06510012',
        '06509110', '06411007' ] 

    print len(daftarmhs)
    '''
    main(daftarmhs[0])
    '''
    for mhs in daftarmhs:
        main(mhs)

