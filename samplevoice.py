
# coding: utf-8

# In[ ]:


from gtts import gTTS
from tempfile import TemporaryFile

while True:
 t=raw_input("enter-")
 tts=gTTS(text=t,lang='en')
 f = TemporaryFile()   
 tts.write_to_fp(f)
 f.close()   
    

