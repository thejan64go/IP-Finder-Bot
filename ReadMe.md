

# 🌐 IP Finder Bot for Telegram

## 📜 Introduction
IP Finder Bot is a Telegram bot 🤖 that provides detailed information about IP addresses 🌍, including geographical location 📍, Internet Service Provider (ISP), and more. It supports both IPv4 and IPv6 addresses and offers functionalities through direct messages 💬 and inline queries 🔍.

## 🖼 Sample Image
![IP Finder Bot Sample](https://te.legra.ph/file/f3810a14eea0913203e5d.png)

## ✨ Features
- **IP Address Lookup**: Enter an IP address to get detailed information 🔎.
- **IPv4 and IPv6 Support**: Handles both IPv4 and IPv6 address formats 🔄.
- **Geographical Information**: Provides details like country 🏳️, city 🏙, region, and postal code 📬.
- **ISP Information**: Retrieves the Internet Service Provider associated with the IP 🌐.
- **Interactive Map**: Shares a static map pinpointing the IP address location 🗺, generated using the [LocationIQ Maps API](https://docs.locationiq.com/docs/maps).
- **Inline Query Support**: Use the bot in any conversation through inline queries 🔍.
- **Privacy Focused**: Does not store user queries 🛡.

## 🗺 Utilizing LocationIQ Maps API for Map Images
The bot generates map images for IP locations using the LocationIQ Maps API:

### 🚀 Getting Started with LocationIQ Maps API
1. Obtain an API key by signing up for a free LocationIQ account 🔑.
2. Use the Static Map service by constructing a URL with the location's latitude and longitude, and your API key 📍.

### 📌 Example API Request
```
https://maps.locationiq.com/v3/staticmap?key=YOUR_LOCATIONIQ_API_KEY&center=LATITUDE,LONGITUDE&zoom=16&size=600x600&markers=icon:large-blue-cutout|LATITUDE,LONGITUDE
```
*Replace `YOUR_LOCATIONIQ_API_KEY`, `LATITUDE`, and `LONGITUDE` with your LocationIQ API key and the geographical coordinates.*

## ⚙️ Installation

### 📋 Prerequisites
- Python 3.6+ 🐍
- Telegram Bot Token 🤖
- IPinfo API token 🔑

### 📦 Required Libraries
```
pyrogram ipinfo requests
```

### 🔧 Installation Steps
1. Clone/download the script.
2. Install required Python libraries: `pip install pyrogram ipinfo requests`.
3. Create a `config.py` with your API ID, API HASH, Bot Token, and IPinfo Access Token.
4. Run the bot: `python your_script_name.py`.

## 📖 Usage
- **Start the Bot**: Send `/start` to see the welcome message 🚀.
- **Find IP Information**: Send any IP address 📧.
- **Inline Query**: Type `@YourBotUsername IP_ADDRESS` in any chat 🔍.

## 🌟 Original Bot
Access the original bot [here](https://t.me/IPfinderobo_bot).

---

