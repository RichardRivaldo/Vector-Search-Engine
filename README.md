# Algeo02-19094
**Tugas Besar 2 IF2123 Aljabar Linier dan Geometri** 

**Aplikasi Dot Product pada Sistem Temu-Balik Informasi (*Information Retrieval*)**

## Spesifikasi dan Permasalahan
* Membuat sebuah *search engine* dalam website lokal berbasis *Cosine Similarity* yang mampu menerima minimal 15 buah dokumen.
* Program menerima *search query* dan mengurutkan dokumen secara menurun berdasarkan tingkat similaritasnya.
* Dilakukan pembersihan dokumen terlebih dahulu dengan melakukan *stemming* dan pembersihan karakter-karakter yang tidak diperlukan.
* Program menampilkan dokumen yang telah diurutkan sebelumnya disertai dengan nilai similaritas setiap dokumen tersebut.
* Selain itu, juga akan ditampilkan tabel frekuensi dari tiap *term* yang dimasukkan sebagai *query* saat pencarian.

## Stacks
* Back-End: Python
    * Libraries: 
        * Python Built-In Libraries (math, string, os, requests)
        * NLTK
        * Beautiful Soup
        * Lxml
        
* Front-End: Flask
   * Libraries :
        * Flask
        * Wtforms
        * Werkzeug

## Setup
* Pastikan telah memiliki *library* dan *packages* yang digunakan. Jika NLTK tidak datang dengan lengkap, bisa dimasukkan kode `nltk.download('nama_package')` untuk mengunduh setiap package yang ada (lebih disarankan untuk menginstall NLTK sepenuhnya). Adapun untuk mendownload package yang berasal dari pip bisa dimasukkan kode `pip install ('nama_package')`.
* Jalankan kode-kode berikut untuk memastikan semua lib sudah terinstall:
   - pip install nltk
   - pip install lxml
   - pip install beautifulsoup4
   - pip install bs4
   - pip install flask
   - pip install flask-wtf
   - pip install werkzeug

## Run
* Jalankan Terminal atau Command Prompt dan pindah ke direktori src dari git ini (dalam Windows, bisa dijalankan perintah `cd/direktori_yang_ingin_dituju`.
* Jalankan program dengan cara menginput `python Main.py`.
* Jika tidak ada error, akan muncul sebuah link *localhost*, biasanya berupa http://127.0.0.1:5000/ dan program akan berjalan.
* Masukkan link tersebut ke dalam mesin pencari atau *browser*.
* Ketika program dijalankan, maka pastikan Terminal tetap terbuka dan program masih tetap berjalan.

## Sources
* All You Need to Know About Text Preprocessing for NLP and Machine Learning in https://www.kdnuggets.com/2019/04/text-preprocessing-nlp-machine-learning.html.
* Flask Tutorials by Corey M. Schafer on YouTube.
* NLP: Building Text Cleanup and PreProcessing Pipeline in https://towardsdatascience.com/nlp-building-text-cleanup-and-preprocessing-pipeline-eba4095245a0
* NLTK 3.5 Documentation in https://www.nltk.org/.
* Text Preprocessing in Python: Steps, Tools, and Examples in https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908.

## Author
* Billy Julius / 13519094
* Maximillian Lukman / 13519153
* Richard Rivaldo / 13519185
