import gtts
from playsound import playsound
from gtts import gTTS
import os
my_text=" माझे नाव विशाल आहे"
language="en"
output= gTTS(text=my_text,lang=language,slow=False)
output.save('t.mp3')
playsound('t.mp3')