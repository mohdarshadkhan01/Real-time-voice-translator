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
down_arrow.pack()
output_lang_label = tk.Label(win, text="Select Output Language:")
output_lang_label.pack()
output_lang = ttk.Combobox(win, values=language_names)
