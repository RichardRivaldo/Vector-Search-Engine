import requests
from bs4 import BeautifulSoup

# fungsi konversi string menjadi list of char
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def webScrap() :
    # membuat web request untuk 2 halaman pertama dari website reuters
    page = requests.get('https://www.reuters.com/news/archive/indonesia').text
    page2 = requests.get('https://www.reuters.com/news/archive/indonesia?view=page&page=2&pageSize=10').text
    # mendefinisikan BeautifulSoup untuk masing-masing halaman
    soup = BeautifulSoup(page, 'lxml')
    soup2 = BeautifulSoup(page2, 'lxml')

    TLink = [] # variabel penampung semua link
    # untuk tiap class 'story', diambil link a href pertama yang ditemukan, kemudian diappend ke variabel TLink
    for list in soup.find_all('article', class_='story') :
        link = list.find('a')
        linkh = link['href']
        TLink.append('https://www.reuters.com'+linkh)
    # ulangi untuk halaman kedua
    for list in soup2.find_all('article', class_='story') :
        link = list.find('a')
        linkh = link['href']
        TLink.append('https://www.reuters.com'+linkh)

    # tinjau satu-satu link yang ada
    for linki in TLink :
        # buat web req dan definisikan BeautifulSoup untuk masing-masing link
        pagei = requests.get(linki).text
        soupi = BeautifulSoup(pagei, 'lxml')

        content = []  # variabel penampung konten paragraf
        # mencari headline
        for h1  in soupi.find_all('h1') :
            headline = h1.text
        # mecari paragraf yang ditandakan class 'Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x' sebagai konten
        for p in soupi.find_all('p', class_='Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x'):
            paragraph = p.text
            content.append(paragraph)

        # sedikit perbaikan terhadap judul yang tidak bisa dijadikan nama file
        headlist = Convert(headline)
        for i in range(len(headlist)) :
            if headlist[i] == ':' :
                headlist[i] = ''
            if headlist[i] == '?' :
                headlist[i] = ''
        headline = ''.join(headlist)

        # export file dengan nama headline dan konten content
        exportFile = open('../test/'+headline+'.txt',"w", encoding='utf-8')
        exportFile.write(' '.join(content))
        exportFile.close()


webScrap()