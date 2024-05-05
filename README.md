# Discord-Bot-Clear-Channel
A Discord Bot that Clears a Channel of all messages.

**This bot/script deletes all messages of a channel from newest to oldest sent**

See `clear-channel.py` for script.

Steps:

1. Download the [clear-channel.py](https://github.com/Courage-1984/Discord-Bot-Clear-Channel/blob/main/clear-channel.py) script in the repo above.
2. Create a folder to put the `clear-channel.py` script in.
3. Open a terminal in that folder location.
4. In that terminal run the following:
```sh
  pip install discord.py
```

4. Now edit the `clear-channel.py` script and add the needed values being `YOUR_BOT_TOKEN`, `SERVER_ID` and `CHANNEL_ID`.

**See the following:**

- [How to Get Your Discord Bot Token](https://www.youtube.com/watch?v=aI4OmIbkJH8)

OR:

![dc bot token](https://github.com/Courage-1984/Discord-Bot-Clear-Channel/assets/18268669/3a45074a-4466-45ab-8ec7-e1561cfa4419)


- [How to Get Server ID, Channel ID, User ID in Discord - Copy ID's](https://www.youtube.com/watch?v=NLWtSHWKbAI)

6. Navigate to [https://discord.com/developers/applications](https://discord.com/developers/applications) and click on your application.
7. Click on the `Bot` option in the left navbar and make sure to enable the following: `Presence Intent`, `Server Members Intent` and `Message Content Intent`.
8. Now click on the `OAuth2` option in the left navbar and copy the `Client ID`.
9. Now open [https://discordapi.com/permissions.html](https://discordapi.com/permissions.html) in a new browser tab.
10. Tick the boxes next to: `Administrator`, `Manage Messages`, `Manage Channels`, `Manage Events`, `Send Messages`, `Embed Links`, `Attach Files`, `Read Message History`, `Manage Server`, `View Channels` and `Manage Server`.
11. Now paste your `Client ID` that you copied in the `Client ID:` field at the bottom of the page.
12. Now click on the link provided at the way bottom of the page.
13. Add your bot/application to your chosen server.
14. Click Continue.
15. Now in the terminal that's in the directory which has your `clear-channel.py` script run the following to excecute the script/bot:
```sh
  python clear-channel.py
```

16. Now your script/bot should run smoothly and delete all messages of a channel from newest to oldest sent.

**PS:**

`YOUR_BOT_TOKEN` and `SERVER_ID` should all be enclosed in single qoutations while:

`CHANNEL_ID` should not be enclosed in qoutations at all.

