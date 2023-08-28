import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def text_to_speech(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)

if __name__ == "__main__":
    pdf_path = "BRANCHING.pdf"  # Replace with your PDF file path
    output_path = "audio.mp3"  # Replace with desired output file path

    pdf_text = pdf_to_text(pdf_path)
    text_to_speech(pdf_text, output_path)

    os.system("start " + output_path)  # This line opens the generated audio file (on Windows)
