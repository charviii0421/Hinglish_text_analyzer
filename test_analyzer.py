from analyzer import analyze_text

examples = [
    "Mujhe kal college jaana hai bro",
    "Yaar ye movie bahut acchi thi",
    "I have exam kal",
]

for text in examples:
    result = analyze_text(text)
    print("\nINPUT:", text)
    print("TYPE:", result["sentence_type"])
    for row in result["tokens"]:
        print(row)
