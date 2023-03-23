#MEHMET KUTAY DÜNDAR

#08.03.2023 Ödev1

###Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

#Sayılar(Numbers):Sayısal değerleri tutarlar.Örnekleri integer ve float olabilir.
#String(str):Metinsel ifadeleri tutarlar.
#Listeler(Lists):Bileşik veri tipleridir.Bir liste içinde birden farklı veri tipi olabilir.
#Tuples:Listelere benzerler ancak en öenmli farkları sadece okunabililir olmaları yani arttırılmaz ya da güncellenemezler.
#Sözlük(Dictionary):Bir çeşit hash tablo türleridir.Sözlük anahtarları tüm pyhton tipleri olabilir ancak genellikle sayılar ve dizelerdir.

###Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#Kurs tamamlama yüzdesinde sayısal veri tipi kullanılmıştır.
#Kurs programındaki başlıklar string veri tipinde kullanılmıştır.
#Kurs programındaki tamamlandı anlamındaki işaretlerde boolean veri tipi kullanılmıştır.

###Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#İletişim alanında "İletişim" ve "Message" alanları boş ise "Lütfen bu alanı doldurun." şeklinde bir uyarı alıyoruz.



iletisim = input("İletişim:")
message = input("Message:")

if iletisim:
    print("Mesajınız başarıyla gönderildi.")
if message:
    print("Mesajınız başarıyla gönderildi.")
else:
    print("Lütfen bu alanı doldurunuz.")
