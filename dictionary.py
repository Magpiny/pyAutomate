import pprint
info = {'name': 'Joy', 'age': 18}

# print(info.items())
for k, v in info.items():
    print(f"{k} : {v}", end=" ")

mssg = "I love coding and soccer that i can alternate them everyday for 365 days without getting bored"
word = '''In the beginning God created the heavens and the earth. 2Now the earth was formless and empty, darkness was 
over the surface of the deep, and the Spirit of God was hovering over the waters. 3And God said, “Let there be light,
” and there was light. 4God saw that the light was good, and he separated the light from the darkness. 5God called 
the light “day,” and the darkness he called “night.” And there was evening, and there was morning—the first day. 6And 
God said, “Let there be a vault between the waters to separate water from water.” 7So God made the vault and 
separated the water under the vault from the water above it. And it was so. 8God called the vault “sky.” And there 
was evening, and there was morning—the second day. 9And God said, “Let the water under the sky be gathered to one 
place, and let dry ground appear.” And it was so. 10God called the dry ground “land,” and the gathered waters he 
called “seas.” And God saw that it was good. 11Then God said, “Let the land produce vegetation: seed-bearing plants 
and trees on the land that bear fruit with seed in it, according to their various kinds.” And it was so. 12The land 
produced vegetation: plants bearing seed according to their kinds and trees bearing fruit with seed in it according 
to their kinds. And God saw that it was good. 13And there was evening, and there was morning—the third day. 14And God 
said, “Let there be lights in the vault of the sky to separate the day from the night, and let them serve as signs to 
mark sacred times, and days and years, 15and let them be lights in the vault of the sky to give light on the earth.” 
And it was so. 16God made two great lights—the greater light to govern the day and the lesser light to govern the 
night. He also made the stars. 17God set them in the vault of the sky to give light on the earth, 18to govern the day 
and the night, and to separate light from darkness. And God saw that it was good. 19And there was evening, 
and there was morning—the fourth day. 20And God said, “Let the water teem with living creatures, and let birds fly 
above the earth across the vault of the sky.” 21So God created the great creatures of the sea and every living thing 
with which the water teems and that moves about in it, according to their kinds, and every winged bird according to 
its kind. And God saw that it was good. 22God blessed them and said, “Be fruitful and increase in number and fill the 
water in the seas, and let the birds increase on the earth.” 23And there was evening, and there was morning—the fifth 
day. 24And God said, “Let the land produce living creatures according to their kinds: the livestock, the creatures 
that move along the ground, and the wild animals, each according to its kind.” And it was so. 25God made the wild 
animals according to their kinds, the livestock according to their kinds, and all the creatures that move along the 
ground according to their kinds. And God saw that it was good. 26Then God said, “Let us make mankind in our image, 
in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all 
the wild animals, and over all the creatures that move along the ground.” 27So God created mankind in his own image, 
in the image of God he created them; male and female he created them. 28God blessed them and said to them, 
“Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the 
sky and over every living creature that moves on the ground.” 29Then God said, “I give you every seed-bearing plant 
on the face of the whole earth and every tree that has fruit with seed in it. They will be yours for food. 30And to 
all the beasts of the earth and all the birds in the sky and all the creatures that move along the ground—everything 
that has the breath of life in it—I give every green plant for food.” And it was so. 31God saw all that he had made, 
and it was very good. And there was evening, and there was morning—the sixth day. 1Thus the heavens and the earth 
were completed in all their vast array. 2By the seventh day God had finished the work he had been doing; so on the 
seventh day he rested from all his work. 3Then God blessed the seventh day and made it holy, because on it he rested 
from all the work of creating that he had done. Adam and Eve 4This is the account of the heavens and the earth when 
they were created, when the LordGod made the earth and the heavens. 5Now no shrub had yet appeared on the earth and 
no plant had yet sprung up, for the LordGod had not sent rain on the earth and there was no one to work the ground, 
6but streams came up from the earth and watered the whole surface of the ground. 7Then the LordGod formed a man from 
the dust of the ground and breathed into his nostrils the breath of life, and the man became a living being. 8Now the 
LordGod had planted a garden in the east, in Eden; and there he put the man he had formed. 9The LordGod made all 
kinds of trees grow out of the ground—trees that were pleasing to the eye and good for food. In the middle of the 
garden were the tree of life and the tree of the knowledge of good and evil. 10A river watering the garden flowed 
from Eden; from there it was separated into four headwaters. 11The name of the first is the Pishon; it winds through 
the entire land of Havilah, where there is gold. 12(The gold of that land is good; aromatic resin and onyx are also 
there.) 13The name of the second river is the Gihon; it winds through the entire land of Cush. 14The name of the 
third river is the Tigris; it runs along the east side of Ashur. And the fourth river is the Euphrates. 15The LordGod 
took the man and put him in the Garden of Eden to work it and take care of it. 16And the LordGod commanded the man, 
“You are free to eat from any tree in the garden; 17but you must not eat from the tree of the knowledge of good and 
evil, for when you eat from it you will certainly die.” 18The LordGod said, “It is not good for the man to be alone. 
I will make a helper suitable for him.” 19Now the LordGod had formed out of the ground all the wild animals and all 
the birds in the sky. He brought them to the man to see what he would name them; and whatever the man called each 
living creature, that was its name. 20So the man gave names to all the livestock, the birds in the sky and all the 
wild animals. But for Adam no suitable helper was found. 21So the LordGod caused the man to fall into a deep sleep; 
and while he was sleeping, he took one of the man’s ribs and then closed up the place with flesh. 22Then the LordGod 
made a woman from the rib he had taken out of the man, and he brought her to the man. 23The man said, “This is now 
bone of my bones and flesh of my flesh; she shall be called ‘woman,’ for she was taken out of man.” 24That is why a 
man leaves his father and mother and is united to his wife, and they become one flesh. 25Adam and his wife were both 
naked, and they felt no shame. The Holy Bible, New International Version® NIV® 

Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®

Used by Permission of Biblica, Inc.® All rights reserved worldwide.

Learn more about New International Version

       '''
count = {}
for chars in word.upper():
    count.setdefault(chars, 0)
    count[chars] += 1
pprint.pprint(count)
