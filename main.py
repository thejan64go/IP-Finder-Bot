#නමෝ බුද්ධාය | තෙරුවන් සරණයි 

#Import All Libraries 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,InlineQuery,InlineQueryResultPhoto
import ipinfo,ipaddress
import logging
import config
import json
from pyrogram import enums
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger(__name__)
json_file = "/ip-bot/user_ids.json" #path of  saving user id's list 
try:
    with open(json_file, "r") as file:
        user_ids = json.load(file)
except FileNotFoundError:
    user_ids = []

ip_data = {}


app = Client(
    "IP_BOT",
    api_id=config.con.API_ID,  # Accessing API_ID through the instance
    api_hash=config.con.API_HASH,  # Accessing API_HASH through the instance
    bot_token=config.con.BOT_TOKEN)  # Accessing BOT_TOKEN through the instance



#◇──────────────────────────── START COMMAND ─────────────────────────────◇

@app.on_message(filters.command("start")& filters.private)
async def start_handler(client: Client, message: Message):
    user_id = message.from_user.id
    inline_keyboard1 = InlineKeyboardMarkup([[InlineKeyboardButton("IP Finder Bot", url="https://t.me/IPfinderobo_bot")]])
    await app.send_photo(chat_id=message.chat.id,photo="https://te.legra.ph/file/c2e0b27bf45dcaa104633.jpg",caption='''
👋 Hello There, 

🤖 I'm IP FINDER BOT⚡️
💫Send Any Ip Address To Me 
🥳 I'm Also IPV6 Supported 
☘️ Inline Mode
😎Check IP Risk Level
✅ 24x7 Active
🚀 Deployed On Faster VPS

😎 We all been in that moment when a device logged in to your account and you have no idea what that is or who that is. Well now you can use IP Finder bot to find 👀 Who The Hell Was That and Where The Hell Was Him at that time. All you need is that ip address only. Just give it a try🥳

🧑‍💻How To Use: Start the bot and send any IP address to it. It's so esay✌️

◇───────────────◇

👨‍💻 Developer: @Error_316 ✅

👨‍💻Powered By @Codex_SL 🇱🇰

◇───────────────◇''', reply_markup=inline_keyboard1)
   
    if user_id not in user_ids:
            user_ids.append(user_id)
            with open(json_file, "w") as file:
                json.dump(user_ids, file)



#◇──────────────────────────── STATS COMMAND ─────────────────────────────◇

@app.on_message(filters.command("stats"))
async def start_handler(client: Client, message: Message):
    x = message.from_user.id
    admin_user_ids=[123456555] # ADD Admin user user id to here
    if x not in admin_user_ids:
        return
    else:
        with open(json_file , 'r') as f:
             user_ids = json.load(f)
             count = len(user_ids)
             #stats Countdown Command
        await message.reply_text(f"🙎‍♂️ All Users : {count}\n\n")


#◇──────────────────────────── Filter IP Addresses ─────────────────────────────◇

