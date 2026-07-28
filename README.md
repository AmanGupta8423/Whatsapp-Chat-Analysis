# WhatsApp Chat Analyzer

An interactive Streamlit web app that analyzes exported WhatsApp chat logs and generates statistics and visualizations. Upload any WhatsApp chat export (`.txt`) and explore message activity, participation trends, word usage, and emoji patterns — works with any chat, not just a specific one.

Live app: https://whatsapp-chat-analysis-3lru.onrender.com/

Repository: https://github.com/AmanGupta8423/Whatsapp-Chat-Analysis

---

## How to Use

1. Open any WhatsApp chat (individual or group) on your phone
2. Tap the three-dot menu, then go to More > Export Chat
3. Choose "Without Media" (recommended, faster upload and analysis)
4. Save or share the exported `.txt` file to your device/email so you can access it on your computer
5. Open the live app link above
6. Upload the `.txt` file using the file uploader in the sidebar
7. Select a specific participant or "All" to view chat-wide stats
8. Click Analyse to generate the statistics and visualizations

Note: The chat data is processed only to generate your statistics and visualizations within the app session — it is not stored or shared anywhere.

---

## Features

- Upload any exported WhatsApp chat file and filter analysis by individual participant or the whole group
- Message table view with sender, message, and timestamp
- Extraction of all links shared in the chat
- Participation timelines: monthly, daily, and weekly message activity
- Hourly activity heatmap (day vs. time-of-day)
- Top statistics: total messages, total words, media shared, links shared
- Most active members ranking (for group chats)
- Word cloud of frequently used words
- Most common words list, with Hinglish stopword filtering for mixed Hindi-English chats
- Emoji usage tracker

---

## Tech Stack

- Python
- Streamlit (web app framework)
- Pandas (data processing)
- Matplotlib and Seaborn (visualizations)
- Deployed on Render

---

## How It Works

1. User uploads a WhatsApp chat export (generated via WhatsApp's "Export Chat" feature)
2. `preprocessor.py` parses the raw text into a structured DataFrame (user, message, date/time)
3. `helper.py` computes the statistics and builds the data for each visualization (timelines, heatmap, word cloud, emoji tracking, etc.)
4. `app.py` renders everything as an interactive Streamlit dashboard

---

## Running Locally

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. Upload a WhatsApp chat export file from the sidebar and click Analyse

---

## Project Structure

```
Whatsapp-Chat-Analysis/
├── app.py                # Streamlit app - UI and layout
├── preprocessor.py       # Parses raw chat export into a structured DataFrame
├── helper.py              # Analytics functions (stats, timelines, heatmap, word cloud, emoji tracking)
├── stop_hinglish.txt      # Stopword list for Hinglish text filtering
├── requirements.txt       # Python dependencies
└── README.md
```

---

## License

Feel free to use or extend this project with attribution.

## About Me

Hi, I'm Aman Gupta — a Data Science Enthusiast and student at NIT Jamshedpur. I built this project to work hands-on with data preprocessing, exploratory analysis, and building interactive dashboards.

Connect with me:
LinkedIn: https://www.linkedin.com/in/aman-gupta-bb196621b/
GitHub: https://github.com/AmanGupta8423
Email: 2024ugpi049@nitjsr.ac.in
