# Vowel_Restoration_Hidden_Markov_Model
## DERLEM
Projede, Yıldız Teknik Üniversitesi Bilgisayar Mühendisliği bölümündeki akademisyenler tarafından kurulmuş Kemik Doğal Dil İşleme Grubu tarafından toplanmış gazete köşe yazıları kullanılmıştır. Toplam 2500 köşe yazısı bulunmaktadır ve bu köşe yazılarının konuları çeşitlilik göstermektedir.

## ÖN İŞLEME
Ayrık halde bulunan köşe yazıları tek bir dosyada birleştirilmiştir. Birleştirilen dosya içinde bulunan bütün büyük harfli kelimeler küçük harfe çevrilmiş, içerisinde rakam ve yabancı karakter (İngilizce de bulunan x w gibi) bulunan kelimeler çıkarılmıştır. Ayrıca bütün noktalama işaretleri elimine edilmiş ve şapkalı ünlüler şapkasız hale dönüştürülmüştür.

## İŞLEM ADIMLARI
Türkçede 29 harf bulunmaktadır. Bu harflerin 8'i seslidir. Sesli Harf Tamamlama projesinde Türkçe harflerin dışında ‘<’, ‘>’ ve ‘w’ karakterleri kullanılmıştır. ‘<’ karakteri kelimenin başlangıcını, ‘>’ karakteri kelimenin bitişini, ‘w’ karakteri ise boşluğu (hiçbir karakterin gelmeyeceğini) ifade eder. ‘<’ ve ‘>’ karakterler sessiz harf kategorisine, w ise sesli harf kategorisine koyulmuştur.

- Hazırlanmış derlem içerisindeki kelimeler okunmuştur.
- Kelimelerin başlangıç ve bitişlerinin belirlenebilmesi için her bir kelimenin başına ve sonuna başlangıç ve bitişi belirtecek karakterler eklenmiştir.

<p align="center">
	elma --> <elma>
	armut --> <armut>
</p>

- Kullanıcı tarafından girilmiş sessiz harflerden sonra gelecek sesli harflerin bulunması gerekmektedir. Bu işlemin belirlenmesinde karakter bigramları kullanılmıştır. Karakter bigramlarının içerisinde bulunan karakterlerin birlikte geçme sayıları belirlenmiştir.

<p align="center">
	<kaya> --> ‘<k’, ‘ka’, ‘ay’, ‘ya’, ‘a>’
</p>

- Bigramların oluşma durumu şu şekildedir. ‘Sesli harf – sessiz harf’, ‘sesli harf – sesli harf’, ‘sessiz harf – sesli harf’ ve ‘sessiz harf – sessiz harf’. Hidden Markov Model oluşturulurken her sessiz harf sonrasında bir sesli harfin geleceği varsayılmıştır. Ancak Türkçe’de iki sessiz harf yan yana gelebilmektedir. Bu durumu oluşturmuş modele uyarlayabilmek için boşluk karakterini (w) kullanılmıştır.

<p align="center">
	<gömlek> --> ‘<g’, ‘gö’, ‘öm’, ‘mw’, ‘wl’, ‘le’, ‘ek’, ‘k>’
</p>

- Karakterlerin birbiri ile geçme sayıları bulunduktan sonra olasılıkları hesaplanmıştır.
- Kullanıcıdan sessiz harf girişi alınmış ve girilen sessiz harf dizgesinin başına ve sonuna ‘<’ ve ‘>’ karakterleri eklenmiştir.

<p align="center">
	<img src="/image/hmm.JPG" alt="Hidden Markov Model" width="400" height="120">
</p>

- Hidden Markov Model (HMM) için başlangıç durum olasılığı 1 olarak belirlenmiştir. Kullanıcı hangi sessiz harfi yazarsa yazsın ilk karakter her zaman ‘<’ olarak atanacaktır. Bu sebeple başlangıç durum 1 olarak seçilmiştir.
- HMM’de sessiz harfler durumları, sesli harfler gözlemlenebilir değişkenleri ifade etmektedir.
- HMM formülünde, durumların birbiri ardına gelme olasılıkları hesaplanmaktadır. Ancak bütün oluşturulabilecek sesli harf kombinasyonlarında sessiz harflerin birbiri ardında bulunma olasılıklarının aynı olması sebebiyle olasılık hesabında bu değer göz ardı edilmiştir.
- Türkçe’de 3 sessiz harfin art arda gelme olasılığı çok düşüktür. Oluşturulan yapıda art arda 3 sessiz harfin gelebilmesi için art arda 2 ‘w’ boşluk karakteri gelmelidir. Art arda 2 boşluk karakterinin gelme olasılığını düşürebilmek için hesaplanan olasılık belirli bir kat sayıya bölünmüştür.
- Türkçe’de ‘ğ’ ile başlayan bir kelime bulunmamaktadır. Bu durum ayrıyeten kontrol edilmiştir. Başlangıç karakterinden sonra ğ karakteri gelmesi durumunda (kullanıcının ilk olarak ğ girmesi) boşluk karakterinin gelmesi engellenmiştir.
- Her bir adımda en yüksek olasılığa sahip olan sesli harf dizgesi ve olasılığı üzerinden işlem yapılmıştır.

## PROGRAM ÇALIŞTIRIlMASI
- Projeyi indirdiğiniz dizine gidiniz.
- Konsol ekranını açınız ve “python main.py” komutunu çalıştırınız.

## OUTPUT
[Örnek sonuçlar için tıklayınız.](/output)