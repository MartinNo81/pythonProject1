# Cvičení 1 - Součet vektorů
# Vytvořte vektor A, který bude naplněn samými jedničkami. Vytvořte vektor B, který bude naplněn samými dvojkami.
# Proveďte součet, rozdíl, vektorový součin a podíl těchto dvou vektorů.

import numpy as np
A = np.ones(shape=4, dtype=int)
B = np.full(shape=4, fill_value=2, dtype=int)
soucet= A+B
rozdil= A-B
soucin= A*B
podil= A/B
print("soucet: {0}\nrozdil: {1}\nsoucin: {2}\npodil: {3}".format(soucet,rozdil,soucin,podil))

# Cvičení 2 - Součet náhodných matic
# Vytvořte dvě matice o velikosti 100 na 100 a naplňte je náhodnými hodnotami.
# Poté tyto matice sečtěte a vizualizujte pomocí knihovny matplotlib příkazem imshow().

import numpy as np
import matplotlib.pyplot as plt
M_01 = np.random.randint(1,100,(100,100))
M_02 = np.random.randint(1,100,(100,100))
plt.imshow((M_01+M_02), cmap="Grays")
plt.show()

# Cvičení 3 - Znudlení obrázku
# Nahrajte si nějaký obrázek a proveďte jeho znudlení z 2D matice na 1D vektor. Zkuste tento vektor následně vizualizovat pomocí imshow.
# pouzijte spise reshape (1 radek, N sloupcu), flatten (N sloupcu) muze zpusobit problemy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
img = mping.imread('picture_grey.png')
R = img.reshape(1,-1)
plt.imshow(R)
plt.show()


# Cvičení 4 - Odbarvení obrázku
# Zkuste odbarvit obrázek - převod do odstínu šedi, co nejefektivnějším způsem v numpy.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
import cv2
image = cv2.imread('picture.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)


cv2.destroyAllWindows()

https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/


# Cvičení 5 - Indexy z podmínky dvou matice
# Mějmě dva vektory:
#
# a = [3, 1, 2, 4, 5, 4, 4, 3, 2]
# b = [3, 2, 3, 4, 2, 4, 4, 1, 1]
# Získejte seznam indexů, kde jsou hodnoty v oboru vektorů shodné. Nápověda: použijte funkci where.





# Cvičení 6 - Index z obrázku splňujících podmínku
# Nahrajte si obrázek a nalezněte indexy pixelů, které mají hodnotu větší, než průměrná hodnota pixelu v obrázku.
# Pokud nahrajete barevný obrázek pak proveďte ještě průměr z barev pixelu a poté získejte průměr z tohoto průměru.
# Pokud to není jasné, tak se prostě chovejte k obrázku, jako by byl pouze v odstínech šedi.






# Cvičení 7 - Skládání obrázků stackem
# Proveďte naskládání obrázků (nechám na vás jaký stack vyberete) a vizualizujte výsledek pomocí imshow.






