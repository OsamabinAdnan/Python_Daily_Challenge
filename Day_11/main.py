import streamlit as st
import re

# Set Streamlit page configuration
st.set_page_config(page_title="Emoji Sentiment Analyzer", page_icon="😊", layout="centered")

# Custom CSS for Neon Theme
st.markdown(
    """
    <style>
    body {
        background-color: #0f0f0f;
        color: #39ff14;
        text-align: center;
    }
    .stTextInput, .stButton>button {
        border: 2px solid #39ff14;
        background-color: #1f1f1f;
        color: #39ff14;
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #39ff14;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the App
st.markdown("<h1 style='text-align: center; color: #39ff14;'>🚀 Emoji Sentiment Analyzer 🤖</h1>", unsafe_allow_html=True)

# Input from the user
user_input = st.text_input("Enter your message:", placeholder="Type a message with emojis...")

# Emoji mood dictionary
emoji_mood_map = {
    # 😃 Happy / Joyful Mood
    "😊": "Happy Mood!", "😃": "Happy Mood!", "😁": "Happy Mood!", "😄": "Happy Mood!", 
    "😆": "Happy Mood!", "😇": "Happy Mood!", "😎": "Happy Mood!", "🥳": "Happy Mood!",
    "😍": "Happy Mood!", "🥰": "Happy Mood!", "😻": "Happy Mood!", "🎉": "Excited Mood!",

    # 😢 Sad / Upset Mood
    "😢": "Sad Mood!", "😭": "Sad Mood!", "☹": "Sad Mood!", "😞": "Sad Mood!", 
    "😔": "Sad Mood!", "😿": "Sad Mood!", "🥺": "Sad Mood!", "😖": "Distressed Mood!", 
    "😕": "Confused Mood!", "🙁": "Upset Mood!", "😫": "Tired Mood!",

    # 😡 Angry / Frustrated Mood
    "😡": "Angry Mood!", "🤬": "Angry Mood!", "😠": "Angry Mood!", "👿": "Angry Mood!",
    "💢": "Annoyed Mood!", "😤": "Frustrated Mood!", "😾": "Annoyed Mood!",

    # 😐 Neutral / Confused / Thinking Mood
    "😐": "Neutral Mood!", "😶": "Neutral Mood!", "🤔": "Thinking Mood!", "🤨": "Skeptical Mood!",
    "😑": "Bored Mood!", "🙄": "Sarcastic Mood!", "🧐": "Curious Mood!",

    # 😂 Funny / Laughing Mood
    "😂": "Laughing Mood!", "🤣": "Laughing Mood!", "😹": "Funny Mood!", "😜": "Playful Mood!",
    "🤪": "Silly Mood!", "😝": "Cheeky Mood!",

    # 😱 Shocked / Surprised / Fearful Mood
    "😱": "Shocked Mood!", "😨": "Anxious Mood!", "😰": "Nervous Mood!", "😧": "Distressed Mood!",
    "😦": "Worried Mood!", "😵": "Dizzy Mood!", "🤯": "Mind-Blown Mood!",

    # 🤢 Disgusted / Sick Mood
    "🤢": "Disgusted Mood!", "🤮": "Vomiting Mood!", "🤧": "Sick Mood!", "😷": "Unwell Mood!",
    "🤕": "Injured Mood!", "🥴": "Dizzy Mood!",

    # ❤️ Love / Affectionate Mood
    "❤️": "Loving Mood!", "💖": "Romantic Mood!", "💕": "Affectionate Mood!", "💞": "Caring Mood!",
    "💗": "Loving Mood!", "💓": "Heartfelt Mood!", "💘": "Crushing Mood!", "💝": "Affectionate Mood!",

    # 😴 Sleepy / Tired Mood
    "😴": "Sleepy Mood!", "🥱": "Yawning Mood!", "💤": "Tired Mood!",

    # 😇 Grateful / Blessed Mood
    "🙏": "Grateful Mood!", "💫": "Blessed Mood!", "✨": "Hopeful Mood!", "🌟": "Inspired Mood!",

    # 🤗 Friendly / Hugging Mood
    "🤗": "Hugging Mood!", "😊": "Friendly Mood!",

    # 🎭 Mixed / Drama Mood
    "🎭": "Dramatic Mood!", "🤹‍♂️": "Juggling Mood!", "🃏": "Joker Mood!"
}

# Define Unicode ranges using chr()
emoji_pattern = re.compile(
    f"[{chr(0x1F600)}-{chr(0x1F64F)}"  # Emoticons
    f"{chr(0x1F300)}-{chr(0x1F5FF)}"  # Miscellaneous Symbols & Pictographs
    f"{chr(0x1F680)}-{chr(0x1F6FF)}"  # Transport & Map
    f"{chr(0x1F700)}-{chr(0x1F77F)}"  # Alchemical Symbols
    f"{chr(0x1F780)}-{chr(0x1F7FF)}"  # Geometric Shapes Extended
    f"{chr(0x1F800)}-{chr(0x1F8FF)}"  # Supplemental Arrows-C
    f"{chr(0x1F900)}-{chr(0x1F9FF)}"  # Supplemental Symbols & Pictographs
    f"{chr(0x2600)}-{chr(0x26FF)}"  # Miscellaneous Symbols
    f"{chr(0x2700)}-{chr(0x27BF)}"  # Dingbats
    f"{chr(0xFE00)}-{chr(0xFE0F)}"  # Variation Selectors
    f"{chr(0x1FA70)}-{chr(0x1FAFF)}"  # Symbols & Pictographs Extended
    "]+", flags=re.UNICODE
)

# Process user input
if st.button("Analyze Mood"):
    if user_input:
        emojis_found = emoji_pattern.findall(user_input)
        
        if emojis_found:
            for emoji in emojis_found:
                if emoji in emoji_mood_map:
                    detected_mood = emoji_mood_map[emoji]
                    break
            else:
                detected_mood = "Emoji found, but mood not recognized!"
        else:
            detected_mood = "No emoji found, can't detect mood!"
        
        # Display Result with Styling
        st.markdown(f"<h2 style='color: #39ff14;'>Detected Mood: {detected_mood} 🎭</h2>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a message first!")
