# Razlaga ***CFIT***

> ## fprlib.cfit(\<funkcija\>, \<X podatki\>, \<Y podatki\>, \<imena spremenljivk\>=None, \<začetne vrednosti\>=None)

### Obvezne spemenljivke:

1. \<funkcija\> : Vstavi funkcijo oziroma njeno "ime" ampak ***obvezno brez citatov!***
2. \<x podatki\> : Vstavi seznam X koordinat meritev.
3. \<y podatki\> : Vstavi seznam Y koordinat meritev.

### Neobvezne spremeljike:

1. \<imena spremenljivk\> : Seznam imen spremenljivk v funkciji, v primeru da seznam ni podan, bodo spremenljivke oštevilčene.
2. \<začetne vrednosti\> : Seznam začetnih vrednosti, ki jih uporabi program za oceno. ***Sicer neobvezno, se lahko pokaže, da program vrne slab fit, če niso začetne vrednosti dobro uganjene!***

## Funkcija:

Da bi naš program lahko karkoli računal moramo predpisati fizikalno funkcijo, za katero menimo, da lepo opiše pojav. Opmnimo, da so imena spremenljivk poljubna, vendar če se nekje uporabi spremenljivka z istim imenom, posledično pomeni, da ti dve vrednosti morata biti enaki:

> def \<funkcija\>(x, a, b, c, d)
>    
>‎return f(x,a,b,c,d)

nato moramo definirati podatke za x in y v obliki *python seznama (list-a)*.
Dodatno lahko definiramo še imena spremenljivk v seznamu, npr.:

> sez = ["prva spremenljivka" , "druga_spremeljivka", "tretja spremenljivka", "karkoli_kakorkoli", 1 ]

***Opomba*** : določeni znaki niso dovoljeni. Npr.: "-".

***Opomba*** : knjižnica avtomatično umakne presledke iz vseh besedil, seveda pa prej vse pretvori v besedila, kakor preveri če je ime spremenljivke podvojeno!

ter definiramo seznam začetnih vrednosti npr.:

> p = [ 1 , 2 , 3 , 4.231E-3 ]

***Opomba*** : na prvem mestu v seznamih "sez" in "p" mora biti ime oz. začetna vrednost, ki odgovarja spremenljivki "a" iz formule, ter na drugem mestu teh seznamov vrednosti, ki pripadajo spremenljivki "b" iz formule.
