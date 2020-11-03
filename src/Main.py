# Memproses dokumen-dokumen beserta query yang dimasukkan

# Libraries

import os
import Read
import Preprocessing
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Ubah query menjadi list untuk divektorisasi
query = input()
query = Read.cleaning(query)
query = Read.token(query)
query = Preprocessing.stopwords(query)
query = Preprocessing.lemmatize(query)
#
#q = [q]
#qVec = vectorizer.transform(q).toarray().reshape(df.shape[0]) <- masih invalid bang lols

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
    content = Preprocessing.lemmatize(content)

    # Menggabungkan semua konten menjadi satu list
    contentList.append(content)

for content in contentList :
    for words in content :
        pass
        # do stuff for each word

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(contentList)
df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names())

print(df.head())
print(df.shape)