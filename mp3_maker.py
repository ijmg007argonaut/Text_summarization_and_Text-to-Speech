# at command line use "pip install gTTS"
from gtts import gTTS
import os

# make Shark_Abstract_Sum.txt file into an mp3
mytext1 = (""" mythology often posits that the 50-foot predator has been hiding
for epochs somewhere at the bottom of the ocean. 'if megalodon is still out there
(and that’s a pretty big if), it’s not what it used to be,' says a researcher. in 1875,
during an expedition for the royal society of London, the HMS Challenger dredged up 4-inch-long
teeth from a depth of 14,000 feet near Tahiti """)
audio = gTTS(text=mytext1, lang="en", slow=False)
audio.save("Shark_Abstract_Sum.mp3")

# make Shark_Extract_Sum.txt file into an mp3
mytext2 = (""" While paleontologists are almost certain megalodon doesn’t swim in our modern seas, they might still
find more details about the species in the depths of the fossil record—and its enduring secrets could
break the surface when we least expect. The ongoing earthly presence of the enormous shark persists in
our collective imagination thanks to rumors, legends, and summer B flicks.Meg mythology often posits that
the 50-foot predator has been hiding for epochs somewhere at the bottom of the ocean. If the megalodon
were living in the dark, inky depths, though, it would have had to become a very different sort of
creature—one we might not find nearly as cinematic. Yet animals near the ocean floor have to get by
on teensy scraps, preying on the scant species that live there or hoovering up biological detritus
that sinks down from carcasses above.Megalodon was a massive fish, but it wasn’t the biggest predator
ever seen in the seas. Its mysterious nature—what we know of it comes largely from studying
teeth—makes it enticing to imagine the Meg’s pulled off the ultimate vanishing act and could,
perhaps, reemerge at any moment.""")
audio = gTTS(text=mytext2, lang="en", slow=False)
audio.save("Shark_Extract_Sum.mp3")
