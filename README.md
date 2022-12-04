# LeakDetector
Pipa minyak memiliki span yang sangat panjang dari satu stasiun minyak ke stasiun minyak lainnya. Jika terjadi suatu kebocoran pada pipa minyak, maka pengecekan terhadap pipa dengan panjang lebih dari 50 km di bawah tanah akan sangat sulit untuk dilakukan.
Pembuatan model machine learning dapat membantu perusahaan untuk mendeteksi letak maupun tingkat kebocoran pada suatu pipa minyak. Hal ini dapat menurunkan potential revenue loss yang terjadi akibat kebocoran, mengurangi beban biaya pengecekan manual pada pipa minyak serta deteksi dini pada kebocoran pipa.
Output yang dihasilkan project ini adalah leak location dan leak rate dari sebuah pipa minyak.

## Persiapan data
Karena data lapangan sangat sulit untuk didapatkan, maka digunakan data sintetik yang berisi data-data yang dibutuhkan.
Karena data adalah sintetik, maka EDA seperti mengecek tipe data, data hilang, dll tidak perlu dilakukan karena data yang dibuat sudah mendekati ideal.

## Preprocessing data
Preprocessing yang dilakukan adalah melakukan data split untuk train dan test pada data output dan data input.

## Feature Engineering and Selection
Feature engineering yang dilakukan adalah membuat Scaling Layer yaitu layer yang di normalisasi berdasarkan input layer.

## Pemodelan dan Evaluasi
Secara garis besar, flowchart pemodelan dan evaluasi model dapat dilihat pada gambar dibawah.
![Metode Penelitian S2 - Page 15](https://user-images.githubusercontent.com/105503003/205515355-052ac30f-ebac-4ab0-ba4d-02feb3d293b2.png)

## Cara Penggunaan
Cara penggunaan secara detail dapat dilihat di Demo Notebook.

## Dataset
Input memerlukan 3 data yaitu delta pressure, leak rate, dan leak location 

## Kesimpulan
- Project ini menggunakan deep learning model untuk mencari leak location dan leak rate
- Deep learning lebih efisien daripada artificial neural network dalam memodelkan leak location dan leak rate

## Reference
- Pudjo Sukarno, dkk. 2007. Leak Detection Modeling and Simulation for Oil Pipeline with Artificial Intelligence Method.
https://ugm365-my.sharepoint.com/:b:/g/personal/aulia_r_365_ugm_ac_id/EZjeNpHYZ_RKtvVcvdg3fHQBFXijc4h21p6xUZApTYXiIA?e=fz4Nio
- Project Summary
https://ugm365-my.sharepoint.com/:b:/g/personal/aulia_r_365_ugm_ac_id/EYlWDKJ3x3dDpz-gItX8gRcB-uRkLufbmjbdUEA7mZ74dw?e=4viTl7
