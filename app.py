import streamlit as st
import pandas as pd
from analyzer import analyze_text

st.set_page_config(
    page_title="Hinglish Text Analyzer",
    page_icon="🇮🇳",
    layout="wide"
)

st.title("🇮🇳 Hinglish Text Analyzer")
st.caption("Analyze Hindi-English code-mixed text written in Roman script.")

st.markdown(
    """
    **What it does:** detects Hindi/English words, identifies code-mixing,
    tokenizes the sentence, and assigns basic Part-of-Speech (POS) tags.
    """
)

examples = [
    "Mujhe kal college jaana hai bro",
    "Yaar ye movie bahut acchi thi",
    "I have exam kal so I am studying",
    "Mera laptop slow hai but theek ho jayega",
]

with st.sidebar:
    st.header("Try an example")
    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state["text"] = example

text = st.text_area(
    "Enter Hinglish text",
    value=st.session_state.get("text", examples[0]),
    height=120,
    placeholder="Example: Mujhe kal college jaana hai bro"
)

if st.button("🔍 Analyze Text", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        result = analyze_text(text)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Words", result["total_words"])
        c2.metric("Hindi", result["hindi_count"])
        c3.metric("English", result["english_count"])
        c4.metric("Other", result["other_count"])

        st.subheader("📊 Language Analysis")
        st.write(f"**Sentence type:** {result['sentence_type']}")
        st.progress(result["hindi_percentage"] / 100)
        st.write(
            f"Hindi/Roman Hindi: **{result['hindi_percentage']:.1f}%** | "
            f"English: **{result['english_percentage']:.1f}%**"
        )

        st.subheader("🏷️ Token & POS Analysis")
        df = pd.DataFrame(result["tokens"])
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("🧾 Summary")
        st.info(result["summary"])

st.markdown("---")

