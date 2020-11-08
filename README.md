# Algeo02-19094
**Tugas Besar 2 IF2123 Aljabar Linier dan Geometri** 

**Aplikasi Dot Product pada Sistem Temu-Balik Informasi (*Information Retrieval*)**

## Spesifikasi dan Permasalahan
* Membuat sebuah *search engine* dalam website lokal berbasis *Cosine Similarity* yang mampu menerima minimal 15 buah dokumen.
* Program menerima *search query* dan mengurutkan dokumen secara menurun berdasarkan tingkat similaritasnya.
* Dilakukan pembersihan dokumen terlebih dahulu dengan melakukan *stemming* dan pembersihan karakter-karakter yang tidak diperlukan.
* Program menampilkan dokumen yang telah diurutkan sebelumnya disertai dengan nilai similaritas setiap dokumen tersebut.

## Screenshot(s)

## Stacks
* Back-End: Python
    * Libraries: 
        * math, string, os, requests (Python)
        * NLTK (termasuk corpus dan wordnet)
        * Beautiful Soup
        * Lxml
        * Scikit-Learn
        * Pandas
        
* Front-End: Flask
   * Libraries :
        * Flask
        * Wtforms

## Setup
* Pastikan telah memiliki *library* dan *packages* yang digunakan. Jika NLTK tidak datang dengan lengkap, bisa dimasukkan kode `nltk.download('nama_package')` untuk mengunduh setiap package yang ada (lebih disarankan untuk menginstall NLTK sepenuhnya). Adapun untuk mendownload package yang berasal dari pip bisa dimasukkan kode `pip install ('nama_package')`.
* Jalankan kode-kode berikut untuk memastikan semua lib sudah terinstall:
   - pip install nltk
   - pip install lxml
   - pip install beautifulsoup4
   - pip install bs4
   - pip install flask
   - pip install flask-wtf

## Run
* Jalankan terminal, pindah ke direktori src dari git ini, dan ketik `python Main.py`, jika tidak ada error, berarti semua library terinstall dengan baik, copy link yang muncul, harusnya berupa http://127.0.0.1:5000/ , dan paste ke browser.

## Sources

## Author
* Billy Julius / 13519094
* Maximillian Lukman / 13519153
* Richard Rivaldo / 13519185
