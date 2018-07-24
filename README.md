# Bot OZONE
![Bot ozone](https://cdn.dribbble.com/users/101288/screenshots/3489110/4.gif)

A **chat bot** developed for the purpose of serving as a remote control( using proper security measures ), as well as a general purpose bot to talk to me when I am lonely :sweat_smile:...

## Requirements
Ozone is a standard **telegram bot** which is basically a python program running on my personal machine and behaves as a kind of remote extension to it. To achieve the different functionalities it claims, Ozone takes the help of many *third party pip modules* and *stand-alone terminal applications*.
Here is a list of them, and ways to install them.

| Name | Type | Related link |
| --- | --- | --- |
| python-telegram-bot | pip module | [link](https://github.com/python-telegram-bot/python-telegram-bot) |
| ImageMagick | terminal app | Pre-installed |
| fswebcam | terminal app | [link](https://askubuntu.com/questions/106770/take-a-picture-from-terminal) |
| aria2 | terminal app | [link](https://aria2.github.io/) |
| dateparser | pip module | [link](https://dateparser.readthedocs.io/en/latest/#supported-calendars) |

**NOTE:** The application also need one undocumented files in *key* directory of the bot.  
   * **key.py**  
      ```python
	  TOKEN='your telegram bot token goes here'
	  ```

   You may also have to create a few directories in the *root directory*:
   * **screenshot**

## How to use it
Well **cd** into the root directory of Ozone and do this in your terminal,
```bash
python main.py
```
but you would not want to use it like this. The best way to use Ozone would be to call it automatically on startup using **systemd**

---

## Command list ( Telegram bot commands )
A list of commands that can be directly given from telegram chat. Some commands are security features hence they need a password file as mentioned earlier. When you ask **Bot father** for a new bot, he will let you add a command list, which basically lists all the available commands your bot seems to offer. This is for a visual cue and is completely optional as long as you can remember all your commands :sweat_smile:. I have listed the commands for you to copy/paste them directly when bot father asks for it. Everything you need to know about your telegram bot is excellently documented by the telegram team right [here](https://core.telegram.org/bots). The list of commands follow their respective use case and syntax in detail.

start - Check if ozone is awake  
screenshot - Screenshot of your machine (Needs password)  
camerashot - Web cam shot from your machine (Needs password)    
download - Download file using download link(Needs password)  
set_reminder - Set a reminder for the given date and time

### Command Anatomy
1. start  
  * **Syntax:** /start 
  * **Type:** Casual 
  * **Use Case:** This command is used to check if the bot server is awake. This responds differently to owner and non-owner users by checking the user name that is saved in the code. 
2. screenshot  
  * **Syntax:** /screenshot \<password\>   
  * **Type:** Security  
  * **Use Case:** This command can be used to get a screenshot of the machine on which the bot server is running. This is a security measure in case you lend your laptop to someone.
3. camerashot  
  * **Syntax:** /camerashot \<password\>   
  * **Type:** Security  
  * **Use Case:** This command can be used to get a web cam photo from the machine on which the bot server is running. This is a security measure in case you wanna see who is using your laptop.
4. download  
  * **Syntax:** /download \<downloadable_link\> \<password\>   
  * **Type:** Utility  
  * **Use Case:** This command let's you download any kind of file given it's downloadable link on the machine on which the bot is running. This comes in handy if you are low on data/space on your phone.

