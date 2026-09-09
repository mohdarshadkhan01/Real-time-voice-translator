import os
import threading
import tkinter as tk
from gtts import gTTS
from tkinter import ttk
import speech_recognition as sr
from playsound import playsound
from deep_translator import GoogleTranslator
from google.transliteration import transliterate_text
win= tk.Tk()
win.geometry("700x450")
win.title("Real-Time Voice🎙️ Translator🔊")
icon = tk.PhotoImage(file="icon.png")
win.iconphoto(False, icon)
input_label = tk.Label(win, text="Recognized Text ⮯")
input_label.pack()
input_text = tk.Text(win, height=5, width=50)
input_text.pack()
output_label = tk.Label(win, text="Translated Text ⮯")
output_label.pack()
output_text = tk.Text(win, height=5, width=50)
output_text.pack()
blank_space = tk.Label(win, text="")
blank_space.pack()
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa"
}
language_names = list(language_codes.keys())
input_lang_label = tk.Label(win, text="Select Input Language:")
input_lang_label.pack()
input_lang = ttk.Combobox(win, values=language_names)
def update_input_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    input_lang.set(selected_language_code)
input_lang.bind("<<ComboboxSelected>>", lambda e: update_input_lang_code(e))
if input_lang.get() == "": input_lang.set("auto")
input_lang.pack()
output_lang = ttk.Combobox(win, values=language_names)
down_arrow.pack()
output_lang_label = tk.Label(win, text="Select Output Language:")
output_lang_label.pack()
output_lang = ttk.Combobox(win, values=language_names)
def update_output_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    output_lang.set(selected_language_code)
output_lang.bind("<<ComboboxSelected>>", lambda e: update_output_lang_code(e))
if output_lang.get() == "": output_lang.set("en")
output_lang.pack()
blank_space = tk.Label(win, text="")
blank_space.pack()
keep_running = False
def update_translation():
    global keep_running
    if keep_running:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Now!\n")
            audio = r.listen(source)
            try:
                speech_text = r.recognize_google(audio)
                speech_text_transliteration = transliterate_text(speech_text, lang_code=input_lang.get()) if input_lang.get() not in ('auto', 'en') else speech_text
                input_text.insert(tk.END, f"{speech_text_transliteration}\n")
                if speech_text.lower() in {'exit', 'stop'}:
                    keep_running = False
                    return
                translated_text = GoogleTranslator(source=input_lang.get(), target=output_lang.get()).translate(text=speech_text_transliteration)
                voice = gTTS(translated_text, lang=output_lang.get())
                voice.save('voice.mp3')
                playsound('voice.mp3')
                os.remove('voice.mp3')
                output_text.insert(tk.END, translated_text + "\n")
            except sr.UnknownValueError:
                output_text.insert(tk.END, "Could not understand!\n")
            except sr.RequestError:
                output_text.insert(tk.END, "Could not request from Google!\n")
    win.after(100, update_translation)
