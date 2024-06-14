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
import matplotlib.image as mpimg

img = mpimg.imread('cloud.jpg')
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]
img_monochrome = sum((r*0.299, g*0.587, b*0.114))
img_reshape = img_monochrome.reshape(1,-1)
img_slice = img_reshape[:,10:50]
plt.imshow(img_slice, cmap="Grays")
plt.show()

# Cvičení 4 - Odbarvení obrázku
# Zkuste odbarvit obrázek - převod do odstínu šedi, co nejefektivnějším způsem v numpy.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

picture = mpimg.imread('fish.jpg')
picture_gray = np.ones((600,600,3),dtype=int)

picture_gray[:,:,0] = (picture[:,:,0] + picture[:,:,1] + picture[:,:,2])//3
picture_gray[:,:,1],picture_gray[:,:,2] = picture_gray[:,:,0],picture_gray[:,:,0]
plt.imshow(picture_gray)
plt.show()

# Cvičení 5 - Indexy z podmínky dvou matice
# Mějmě dva vektory:
#
# a = [3, 1, 2, 4, 5, 4, 4, 3, 2]
# b = [3, 2, 3, 4, 2, 4, 4, 1, 1]
# Získejte seznam indexů, kde jsou hodnoty v oboru vektorů shodné. Nápověda: použijte funkci where.

import numpy as np

a = [3, 1, 2, 4, 5, 4, 4, 3, 2]
b = [3, 2, 3, 4, 2, 4, 4, 1, 1]

A=np.array(a)
B=np.array(b)

indexy_stejnych_hodnot = np.where( A == B )
print(indexy_stejnych_hodnot)

# Cvičení 6 - Index z obrázku splňujících podmínku
# Nahrajte si obrázek a nalezněte indexy pixelů, které mají hodnotu větší, než průměrná hodnota pixelu v obrázku.
# Pokud nahrajete barevný obrázek pak proveďte ještě průměr z barev pixelu a poté získejte průměr z tohoto průměru.
# Pokud to není jasné, tak se prostě chovejte k obrázku, jako by byl pouze v odstínech šedi.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('fish.jpg')
prumer = np.average(img)
indexy_pixel_vetsi_prumeru = np.argwhere(img > prumer)
print(indexy_pixel_vetsi_prumeru)


# Cvičení 7 - Skládání obrázků stackem
# Proveďte naskládání obrázků (nechám na vás jaký stack vyberete) a vizualizujte výsledek pomocí imshow.

# vertical stack

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img01 = mpimg.imread('cloud.jpg')
img01_orez = img01[:,300:900]
img_02 = mpimg.imread('fish.jpg')

img_final = np.vstack((img01_orez,img_02))

plt.imshow(img_final)
plt.show()

# deep stack

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img01 = mpimg.imread('cloud.jpg')
img01_orez = img01[300:900,300:900]
img_02 = mpimg.imread('fish.jpg')

img_dstack = np.dstack((img01_orez,img_02))
r1=img_dstack[:,:,0]
g1=img_dstack[:,:,1]
b1=img_dstack[:,:,2]
r2=img_dstack[:,:,3]
b2=img_dstack[:,:,4]
g2=img_dstack[:,:,5]

img_monochrome = sum((r1*0.299, g1*0.587, b1*0.114,r2*0.299, g2*0.587, b2*0.114))
plt.imshow(img_monochrome, cmap="Grays")
plt.show()