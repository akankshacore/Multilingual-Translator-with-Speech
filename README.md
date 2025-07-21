# Multilingual Translator with Speech

A simple Python-based multilingual translator with speech output using Google Translate and gTTS.

## 📝 Features

- Translate text between 100+ languages  
- Auto-detect source and target languages by name or code  
- Convert translated text to speech using Google Text-to-Speech (gTTS)  
- Play audio using Pygame  
- Command-line based and easy to use  

## 🛠️ Technologies Used

- `googletrans` (4.0.0-rc1)  
- `gTTS`  
- `pygame`  
- Python 3  

## 💡 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multilingual-translator-with-speech.git
cd multilingual-translator-with-speech
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python translator.py
```

### 4. Follow the prompts

* Enter the language you're translating **from** (e.g., `english` or `en`)
* Enter the phrase to translate
* Enter the language you're translating **to** (e.g., `french` or `fr`)

## 📦 Requirements

Install all dependencies with:

```bash
pip install googletrans==4.0.0-rc1 gTTS pygame
```

Or use the `requirements.txt` file.

## 📁 Files Included

* `translator.py` — Main Python script
* `README.md` — Project documentation
* `requirements.txt` — Dependency list
* `.gitignore` — Ignore audio files and `__pycache__`

## 📸 Preview

```bash
Enter the language you want to translate from: english
Enter the word or phrase to translate: how are you
Enter the language you want to translate to: french
Translation: Comment allez-vous
```

*(Audio plays: "Comment allez-vous")*

## 🧠 Future Enhancements

* Add GUI using Tkinter or PyQt
* Auto-suggest supported languages
* Store translation history

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📃 License

This project is open source and free to use under the [MIT License](LICENSE).
