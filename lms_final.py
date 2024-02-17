open("books.txt",mode="a+",encoding="utf-8")

class Library:
    def __init__(self,book_title,book_author,release,numberofpage):
        self.book_title=book_title
        self.book_author=book_author
        self.release=release
        self.numberofpage=numberofpage
        
    def list_books(self):
        print("Kitap adi:"+self.book_title+"         Kitap yazari:"+self.book_author+"\n")


    def add_books(self):
        file=open("books.txt",mode="a+",encoding="utf-8")
        icerik=self.book_title+","+self.book_author+","+self.release+","+self.numberofpage+"\n"
        file.write(icerik)


    def remove_books(self,content_):
        try:
            content_=content_.splitlines()
            satir_no=0
            for i in content_:
                i=i.split(",")
                if book_title_del==i[0]:
                    print(i[0]+" isimli kitabın silme işlemi gerçekleşmiştir")
                    break
                satir_no+=1
            del content_[satir_no]
            file=open("books.txt",mode="w",encoding="utf-8")
            for i in content_:
                i=i.split(",")
                lib=Library(i[0],i[1],i[2],i[3])
                lib.add_books()
        except:
            print("Yanlış girdiniz.Listedeki kayıtlı  kitaplardan seçmelisiniz...")

        

while True:
    
         
    
    inp=input("##   MENU    ##\n1)List Books\n2)Add Book\n3)Remove Book\nCikis icin Q tusuna basiniz...")

    if inp=='q' or inp=='Q':
            break

    elif inp=="1":
        file=open("books.txt",mode="r",encoding="utf-8")
        satirlar=file.read()
        satirlar=satirlar.splitlines()
        for i in satirlar:
            i=i.split(",")
            lib=Library(i[0],i[1],i[2],i[3])
            lib.list_books()


    elif inp=="2":
        
        book_title_=input("Kitap adini giriniz:")
        book_author_=input("Kitabin yazarini giriniz:")
        release_=input("Kitabin  yayinlanma tarihini giriniz:")
        numberofpage_=input("Kitabin  sayfa sayisini giriniz:")
        lib=Library(book_title_,book_author_,release_,numberofpage_)
        lib.add_books()


    elif inp=="3":
        book_title_del=input("Silmek istediğiniz kitap adini giriniz:")
        file=open("books.txt",mode="r",encoding="utf-8")
        content_=file.read()
        #print(content_)
        Library.remove_books(None,content_)

    elif inp!='q' or inp!='Q' or inp!="1" or inp!="2" or inp!="3":
        print("Lütfen gösterilen seçeneklerden bir tanesini giriniz...")

        