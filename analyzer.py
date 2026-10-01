import re

# Small curated lexicons for a fast, offline classroom demo.
# Roman Hindi has many spelling variations, so common variants are included.

HINDI_WORDS = {
    "main", "mai", "mein", "mujhe", "mujh", "mera", "meri", "mere",
    "hum", "ham", "hume", "humein", "aap", "aapko", "tum", "tumhe",
    "tu", "tera", "teri", "tere", "ye", "yeh", "woh", "vo", "us",
    "uska", "uski", "iske", "iska", "ki", "ka", "ke", "ko", "se",
    "par", "pe", "me", "mein", "aur", "ya", "lekin", "magar", "kyunki",
    "kyun", "kya", "kaise", "kab", "kahan", "nahi", "nahin", "nhi",
    "haan", "han", "hai", "hain", "tha", "thi", "the", "hoga", "hogi",
    "ho", "hu", "hun", "raha", "rahi", "rahe", "gaya", "gayi", "gaye",
    "jaana", "jana", "ja", "aana", "ana", "aaya", "aayi", "aaye",
    "kar", "karo", "karta", "karti", "karte", "kiya", "kiye", "kya",
    "dena", "diya", "liye", "liya", "lena", "le", "chal", "chalo",
    "bol", "bola", "suno", "sun", "dekh", "dekho", "samajh",
    "samaj", "pata", "lagta", "lagti", "acha", "accha", "achha",
    "acchi", "achhi", "bura", "bur", "bahut", "bohot", "thoda",
    "zyada", "kam", "abhi", "kal", "aaj", "parso", "subah", "raat",
    "din", "raat", "ghar", "college", "dost", "yaar", "bhai", "behen",
    "ladka", "ladki", "baccha", "bachha", "log", "sab", "kuch",
    "koi", "kaun", "kyon", "kyu", "phir", "fir", "bhi", "toh", "to",
    "sirf", "mujhse", "aapse", "tumse", "apna", "apni", "apne",
    "hamara", "hamari", "hamare", "mera", "meri", "mere"
}

ENGLISH_WORDS = {
    "i", "you", "he", "she", "we", "they", "it", "me", "my", "your",
    "his", "her", "our", "their", "this", "that", "these", "those",
    "a", "an", "the", "and", "or", "but", "because", "if", "then",
    "is", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would",
    "can", "could", "should", "must", "may", "might",
    "go", "going", "went", "come", "coming", "came", "make", "made",
    "study", "studying", "read", "reading", "write", "writing",
    "work", "working", "play", "playing", "watch", "watching",
    "eat", "eating", "drink", "drinking", "like", "love", "need",
    "want", "know", "think", "see", "look", "give", "take",
    "college", "school", "class", "teacher", "student", "friend",
    "bro", "dude", "movie", "film", "phone", "laptop", "exam",
    "assignment", "project", "today", "tomorrow", "yesterday",
    "good", "great", "bad", "nice", "very", "really", "not",
    "late", "slow", "fast", "online", "offline", "okay", "ok",
    "thanks", "thank", "please", "sorry", "yes", "no", "hello",
    "bye", "time", "day", "night", "morning", "money", "home"
}

