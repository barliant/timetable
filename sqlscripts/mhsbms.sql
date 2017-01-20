-- Anung Ariwibowo
-- 01 Desember 2014
-- Meng-export data mahasiswa BMS


.header ON
.mode csv
.separator ";"
.output ../raw-data/kuliahUlang.csv
---.output mhsBMS.csv

SELECT kode, nama, COUNT(nim) AS jml
FROM coursestaken
WHERE nim IN ('06407046', '06407004',
  '06407029', '06407040', '06507005',
  '06508009', '06408029', '06408018',
  '06409002', '06509006', '06509023',
  '06509017', '06509110', '06509012',
  '06510001', '06510015')
  AND grade IN ('D', 'E')
GROUP BY kode, nama
HAVING COUNT(nim) >= 5
ORDER BY 3 DESC;


.mode list
.output stdout
.separator "|"

