# Memproses dokumen-dokumen beserta query yang dimasukkan

# Libraries
from flask import Flask , render_template, url_for , flash , redirect
import os
import Read
import Preprocessing
import math
from form import QueryForm

# Menampung semua nama file ke dalam suatu variabel list fileList
fileList = []
for root, dirs, files in os.walk('../test', topdown=False):
    for name in files :
        dir = os.path.join(root,name).split('\\')  # Mengambil hanya nama filenya, tidak bersama direktori yang displit oleh \
        fileList.append(dir[1])

contentList = []
for name in fileList :
    # Menampung tiap konten dalam tiap file, melakukan cleaning, konversi ke token, menghapus stopword, dan lemmatize
    content = Read.readfile('../test/'+name)
    content = Read.cleaning(content)
    content = Read.token(content)
    content = Preprocessing.stopwords(content)
    content = Preprocessing.stemming(content)

    # Menggabungkan semua konten menjadi satu list
    contentList.append(content)

# Membuat variabel penampung kata-kata yang ada di dokumen
wordList = []
for content in contentList :
    for word in content :
        if word not in wordList :
            wordList.append(word)

# Membuat variabel penampung jumlah kemunculan tiap kata pada tiap data
mVec = [[0 for x in range(len(wordList))] for y in range(len(fileList))]
j = 0
for content in contentList :
    for word in content :
        for i in range(len(wordList)) :
            if word == wordList[i] :
                mVec[j][i] = mVec[j][i] + 1
    j = j + 1

def Search(query) :
    # Terima query, lakukan pembersihan dll ke query seperti ke database
    query = Read.cleaning(query)
    query = Read.token(query)
    query = Preprocessing.stopwords(query)
    query = Preprocessing.stemming(query)

    # Proses menghasilkan vektor q yang sudah dihilangkan kata berulang
    q2 = []
    for word in query :
        if word not in q2 :
            q2.append(word)
    num_q = [0 for x in range(len(q2))]
    for word in query :
        for i in range(len(q2)) :
            if word == q2[i] :
                num_q[i] += 1

    # Untuk setiap kata dari query yang muncul di database, simpan urutan ke berapanya
    qWord = []
    for word in query :
        for i in range(len(wordList)) :
            if word == wordList[i] :
                qWord.append(i)

    # Query bisa berulang, jadi dicatat juga kemunculan tiap kata di query yang muncul di database
    num_qWord =[0 for x in range(len(qWord))]
    for word in query :
        for i in range(len(qWord)) :
            if word == wordList[qWord[i]]:
                num_qWord[i] += 1

    # Menghitung similaritas
    sim = []
    for i in range(len(fileList)) :
        # Menghitung Dot Product
        dotProd = 0
        k = 0
        for idx in qWord :
            dotProd += mVec[i][idx] * num_qWord[k]   # num_qWord adalah jlh kemunculan pada query, mVec adalah jlh kemunculan pada data
            k +=1

        # Menghitung norma dari query
        sumQ = 0
        for l in num_q :
            sumQ += pow(l,2)
        normQ = float(math.sqrt(sumQ))

        # Menghitung norma dari data
        sumD = 0
        for j in range(len(wordList)) :
            sumD += pow(mVec[i][j],2)
        normD = float(math.sqrt(sumD))

        # Menghitung similaritas data sekarang dengan query, dan dimasukkan ke list similaritas
        currSim = float(dotProd/(normQ * normD))
        sim.append(currSim)

    #print(sim) # buat tes

    # Membuat array yang menampung judul dokumen dengan format yang telah dislice
    titleList = [Title[:-4] for Title in fileList]

    # Membuat array yang menampung kalimat pertama dari setiap 
    headList = []
    for titles in fileList:
        with open('../test/'+titles, encoding='utf-8') as f:
            head = f.read().split('.')
            headList.append(head[0] + '.')

    # Menginisialisasi Array 2D berisi perhitungan similarity, judul dokumen, dan kalimat pertama setiap dokumen
    processedFiles = [[0 for i in range(3)] for j in range(len(fileList))]

    # Memasukkan tingkat similarity tiap dokumen
    for i in range(len(sim)):
        processedFiles[i][0] = sim[i]

    # Memasukkan semua judul dokumen
    for i in range(len(fileList)):
        processedFiles[i][1] = titleList[i]

    # Memasukkan kalimat pertama dari setiap dokumen
    for i in range(len(headList)):
        processedFiles[i][2] = headList[i]

    # Mengurutkan array yang telah didapat dengan key berupa kolom pertama, yaitu tingkat similaritas
    # dari yang paling tinggi
    sortedProcessed = sorted(processedFiles, key = lambda keyCol:keyCol[0], reverse=True)

    #print(sortedProcessed)

    # Menginisialisasi list kosong untuk menampung proses selanjutnya
    processedLD = []

    # Memasukkan tiap atribut yang ada ke dalam sebuah dictionary dengan key berupa Similarity, Title, dan FirstSentence
    for articles in range(len(sortedProcessed)):
        with open(('../test/'+sortedProcessed[articles][1]+'.txt'), 'r', encoding='utf-8') as File: 
            contents = File.read()
        attributeDict = {"Similarity" : sortedProcessed[articles][0],
                        "Title" : sortedProcessed[articles][1],
                        "FirstSentence" : sortedProcessed[articles][2],
                        "Contents" : contents,
                        "ID" : "Doc" + str(articles+1)
                        }
        # Memasukkan tiap dictionary yang telah dihasilkan ke dalam list sebelumnya
        processedLD.append(attributeDict)

    return processedLD

# Inisiasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123abc123asiwh292rj'

posts = []

# Rute utama, utk query dan hasil searching
@app.route('/' , methods=['GET' , 'POST'])
def query():
    # Panggil QueryForm dari form.py
    form = QueryForm()
    # Jika ada query yang disubmit, lakukan proses search, dan oper ke query.html sebagai posts
    if form.validate_on_submit() :
        flash(f'Searching successed' , 'success')
        postQ = Search(form.query.data)
        return render_template('query.html' , posts = postQ, form = form)
    # Jika tidak ada (pertama kali) , hasil searching tampilkan kosong
    return render_template('query.html' , posts = posts, form = form)

# Rute untuk tiap artikel
@app.route('/article/<id>')
def article(id):
    return render_template("article.html")


if __name__ == '__main__':
    app.run(debug=False)
