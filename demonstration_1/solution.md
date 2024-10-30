## Static

_Note: Ce challenge vient de crackmes.one_

Tout d'abord, `strings` ne retourne rien

Ensuite, on remarque un xor avec 3. De plus, l'array en entrée est de taille 0x20. On adapte le type.

Utiliser ```pwn.xor(b'ag7`124504a`;1;:;1`3:3a1gf72a;7g', '\x03' * 0x20)``` pour retrouver le mot de passe

## Dynamic

_Note: Ce challenge vient de crackmes.one_

On voit rapidement dans Ghidra que le programme modifie des trucs en mémoire puis demande où est le flag. C'est probablement à cet endroit.

Ouvrir avec gdb (GEF)
1. `b main`
2. Avancer jusqu'à récupération du pointeur (malloc)
3. `b *main+216`
4. `telescope <pointeur>`
5. Récupérer flag