@app.on_message(filters.text & filters.private)
async def get_ip(client: Client, message: Message):
    global x,ip_address
    ip_address=message.text
    try:
        ip = ipaddress.ip_address(ip_address)
        await app.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
        if isinstance(ip, ipaddress.IPv4Address) or isinstance(ip, ipaddress.IPv6Address):

            # IPINFO API TOKEN
            access_token = config.con.IP_API
            handler = ipinfo.getHandler(access_token)
            ip = handler.getDetails(ip_address)

            # Assign All Entities To List
            x = [ip.details.get('ip', None), ip.details.get('country_name', None),
                 ip.details.get('continent', {}).get('name', None), ip.details.get('region', None),
                 ip.details.get('city', None), ip.details.get('postal', None), ip.details.get('timezone', None),
                 ip.details.get('latitude', None), ip.details.get('longitude', None), ip.details.get('loc', None),
                 ip.details.get('country_currency', {}).get('code', None), ip.details.get('org', None),
                 ip.details.get('country_flag', {}).get('emoji', None)]

            url = f"https://maps.locationiq.com/v3/staticmap?key=pk.{'YOUR API KEY'}&center={x[7]},{x[8]}&zoom=16&size=600x600&markers=icon:large-blue-cutout%7C{x[7]},{x[8]}"
            ip_data[message.chat.id] = {
            'ip_address': x[0]}
            try:
                # Make the API request
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for non-200 status codes

                inline_keyboard = InlineKeyboardMarkup([ [InlineKeyboardButton('✈️ Open Location Via Google Map 🌎‍',url=f'https://www.google.com/maps/search/?api=1&query={x[7]}%2C{x[8]}')]])
                await app.send_photo(chat_id=message.chat.id,
                               photo=url,
                               caption=f"🍀 Location Found 🔎\n\n🛰IP Address ➤ {x[0]}\n🌎Country ➤ {x[1]}{x[12]}\n💠continent ➤{x[2]}\n🗺Province ➤ {x[3]}\n🏠City ➤ {x[4]}\n✉️ Postal Code ➤<code> {x[5]} </code>\n🗼Internet Provider ➤ {x[11]}\n🕢Time Zone➤ {x[6]}\n〽️Location ➤<code>{x[9]}</code>\n💰 Currency ➤ {x[10]} \n\n🔥Powered By @Codex_SL 🇱🇰",
                               reply_markup=inline_keyboard)

            except requests.exceptions.RequestException as e:
                #IF API request limit Exceeded Switch to location sharing option
                try:
                    inline_keyboard1 = InlineKeyboardMarkup([[InlineKeyboardButton("IP Finder Bot", url="https://t.me/IPfinderobo_bot")]])
                    await app.send_location(chat_id=message.chat.id,  latitude=float(x[7]), longitude=float(x[8]))
                    await app.send_message(chat_id=message.chat.id,text=f"🍀 Location Found 🔎\n\n🛰IP Address ➤ {x[0]}\n🌎Country ➤ {x[1]}{x[12]}\n💠continent ➤{x[2]}\n🗺Province ➤ {x[3]}\n🏠City ➤ {x[4]}\n✉️ Postal Code ➤<code> {x[5]} </code>\n🗼Internet Provider ➤ {x[11]}\n🕢Time Zone➤ {x[6]}\n〽️Location ➤<code>{x[9]}</code>\n💰 Currency ➤ {x[10]} \n\n🔥Powered By @Codex_SL 🇱🇰",reply_markup=inline_keyboard1)         
                except:
                    await app.send_message(chat_id=message.chat.id,text="Invalid ip or Private ip Address ❌")
    except ValueError:
        return
    

#◇──────────────────────────── Inline Mode ─────────────────────────────◇

@app.on_inline_query()
async def inline_query_handler(client: Client, query: InlineQuery):
    results = []
    query_str = query.query.strip()

    try:
        ipdata = ipaddress.ip_address(query_str)
        if isinstance(ipdata, ipaddress.IPv4Address) or isinstance(ip, ipaddress.IPv6Address):
            access_token = config.con.IP_API
            handler = ipinfo.getHandler(access_token)
            ip = handler.getDetails(ipdata)

            # Assign All Entities To List
            x = [ip.details.get('ip', None), ip.details.get('country_name', None),
                 ip.details.get('continent', {}).get('name', None), ip.details.get('region', None),
                 ip.details.get('city', None), ip.details.get('postal', None), ip.details.get('timezone', None),
                 ip.details.get('latitude', None), ip.details.get('longitude', None), ip.details.get('loc', None),
                 ip.details.get('country_currency', {}).get('code', None), ip.details.get('org', None),
                 ip.details.get('country_flag', {}).get('emoji', None)]

            results = [
            InlineQueryResultPhoto(
            photo_url=f"https://telegra.ph/file/dba626143ccfea3c4d718.jpg",
            id="80100192",
            thumb_url=f"https://telegra.ph/file/dba626143ccfea3c4d718.jpg",
            title='🌎 Inline Share Location 🔎',
            description=f"🍀 Location Found :{x[0]}",
            caption=f"🍀 Location Found 🔎\n\n🛰IP Address ➤ {x[0]}\n🌎Country ➤ {x[1]}{x[12]}\n💠continent ➤{x[2]}\n🗺Province ➤ {x[3]}\n🏠City ➤ {x[4]}\n✉️ Postal Code ➤<code> {x[5]} </code>\n🗼Internet Provider ➤ {x[11]}\n🕢Time Zone➤ {x[6]}\n〽️Location ➤<code>{x[9]}</code>\n💰 Currency ➤ {x[10]} \n\n🔥Powered By @Codex_SL 🇱🇰",         
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('‍🔥Codex SL 🇱🇰', url='https://t.me/Codex_SL')],[InlineKeyboardButton('🤖 IP ҒIΠDΣR BOT 🔎', url='https://t.me/IPfinderobo_bot')]]),
    )]
            await client.answer_inline_query(query.id, results=results,cache_time=2)

    except ValueError:
        pass

if __name__ == '__main__':
    app.run()
