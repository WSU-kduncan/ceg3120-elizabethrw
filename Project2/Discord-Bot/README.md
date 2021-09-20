Project 2 R&D
---
Name: Elizabeth Wright
---

Setup
---
1. How to get an API: Go to the Discord developer portal, create an application. In "General Information", there is an application ID and public key (this is the API application).
2. Where to put it to work with the code: Now that we have an APi, we need to create a bot (use the Bot option on the side, give the bot a name and permissions and save), then go to "OAuth2", then click "bot" and choose bot permissions (choosing "Administrator" is one option that allows everything). Copy and paste the HTTPS link into your browser, and choose the guild you would like to add the bot to, and authorize it - Now the bot is in a guild it can operate in. We also must put the token of the bot and the guild name in .env, and .env in .gitignore for the code to work (and to hide this information from being pushed publicly). Once the code is running, I can confirm it works by typing "bee!" and getting the correct response from the bot, and merging the differences to my main branch.
3. Dependencies: discord.py, python-dotenv, python3, python3-pip. 

Usage
---

4. Commands I can type in my discord server: bee!
5. What response this provides from my bot: One of the bee_movie_quotes.

Research
---

6. To keep the program/bot active, the script needs to be hosted somewhere at all times. A person could use a server for discord bots to continually run on, called a VPS (Virtual Private Server). This would work because it is a way for your program to be continually running, just like if it were to run on a computer's terminal at all times. Using the Cloud to run the Discord bot would also work for the same reason a VPS would.