POS_LEXICON = {
    # Hindi/Roman Hindi
    "main": "PRON", "mai": "PRON", "mujhe": "PRON", "mera": "PRON",
    "meri": "PRON", "mere": "PRON", "hum": "PRON", "ham": "PRON",
    "aap": "PRON", "aapko": "PRON", "tum": "PRON", "tumhe": "PRON",
    "tu": "PRON", "tera": "PRON", "teri": "PRON", "ye": "PRON",
    "yeh": "PRON", "woh": "PRON", "vo": "PRON", "us": "PRON",
    "kya": "PRON", "kaun": "PRON", "koi": "PRON", "kuch": "PRON",
    "hai": "AUX", "hain": "AUX", "tha": "AUX", "thi": "AUX",
    "the": "AUX", "hoga": "AUX", "hogi": "AUX", "ho": "AUX",
    "hun": "AUX", "hu": "AUX",
    "jaana": "VERB", "jana": "VERB", "ja": "VERB", "aana": "VERB",
    "ana": "VERB", "aaya": "VERB", "aayi": "VERB", "kar": "VERB",
    "karo": "VERB", "karta": "VERB", "karti": "VERB", "karte": "VERB",
    "kiya": "VERB", "kiye": "VERB", "dena": "VERB", "diya": "VERB",
    "lena": "VERB", "le": "VERB", "liya": "VERB", "gaya": "VERB",
    "gayi": "VERB", "gaye": "VERB", "raha": "VERB", "rahi": "VERB",
    "rahe": "VERB", "bol": "VERB", "bola": "VERB", "suno": "VERB",
    "sun": "VERB", "dekh": "VERB", "dekho": "VERB", "samajh": "VERB",
    "pata": "VERB", "lagta": "VERB", "lagti": "VERB",
    "acha": "ADJ", "accha": "ADJ", "achha": "ADJ", "acchi": "ADJ",
    "achhi": "ADJ", "bura": "ADJ", "bahut": "ADV", "bohot": "ADV",
    "thoda": "ADV", "zyada": "ADV", "kam": "ADV", "abhi": "ADV",
    "kal": "ADV", "aaj": "ADV", "parso": "ADV", "phir": "ADV",
    "fir": "ADV", "bhi": "ADV", "toh": "PART", "to": "PART",
    "aur": "CONJ", "ya": "CONJ", "lekin": "CONJ", "magar": "CONJ",
    "kyunki": "CONJ", "ki": "SCONJ", "ka": "ADP", "ke": "ADP",
    "ko": "ADP", "se": "ADP", "par": "ADP", "pe": "ADP",
    "bhai": "NOUN", "yaar": "NOUN", "dost": "NOUN", "ghar": "NOUN",
    "college": "NOUN", "ladka": "NOUN", "ladki": "NOUN", "log": "NOUN",

    # English
    "i": "PRON", "you": "PRON", "he": "PRON", "she": "PRON", "we": "PRON",
    "they": "PRON", "it": "PRON", "me": "PRON", "my": "PRON", "your": "PRON",
    "his": "PRON", "her": "PRON", "our": "PRON", "their": "PRON",
    "this": "DET", "that": "DET", "these": "DET", "those": "DET",
    "a": "DET", "an": "DET", "the": "DET",
    "and": "CONJ", "or": "CONJ", "but": "CONJ", "because": "SCONJ",
    "if": "SCONJ", "is": "AUX", "am": "AUX", "are": "AUX", "was": "AUX",
    "were": "AUX", "be": "AUX", "been": "AUX", "being": "AUX",
    "have": "VERB", "has": "VERB", "had": "VERB", "do": "VERB",
    "does": "VERB", "did": "VERB", "go": "VERB", "going": "VERB",
    "went": "VERB", "come": "VERB", "coming": "VERB", "came": "VERB",
    "make": "VERB", "made": "VERB", "study": "VERB", "studying": "VERB",
    "read": "VERB", "reading": "VERB", "write": "VERB", "writing": "VERB",
    "work": "VERB", "working": "VERB", "play": "VERB", "playing": "VERB",
    "watch": "VERB", "watching": "VERB", "eat": "VERB", "eating": "VERB",
    "drink": "VERB", "drinking": "VERB", "like": "VERB", "love": "VERB",
    "need": "VERB", "want": "VERB", "know": "VERB", "think": "VERB",
    "see": "VERB", "look": "VERB", "give": "VERB", "take": "VERB",
    "good": "ADJ", "great": "ADJ", "bad": "ADJ", "nice": "ADJ",
    "late": "ADJ", "slow": "ADJ", "fast": "ADJ", "very": "ADV",
    "really": "ADV", "not": "PART", "today": "ADV", "tomorrow": "ADV",
    "yesterday": "ADV", "college": "NOUN", "school": "NOUN", "class": "NOUN",
    "teacher": "NOUN", "student": "NOUN", "friend": "NOUN", "bro": "NOUN",
    "dude": "NOUN", "movie": "NOUN", "film": "NOUN", "phone": "NOUN",
    "laptop": "NOUN", "exam": "NOUN", "assignment": "NOUN", "project": "NOUN",
    "time": "NOUN", "day": "NOUN", "night": "NOUN", "morning": "NOUN",
    "money": "NOUN", "home": "NOUN", "online": "ADJ", "offline": "ADJ",
    "okay": "ADJ", "ok": "INTJ", "thanks": "INTJ", "thank": "INTJ",
    "please": "INTJ", "sorry": "INTJ", "yes": "INTJ", "no": "INTJ",
    "hello": "INTJ", "bye": "INTJ"
}

