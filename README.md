Dit python programma automatiseert het bijhouden van een marktplaats account met veel advertenties (>300). Elke dag wordt gekeken of advertenties op marktplaats verlopen zijn. Zo ja, worden de verlopen advertenties opnieuw geplaatst met behulp van de webscraping library selenium. Voor een nieuwe advertentie hoef je simpelweg alleen een nieuwe folder aan te maken met bechrijving en foto's. Deze wordt dan vanzelf online gezet.

Het programma maakt gebruik van de map 'fotos' en de text files "Beschrijving.txt" en "Categorie.txt". Het laatste bestand wordt gebruikt om de advertentie in de juiste categorie te plaatsen.

Indeling "Catergorie.txt":

Categorie 1--Categorie 2--Categorie 3--Conditie--Prijstype--Prijs*--Verzendoptie--

*Alleen als bij Prijstype 'Vraagprijs' is gekozen.

Verzendopties:

Klein = Past door bievenbus, 100-350g
Licht = Past door brievenbus, 0-2kg
Groot = Past niet door brievenbus, 0-10kg
Zwaar = Past niet door brievenbus, 10-23kg
