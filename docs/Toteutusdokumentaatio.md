### Toteutusdokumentaatio
Ohjelma koostuu matriisiluokasta ja jäsentäjäluokasta. Nimensä mukaisesti matriisiluokassa on toiminno matriisien laskuoperaatioille ja jäsentäjäluokassa toiminnot käyttäjän syötteen jäsennykselle. Käyttöliittymä on tekstipohjainen.

## Matrix-luokka

Matriisiluokasta löytyy toiminnot mm. matriisien determinantin laskemiselle, kerto-,vähennys-,yhteenlaskulle, käänteismatriisin määrittelemiselle, transpoosille sekä Gauss-Jordanin eliminaatiolle.

## FormulaParser-luokka

Jäsenninluokkasta löytyy toiminnot käyttäjän lausekkeiden jäsentämiselle. Metodissa parseExpression jäsennetään ensin löydetyt matriisit, tämän jälkeen käydään vielä läpi eri operaatiot mitä toteutetaan matriiseille, jonka jälkeen palautetaan vastauksena joko matriisi tai numero.


