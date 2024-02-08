IP Finder Bot for Telegram
Introduction
IP Finder Bot is a Telegram bot designed to help users find detailed information about an IP address, including the geographical location, Internet Service Provider (ISP), and more. It supports both IPv4 and IPv6 addresses and provides functionalities through both direct messaging and inline queries.

Features
IP Address Lookup: Enter an IP address to get detailed information.
Support for IPv4 and IPv6: Can handle both IPv4 and IPv6 address formats.
Geographical Information: Provides country, city, region, and even postal code.
ISP Information: Retrieves the Internet Service Provider associated with the IP.
Interactive Map: Shares a static map pinpointing the IP address location.
Inline Query Support: Use the bot in any conversation through inline queries.
Privacy Focused: Does not store user queries for privacy.
Installation
To use this bot, you need to have Python installed on your machine along with some specific libraries. Follow the steps below to set up and run the bot:

Prerequisites
Python 3.6 or newer
A Telegram Bot Token (obtained from BotFather)
An IPinfo API token (obtain from IPinfo)
Required Libraries
pyrogram - A modern, elegant, and asynchronous Telegram MTProto API framework.
ipinfo - For fetching IP details.
requests - For making HTTP requests.
Installation Steps
Clone this repository or download the script.
Install the required Python libraries using pip:
Copy code
pip install pyrogram ipinfo requests
Create a config.py file in the same directory as the script with the following content, replacing YOUR_API_ID, YOUR_API_HASH, YOUR_BOT_TOKEN, and YOUR_IPINFO_ACCESS_TOKEN with your actual details:
python
Copy code
class con:
    API_ID = 'YOUR_API_ID'  # Your API ID (as a string)
    API_HASH = 'YOUR_API_HASH'  # Your API Hash (as a string)
    BOT_TOKEN = 'YOUR_BOT_TOKEN'  # Your Bot Token (as a string)
    IP_API = 'YOUR_IPINFO_ACCESS_TOKEN'  # Your IPinfo Access Token (as a string)
Run the bot:
Copy code
python your_script_name.py
Usage
Start the Bot: Send /start to the bot to see the welcome message and instructions.
Find IP Information: Simply send any IP address to the bot, and it will return the information.
Inline Query: In any chat, type @YourBotUsername IP_ADDRESS to share IP information directly in the cha