''' coloring.py

Eksperimen membuat susunan jadwal menggunakan model Graph Coloring.
Perhatikan bahwa Graph Coloring Problem is known to be NP-Complete.
Karena dari itu, mungkin solusi yang didapatkan membutuhkan waktu yang
cukup lama, sesuai dengan peningkatan jumlah verteks (yakni mata
kuliah).


Modelling:

Setiap mata kuliah diwakili oleh sebuah verteks. Antara satu verteks
dengan verteks lain terdapat sebuah edge jika ada People (Dosen atau
Mahasiswa) yang mengajar (atau mengambil) kedua verteks tersebut.

Nilai $k$ (chromatic number) dari graf yang terbentuk adalah jumlah
minimum slot waktu yang harus dijadwalkan.


Anung B. Ariwibowo (barliant@gmail.com)
20141218

* 20141218
  * Studi kasus pada penjadwalan Semester Pendek PPHB Gasal
    2014/2015.
'''

__author__ = 'Anung B. Ariwibowo'

import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import xlwt
import numpy as np

import getpass


def main():
    G = nx.Graph()

    wb = xlrd.open_workbook('../raw-data/kelas-2014-2015-2.xls')
    wb_out = xlwt.Workbook()
    sheet_out = wb_out.add_sheet('jadwal')

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
    krs = {}
    for rowidx in range(1, sheet.nrows-1):
        nim = data['NIM'][rowidx]
        kode = data['Kode'][rowidx]
        #print nim, kode
        if krs.has_key(nim):
            krs[nim].append(kode)
        else:
            krs[nim] = [kode]
    for nim in krs:
        if len(krs[nim]) > 1:
            for kode in krs[nim]:
                for other in krs[nim]:
                    if kode != other:
                        G.add_edge(kode, other)
    #print "Edges  : ", G.edges()
    print "Degrees: ", nx.degree(G)
    color_list = []

    for key, value in sorted(nx.degree(G).iteritems(), key=lambda(k, v): (v, k), reverse=True):
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
    sheet_out.write(0, 0, 'Kode')
    sheet_out.write(0, 1, 'Color')
    rowidx = 1
    colidx = 0
    for lecture in color_list:
        #print lecture, G.node[lecture]['color']
        sheet_out.write(rowidx, colidx+0, lecture)
        sheet_out.write(rowidx, colidx+1, G.node[lecture]['color'])
        rowidx = rowidx + 1
    wb_out.save('../raw-data/jadwal-2014-2015-2.xls')

    #nx.draw_networkx(G, pos=nx.spring_layout(G))
    #nx.draw_networkx(G, pos=nx.spectral_layout(G))
    nx.draw_networkx(G, pos=nx.circular_layout(G))
    plt.show()



if __name__ == '__main__':
    main()

