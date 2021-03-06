### Testausdokumentaatio

#### Suorituskykytestaus
* Testasin Matriisi-luokan metodeita 1x1-9x9 matriiseilla
* Testatut matriisit olivat porrasmatriiseja, joiden kaikki nollasta poikkeavat arvot ovat ykkösiä
* n tarkoittaa matriisin alkioiden lukumäärää, jos ei muuta sanota

##### Matriisin yhteen- ja vähennyslasku
* Testauksessa oli käytetty kahta identtistä matriisia
* Aikavaativuus algoritmilla on O(n)

![Matriisin yhteenlaskun kuva](yhteenlasku.jpeg)

##### Matriisin kertominen
* Testauksessa oli käytetty kahta identtistä matriisia
* Aikavaativuus algoritmilla on O(nmp), missä matriisit ovat nxm ja mxp

![Matriisin kertolaskun kuva](kertolasku.jpeg)

##### Matriisin determinantti
* Aikavaativuus algoritmille(n!)

![Determinantti kuva](determinantti.jpeg)

##### Matriisin transponointi
* Aikavaativuus algoritmille O(n)

![Transponointi kuva](transponointi.jpeg)

##### Gauss-Jordan eliminointi
* Aikavaativuus algoritmille O(n^3)

![Gauss-Jordan eliminointi kuva](gaussjordan.jpeg)

##### Matriisin inversio
* Inversiossa hyödynnettään Gauss-Jordanin eliminointia
* Aikavaativuus algoritmille O(n^3)

![Inversio kuva](inversio.jpeg)