def tokenize(text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?|[^\w\s]", text)

def classify_language(word):
    w = word.lower()
    if w in HINDI_WORDS and w in ENGLISH_WORDS:
        # Words shared by both sets are generally treated as English/common.
        return "English/Common"
    if w in HINDI_WORDS:
        return "Hindi"
    if w in ENGLISH_WORDS:
        return "English"
    if re.fullmatch(r"\d+(?:\.\d+)?", w):
        return "Number"
    if re.fullmatch(r"[^\w\s]", w):
        return "Punctuation"
    return "Unknown"

def guess_pos(word, language):
    w = word.lower()
    if w in POS_LEXICON:
        return POS_LEXICON[w]

    if re.fullmatch(r"\d+(?:\.\d+)?", w):
        return "NUM"
    if re.fullmatch(r"[^\w\s]", w):
        return "PUNCT"

    # Useful suffix rules for unseen Roman-Hindi words.
    if language == "Hindi":
        if w.endswith(("na", "ne", "ni", "ta", "ti", "te", "kar", "gaya", "gayi")):
            return "VERB"
        if w.endswith(("wala", "wali", "wale")):
            return "NOUN"

    # Basic English morphology.
    if w.endswith(("ing", "ed")):
        return "VERB"
    if w.endswith(("ly",)):
        return "ADV"
    if w.endswith(("ous", "ful", "able", "ive", "al")):
        return "ADJ"

    return "NOUN" if language in ("Hindi", "English", "English/Common") else "X"

def analyze_text(text):
    raw_tokens = tokenize(text)
    tokens = []

    for word in raw_tokens:
        language = classify_language(word)
        pos = guess_pos(word, language)
        tokens.append({
            "Token": word,
            "Language": language,
            "POS Tag": pos
        })

    word_rows = [r for r in tokens if r["Language"] not in ("Punctuation",)]
    total = len(word_rows)

    hindi = sum(r["Language"] == "Hindi" for r in word_rows)
    english = sum(r["Language"] in ("English", "English/Common") for r in word_rows)
    other = total - hindi - english

    if hindi > 0 and english > 0:
        sentence_type = "Hinglish / Code-Mixed"
    elif hindi > 0:
        sentence_type = "Mostly Hindi"
    elif english > 0:
        sentence_type = "Mostly English"
    else:
        sentence_type = "Unknown / Other"

    hp = (hindi / total * 100) if total else 0
    ep = (english / total * 100) if total else 0

    summary = (
        f"The text contains {hindi} Hindi word(s) and {english} English word(s). "
        f"It is classified as **{sentence_type}**. "
        f"The analyzer uses tokenization, a Hinglish lexicon, and rule-based POS tagging."
    )

    return {
        "tokens": tokens,
        "total_words": total,
        "hindi_count": hindi,
        "english_count": english,
        "other_count": other,
        "hindi_percentage": hp,
        "english_percentage": ep,
        "sentence_type": sentence_type,
        "summary": summary
    }
