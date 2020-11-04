# Memproses dokumen-dokumen beserta query yang dimasukkan

# Libraries

import os
import Read
import Preprocessing
import pandas as pd
import math
from numpy import *
from sklearn.feature_extraction.text import TfidfVectorizer


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

mVec = [[0 for x in range(len(wordList))] for y in range(len(fileList))]


j = 0
for content in contentList :
    for word in content :
        for i in range(len(wordList)) :
            if word == wordList[i] :
                mVec[j][i] = mVec[j][i] + 1
    j = j + 1

mVec = reshape(mVec,(len(fileList), len(wordList)))

# Terima query, lakukan pembersihan dll ke query seperti ke database
query = input()
query = Read.cleaning(query)
query = Read.token(query)
query = Preprocessing.stopwords(query)
query = Preprocessing.stemming(query)

# Ubah query menjadi suatu list
q = [query]

# Proses menghasilkan vektor q yang sudah dihitung kata berulang
q2 = []
for word in q[0] :
    if word not in q2 :
        q2.append(word)
num_q = [0 for x in range(len(q2))]
for word in q[0] :
    for i in range(len(q2)) :
        if word == q2[i] :
            num_q[i] += 1

# Tampung setiap kata dari query yang muncul di database, simpan urutan ke berapanya
qWord = []
for word in q[0] :
    for i in range(len(wordList)) :
        if word == wordList[i] :
            qWord.append(i)

# Query bisa berulang, jadi dicatat juga kemuncula tiap kata di query yang muncul di database
num_qWord =[0 for x in range(len(qWord))]
for word in q[0] :
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

    # Menghitun norma dari query
    sumQ = 0
    for l in num_q :
        sumQ += pow(l,2)
    normQ = math.sqrt(sumQ)

    # Menghitung norma dari data
    sumD = 0
    for j in range(len(wordList)) :
        sumD += pow(mVec[i][j],2)
    normD = math.sqrt(sumD)

    # Menghitung similaritas data sekarang dengan query, dan dimasukkan ke list similaritas
    currSim = float(dotProd/(normQ * normD))
    sim.append(currSim)

print(sim) # buat tes