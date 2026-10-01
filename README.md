# 🇮🇳 Hinglish Text Analyzer

A lightweight NLP project that analyzes **Hindi-English code-mixed (Hinglish) text** written in Roman script, such as WhatsApp-style messages.

## 🎯 Objective

The system:
- Tokenizes Hinglish text into individual words.
- Identifies Hindi/Roman-Hindi and English words.
- Detects whether a sentence is code-mixed.
- Assigns basic Part-of-Speech (POS) tags such as NOUN, VERB, PRON, ADJ and ADV.
- Displays the analysis through an interactive Streamlit web app.

## 🧠 Methodology

```text
User Input
   ↓
Tokenization
   ↓
Language Identification
   ↓
Hinglish / Code-Mix Detection
   ↓
Rule + Lexicon Based POS Tagging
   ↓
Analysis Table + Summary
```

### Why Hinglish is challenging

Hinglish is commonly written in Roman script, and the same Hindi word may have several spellings:

- acha / accha / achha
- nahi / nahin / nhi
- kya / kyaa

Therefore, a small curated lexicon plus rule-based processing is used in this educational prototype.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Regular Expressions
- Rule-based NLP / lexical analysis

## 📁 Project Structure

```text
Hinglish_text_analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── sample_hinglish.csv
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/charviii0421/Hinglish_text_analyzer.git
cd Hinglish_text_analyzer
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The browser will open with the Hinglish Text Analyzer.

## 🧪 Example

Input:

```text
Mujhe kal college jaana hai bro
```

The application identifies the sentence as **Hinglish / Code-Mixed** and produces token-level language and POS information.

## ⚠️ Limitations

This is an educational prototype. Roman Hindi has no single standardized spelling, so a lexicon/rule-based system cannot correctly classify every possible Hinglish word. A larger annotated Hinglish corpus and a trained sequence model could improve coverage.

## 🚀 Future Scope

- Add a larger annotated Hinglish dataset.
- Train an ML sequence-tagging model.
- Add transliteration to Devanagari Hindi.
- Add slang and spelling normalization.
- Add sentiment and intent analysis.
- Compare rule-based POS tagging with CRF/HMM/transformer approaches.

## 👩‍💻 Project

**Hinglish Text Analyzer — NLP Project**
