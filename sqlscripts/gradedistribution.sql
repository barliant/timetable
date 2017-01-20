CREATE TABLE gradedistribution (
  semester TEXT(11) NOT NULL,
  prodi TEXT(3) NOT NULL,
  kode TEXT(6) NOT NULL,
  kuliah TEXT NOT NULL,
  kelas NUMBER NOT NULL,
  dosen TEXT NOT NULL,
  A NUMBER,
  Aminus NUMBER,
  Bplus NUMBER,
  B NUMBER,
  Bminus NUMBER,
  Cplus NUMBER,
  C NUMBER,
  D NUMBER,
  E NUMBER,
  INC NUMBER,
  NR NUMBER,
  MG NUMBER,
  W NUMBER,
  UW NUMBER
);

INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB451', 'Tugas Akhir II', 1, 'Syaifuddin', 0, 0, 2, 2, 1, 0, 2, 0, 0, 0, 0, 28, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKB206', 'Kreativitas dan innovasi', 1, 'M Najih', 0, 2, 4, 5, 4, 3, 17, 3, 0, 0, 0, 7, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKB406', 'Metodologi Penelitian', 1, 'Djasli Djamarus', 0, 0, 0, 3, 3, 1, 11, 8, 0, 0, 0, 8, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IUM461', 'Struktur Diskrit I', 1, 'Syandra Sari', 2, 0, 1, 2, 4, 3, 3, 14, 3, 0, 0, 5, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB405', 'Penulisan Ilmiah dan Laporan', 1, 'Djasli Djamarus', 0, 0, 3, 2, 0, 2, 6, 5, 1, 0, 0, 9, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH113', 'Praktikum Jaringan Komputer dan Keamanan', 1, 'Gatot Budi Santoso', 12, 6, 1, 4, 5, 5, 8, 5, 7, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKL341', 'Struktur Data & Algoritma', 1, 'Is Mardianto', 0, 0, 0, 2, 2, 0, 8, 6, 5, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH313', 'Jaringan Komputer dan Keamanan', 1, 'Adrian Sjamsul Qamar', 6, 1, 1, 2, 4, 3, 1, 3, 8, 0, 0, 7, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKD313', 'Manajemen Data dan Informasi Lanjut', 1, 'Djasli Djamarus', 0, 2, 0, 3, 1, 0, 6, 8, 3, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKL341', 'Struktur Data & Algoritma', 1, 'Mira Ziveria', 0, 1, 0, 3, 1, 2, 4, 4, 5, 0, 0, 6, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKB411', 'Konsep Teknologi Informasi dan Keamanan', 1, 'Agus Salim', 3, 2, 7, 4, 1, 3, 6, 8, 1, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH151', 'Praktikum Organisasi dan Arsitektur Komputer', 1, 'Gatot Budi Santoso', 13, 7, 1, 2, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH311', 'Sistem Operasi', 1, 'Anung B Ariwibowo', 5, 1, 1, 3, 0, 3, 9, 2, 0, 0, 0, 4, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKH313', 'Jaringan Komputer dan Keamanan', 1, 'Gatot Budi Santoso', 0, 0, 0, 0, 0, 2, 6, 5, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISD314', 'Teknik Data Mining', 1, 'Syandra Sari', 2, 0, 3, 5, 3, 9, 11, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH309', 'Pengelolaan Jaringan Komputer', 1, 'Gatot Budi Santoso', 2, 0, 5, 4, 1, 1, 3, 9, 1, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH342', 'Pengolahan Sinyal Dijital', 1, 'E SHINTA DEWI JULIAN', 0, 1, 3, 1, 3, 3, 7, 4, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS413', 'Technopreneurship', 1, 'Syaifuddin', 8, 7, 13, 8, 3, 9, 10, 1, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB600', 'Tugas Akhir', 1, 'Syaifuddin', 0, 0, 4, 8, 1, 0, 0, 0, 2, 0, 0, 11, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH111', 'Praktikum Sistem Operasi', 1, 'Gatot Budi Santoso', 3, 3, 3, 5, 3, 4, 6, 4, 2, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS327', 'Desain Perangkat Lunak', 1, 'Rr Setyo Ariane Is', 5, 2, 2, 9, 4, 5, 4, 1, 0, 0, 0, 6, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'ISM221', 'Ekonomi Informasi', 1, 'Edi Kuswandono', 1, 0, 0, 5, 0, 0, 1, 6, 3, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'UBA402', 'Internasionalisasi', 1, 'Mutmainatul Mardiyah', 2, 2, 3, 4, 7, 4, 2, 2, 0, 7, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKL141', 'Praktikum Struktur Data dan Algorithma', 1, 'Mira Ziveria', 8, 4, 4, 15, 6, 1, 2, 3, 0, 0, 0, 6, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH112', 'Praktikum Keamanan Sistem Operasi', 1, 'Gatot Budi Santoso', 0, 1, 0, 0, 0, 0, 1, 3, 6, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH310', 'Sistem Keamanan Jaringan', 1, 'Gatot Budi Santoso', 0, 1, 0, 4, 2, 1, 4, 3, 3, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'UKT101', 'Kuliah Kerja Lapangan', 1, 'Gatot Budi Santoso', 23, 5, 6, 3, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS323', 'Analisis dan Pemodelan Perangkat Lunak', 1, 'Rr Setyo Ariane Is', 2, 0, 1, 0, 1, 1, 4, 0, 0, 0, 0, 4, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH313', 'Jaringan Komputer dan Keamanan', 1, 'Adrian Sjamsul Qamar', 2, 0, 2, 2, 3, 0, 3, 1, 2, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKH323', 'Keamanan Informasi', 1, 'Anung B Ariwibowo', 0, 3, 0, 8, 7, 4, 3, 4, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKP303', 'Mobile Programming', 1, 'Dian Pratiwi', 0, 3, 1, 1, 2, 1, 5, 3, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKH351', 'Organisasi dan Arsitektur Komputer', 1, 'Binti Solihah', 1, 3, 1, 2, 1, 1, 7, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB450', 'Tugas Akhir I', 1, 'Syaifuddin', 0, 2, 1, 1, 7, 0, 5, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKL335', 'Dasar Pemrograman', 1, 'Syandra Sari', 0, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH323', 'Keamanan Informasi', 1, 'Is Mardianto', 0, 0, 0, 4, 0, 0, 1, 2, 0, 1, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB205', 'Metodologi Penelitian dan Penulisan Ilmiah', 1, 'Djasli Djamarus', 0, 0, 0, 0, 0, 3, 1, 1, 0, 0, 0, 5, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKH351', 'Organisasi dan Arsitektur Komputer', 1, 'AGUNG SEDIYONO', 0, 0, 0, 1, 2, 0, 3, 0, 2, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH318', 'Verifikasi dan Validasi Keamanan Informasi', 1, 'AGUNG SEDIYONO', 0, 0, 1, 2, 0, 0, 3, 2, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKS301', 'Interaksi Manusia Dan Komputer', 1, 'Dian Pratiwi', 7, 3, 1, 2, 1, 3, 3, 2, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS304', 'Metode Berorientasi Obyek', 1, 'ABDUL ROCHMAN', 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 0, 4, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH351', 'Organisasi dan Arsitektur Komputer', 1, 'Gatot Budi Santoso', 0, 0, 0, 0, 0, 0, 1, 1, 4, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP311', 'Pemrograman Berbasis Web', 1, 'Dian Pratiwi', 0, 1, 3, 3, 4, 0, 1, 2, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG101', 'Praktikum Grafika Komputer', 1, 'Binti Solihah', 1, 0, 0, 6, 2, 1, 4, 2, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISM404', 'Proyek Rekayasa', 1, 'AGUNG SEDIYONO', 3, 2, 3, 4, 1, 0, 1, 0, 0, 1, 0, 4, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH314', 'Sistem Pengendalian Akses', 1, 'Is Mardianto', 2, 2, 2, 5, 2, 1, 1, 2, 1, 1, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'PDU212', 'Teori Warna', 1, 'Dian Pratiwi', 1, 0, 1, 3, 0, 1, 4, 2, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKL343', 'Disain & Analisa Algoritma (MPM)', 1, 'ABDUL ROCHMAN', 0, 0, 0, 1, 0, 1, 4, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH312', 'Keamanan Sistem Operasi', 1, 'Gatot Budi Santoso', 0, 0, 1, 2, 2, 0, 1, 1, 3, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP321', 'Manajemen dan Kualitas Perangkat Lunak', 1, 'Anung B Ariwibowo', 5, 1, 1, 4, 0, 4, 1, 2, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH309', 'Pengelolaan Jaringan Komputer', 1, 'Gatot Budi Santoso', 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKL343', 'Disain & Analisa Algoritma (MPM)', 1, 'Djasli Djamarus', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISM403', 'Etika Agama Profesionalisme dan Legal', 1, 'M Najih', 0, 0, 0, 0, 2, 1, 3, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKD312', 'Manajemen Data dan Informasi', 1, 'Djasli Djamarus', 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKG302', 'Pengolahan Citra', 1, 'Ratna Shofiati', 1, 1, 0, 2, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH132', 'Praktikum Pengelolaan Jaringan Komputer', 1, 'Gatot Budi Santoso', 0, 0, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKL341', 'Struktur Data & Algoritma', 1, 'Djasli Djamarus', 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKP333', 'Cloud Computing', 1, 'Adrian Sjamsul Qamar', 2, 1, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKL335', 'Dasar Pemrograman', 1, 'Syandra Sari', 4, 0, 2, 9, 7, 8, 0, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG402', 'Grafika Komputer', 1, 'Binti Solihah', 0, 3, 0, 2, 3, 2, 0, 0, 1, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKH313', 'Jaringan Komputer dan Keamanan', 1, 'Gatot Budi Santoso', 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKB411', 'Konsep Teknologi Informasi dan Keamanan', 1, 'Agus Salim', 5, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH329', 'Pengelolaan Keamanan Informasi', 1, 'Machnizam Machnin', 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISO301', 'Pengelolaan Sistem Informasi', 1, 'Teddy Siswanto', 3, 1, 1, 2, 3, 0, 1, 0, 0, 1, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG302', 'Pengolahan Citra', 1, 'Dian Pratiwi', 0, 2, 1, 3, 2, 1, 2, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IIB205', 'Perilaku Organisasi', 1, 'SUHARSONO', 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISO101', 'Praktikum PSI', 1, 'Teddy Siswanto', 2, 3, 0, 5, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG321', 'Rekayasa Sistem Multimedia', 1, 'Ahmad Zuhdi', 2, 0, 4, 7, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'PDU212', 'Teori Warna', 1, 'Dian Pratiwi', 0, 0, 1, 2, 4, 2, 1, 0, 1, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISL304', 'Analisa Proses Bisnis', 1, 'Agus Salim', 4, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISM221', 'Ekonomi Informasi', 1, 'Anna Tohir', 7, 6, 0, 8, 13, 0, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IUM314', 'Kalkulus', 1, 'Syaifuddin', 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISM401', 'Manajemen Proyek Teknologi Informasi', 1, 'Syaifuddin', 3, 7, 10, 10, 6, 4, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH151', 'Praktikum Organisasi dan Arsitektur Komputer', 1, 'Gatot Budi Santoso', 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP113', 'Praktikum Bahasa Pemrograman', 1, 'Binti Solihah', 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG101', 'Praktikum Grafika Komputer', 2, 'Binti Solihah', 2, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH113', 'Praktikum Jaringan Komputer dan Keamanan', 1, 'Gatot Budi Santoso', 11, 2, 1, 3, 3, 3, 0, 0, 2, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISO101', 'Praktikum PSI', 1, 'Agus Salim', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG121', 'Praktikum Rekayasa Sistem Multimedia', 1, 'Dian Pratiwi', 3, 8, 7, 10, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IUM461', 'Struktur Diskrit I', 1, 'Syaifuddin', 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IUM461', 'Struktur Diskrit I', 1, 'Syaifuddin', 0, 0, 1, 2, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH318', 'Verifikasi dan Validasi Keamanan Informasi', 1, 'Adrian Sjamsul Qamar', 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISL304', 'Analisa Proses Bisnis', 1, 'Agus Salim', 5, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISM314', 'Audit Sistem Informasi', 1, 'Agus Salim', 1, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'ISM221', 'Ekonomi Informasi', 1, 'Edi Kuswandono', 1, 1, 1, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKG402', 'Grafika Komputer', 1, 'Dian Pratiwi', 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'IKS328', 'ITSM', 1, 'Ahmad Zuhdi', 2, 1, 5, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKL233', 'Pemodelan Geometri', 1, 'Ahmad Zuhdi', 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH342', 'Pengolahan Sinyal Dijital', 1, 'SUHARTATI AGOES', 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISM114', 'Praktikum Audit Sistem Informasi', 1, 'Agus Salim', 3, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISM114', 'Praktikum Audit Sistem Informasi', 1, 'Teddy Siswanto', 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKG101', 'Praktikum Grafika Komputer', 1, 'Ratna Shofiati', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH116', 'Praktikum Model dan Arsitektur Keamanan Informasi', 1, 'AGUNG SEDIYONO', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG102', 'Praktikum Pengolahan Citra', 1, 'Binti Solihah', 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH111', 'Praktikum Sistem Operasi', 2, 'Gatot Budi Santoso', 0, 0, 1, 3, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'ISD305', 'Rekayasa Data dan Pengetahuan', 1, 'Ahmad Zuhdi', 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'IKS308', 'Sistem Informasi Manajemen', 1, 'Teddy Siswanto', 1, 0, 1, 1, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IUM351', 'Statistik Dasar', 1, 'Syaifuddin', 0, 0, 0, 2, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IUM461', 'Struktur Diskrit I', 1, 'Syandra Sari', 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IUM263', 'Struktur Diskrit II', 1, 'Syandra Sari', 1, 0, 2, 2, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKS323', 'Analisis dan Pemodelan Perangkat Lunak', 1, 'Teddy Siswanto', 3, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISM314', 'Audit Sistem Informasi', 1, 'Agus Salim', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISL305', 'Business Intelligence', 1, 'Teddy Siswanto', 1, 0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'ISD312', 'Information Retrieval', 1, 'Syandra Sari', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS301', 'Interaksi Manusia Dan Komputer', 1, 'Teddy Siswanto', 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKB411', 'Konsep Teknologi Informasi dan Keamanan', 1, 'Agus Salim', 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKB206', 'Kreativitas dan innovasi', 1, 'M Najih', 0, 0, 1, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKB250', 'Kuliah Kerja Profesi', 1, 'M Najih', 3, 9, 7, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKB250', 'Kuliah Kerja Profesi', 1, 'M Najih', 0, 4, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'UKT300', 'Kuliah Usaha Mandiri Ilmu Teknik Terapan', 1, 'Binti Solihah', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISM316', 'Manajemen Pemasaran IT', 1, 'Anna Tohir', 4, 10, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'ISM401', 'Manajemen Proyek Teknologi Informasi', 1, 'Syaifuddin', 1, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'UKW400', 'Pancasila dan Kewarganegaraan', 1, 'Diny Luthfah', 0, 0, 0, 8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP302', 'Pemprog Berbasis Komponen', 1, 'ABDUL ROCHMAN', 2, 3, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'ISM313', 'Pengantar Audit Sistem Informasi', 1, 'Teddy Siswanto', 0, 0, 2, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISO301', 'Pengelolaan Sistem Informasi', 1, 'Agus Salim', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'ISL303', 'Pengetahuan Bisnis', 1, 'Anna Tohir', 5, 3, 2, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKG302', 'Pengolahan Citra', 1, 'Dian Pratiwi', 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS123', 'Praktikum Analisis dan Pemodelan Perangkat Lunak', 1, 'Anung B Ariwibowo', 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKS126', 'Praktikum Desain Perangkat Lunak', 1, 'Anung B Ariwibowo', 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKS126', 'Praktikum Desain Perangkat Lunak', 1, 'Anung B Ariwibowo', 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKL133', 'Praktikum Pemodelan Geometri', 1, 'Binti Solihah', 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP102', 'Praktikum Pemrograman Berbasis Komponen', 1, 'Anung B Ariwibowo', 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKP111', 'Praktikum Pemrograman Berbasis Web', 1, 'Dian Pratiwi', 0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH132', 'Praktikum Pengelolaan Jaringan Komputer', 1, 'Gatot Budi Santoso', 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKH109', 'Praktikum Pengelolaan Keamanan Informasi', 1, 'Is Mardianto', 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'SI', 'IKS108', 'Praktikum SIM', 1, 'Teddy Siswanto', 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'SI', 'IKS108', 'Praktikum SIM', 1, 'Teddy Siswanto', 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-2', 'TIF', 'IKG304', 'Seni Animasi', 1, 'Evan Maulana', 3, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-3', 'TIF', 'IKH311', 'Sistem Operasi', 1, 'ABDUL ROCHMAN', 0, 1, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2011-2012-4', 'TIF', 'IKH311', 'Sistem Operasi', 1, 'Anung B Ariwibowo', 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKH331', 'Sistem Terdistribusi', 1, 'ABDUL ROCHMAN', 1, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO gradedistribution VALUES ('2012-2013-1', 'TIF', 'IKS318', 'Verifikasi dan Validasi Perangkat Lunak', 1, 'ABDUL ROCHMAN', 0, 3, 1, 12, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0);

