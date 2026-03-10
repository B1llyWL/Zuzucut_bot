<h1 align="center">Zuzucut Bot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Aiogram-2.25-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Aiogram">
  <img src="https://img.shields.io/badge/Telegram%20Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot">
</p>

<p align="center">
  🎨 <b>Zuzucut Bot</b> — Telegram bot for collecting art commissions. <br>
  It guides clients through a step‑by‑step form and sends the completed request to the artist.
</p>

<p align="center">
  <!-- YouTube Video Button -->
  <a href="https://youtu.be/kAAAGlONyoQ" target="_blank">
    <img src="https://img.shields.io/badge/Watch%20on-YouTube-red?style=for-the-badge&logo=youtube" alt="YouTube Video">
  </a>
  <!-- Telegram Bot Link -->
  <a href="https://t.me/Zuzucutbot" target="_blank">
    <img src="https://img.shields.io/badge/Open%20in-Telegram-26A5E4?style=for-the-badge&logo=telegram" alt="Open in Telegram">
  </a>
</p>

---

<h2 align="center">📸 Screenshot</h2>

<div align="center">
  <img src="https://github.com/user-attachments/assets/c60c2ef9-c6ce-47f2-97dd-ea5773c1f4c6" 
       alt="Bot interface screenshot" 
       width="651" 
       style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

<h2 align="center">📖 About the Bot</h2>

<p align="center">
  Zuzucut Bot simplifies the process of ordering custom artwork. <br>
  Clients answer a structured questionnaire, and the bot forwards the complete request to the artist.
</p>

<h3 align="center">📋 What the bot collects</h3>

<table align="center" style="width:80%; border-collapse:collapse;">
  <tr>
    <th style="background:#f2f2f2; padding:8px; border:1px solid #ddd;">Step</th>
    <th style="background:#f2f2f2; padding:8px; border:1px solid #ddd;">Information</th>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">1</td>
    <td style="padding:8px; border:1px solid #ddd;">Name</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">2</td>
    <td style="padding:8px; border:1px solid #ddd;">Username (for delivery)</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">3</td>
    <td style="padding:8px; border:1px solid #ddd;">Type of work (full art / sketch)</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">4</td>
    <td style="padding:8px; border:1px solid #ddd;">Background style (flat color, simple rendering, collage)</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">5</td>
    <td style="padding:8px; border:1px solid #ddd;">Deadline (with +30% for urgency)</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">6</td>
    <td style="padding:8px; border:1px solid #ddd;">Extra factors (second character, excessive detail, complex angle)</td>
  </tr>
  <tr>
    <td style="padding:8px; border:1px solid #ddd;">7</td>
    <td style="padding:8px; border:1px solid #ddd;">Additional comments</td>
  </tr>
</table>

<h2 align="center">🤖 Bot Commands & Features</h2>

<ul style="display:inline-block; text-align:left;">
  <li><code>/start</code> – welcome message and main menu</li>
  <li><code>/help</code> – get assistance</li>
  <li><code>/contact</code> – contact the developer and artist</li>
  <li><code>/register</code> – start a new art commission request</li>
  <li><b>Interactive buttons:</b>
    <ul>
      <li>❓ How to order an art</li>
      <li>💰 Payment info (Sberbank, RUB only)</li>
      <li>💵 Price list (detailed pricing)</li>
      <li>🖼️ Examples of works (link to portfolio)</li>
      <li>⏳ Typical deadlines</li>
      <li>⭐ Client reviews</li>
    </ul>
  </li>
</ul>

<h2 align="center">🚀 How to Use</h2>

<p align="center">
  1. Open Telegram and search for <code>@Zuzucutbot</code>.<br>
  2. Start the bot with <code>/start</code>.<br>
  3. Use the menu buttons or <code>/register</code> to place an order.<br>
  4. Follow the step‑by‑step questionnaire – your request will be sent directly to the artist.
</p>

<h2 align="center">⚙️ Installation (for developers)</h2>

<p align="center">
  <i>Want to run your own instance?</i>
</p>

<pre style="background:#f6f8fa; padding:15px; border-radius:8px; max-width:800px; margin:0 auto;"><code># 1. Clone the repository
git clone https://github.com/yourusername/zuzucut-bot.git
cd zuzucut-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file with your bot token
echo "BOT_TOKEN=your_telegram_bot_token" > .env

# 4. Run the bot
python bot.py</code></pre>

<p align="center">
  <i>Make sure you have Python 3.8+ and a Telegram bot token from <a href="https://t.me/BotFather">@BotFather</a>.</i>
</p>

<hr>
<p align="center">
  A Python‑powered bot created for the Zuzucut art community. <br>
  Developed with ❤️ using <a href="https://docs.aiogram.dev/">Aiogram</a>.
</p>
