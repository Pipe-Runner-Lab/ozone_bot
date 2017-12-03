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

**NOTE:** The application also need two undocumented files in root.  
   * **password.py**  
      ```python
	  CODE='your password goes here'
	  ```
   * **key.py**  
      ```python
	  TOKEN='your telegram bot token goes here'
	  ```

   You may also have to create a few directories in the root:
   * **screenshot**

## How to use it
Well **cd** into the root directory of Ozone and do this in your terminal,
```bash
python main.py
```  
but you would not want to use it like this. The best way to use Ozone would be to call it automatically on startup using **systemd**
---

## Command list ( Telegram bot commands )
A list of commands that can be directly given from telegram chat. Some commands are security features hence they need a password file as mentioned earlier. When you ask **Bot father** for a new bot, he will let you add a command list, which basically lists all the available commands your bot seems to offer. This is for a visual cue and is completely optional as long as you can remember all your commands :sweat_smile:. I have listed the commands for you to copy/paste them directly when bot father asks for it. Everything you need to know about your telegram bot is excellently documented by the telegram team right [here](https://core.telegram.org/bots). 

start - Check if ozone is awake  
screenshot - Screenshot of your machine (Needs password)  
camerashot - Web cam shot from your machine (Needs password)