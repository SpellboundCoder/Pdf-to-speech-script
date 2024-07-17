from pdfquery import PDFQuery
from gtts import gTTS
from playsound import playsound
import os
import tempfile

# path to pdf file
pdf = PDFQuery('assets/pdf_files/CV lead magnet.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]
text_to_audio = "".join(text)

print(text_to_audio)


def do_tts(text_):
    tts = gTTS(text_)
    temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
    tts.save(temp_file.name)
    file_url = "file://" + os.path.abspath(temp_file.name)
    temp_file.close()
    return file_url


file_path = do_tts(text_to_audio)
playsound(file_path)
os.remove(file_path)

