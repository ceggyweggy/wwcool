import requests

from config import TELEGRAM_SEND_MESSAGE_URL

import time 
import random 
import telegram_bot 
import telegram 
import telegram.ext 

random.seed()
# 712481525, chloe, 204, robo
intros = 4
intro_names = ["cadence (or cegg(y) (weggy) or any variation of cadence, really)", "andreaaaaaa", "emma", "adele", "chloe"]
intro_classes = ["212", "idk but er 212'20 yes", "210", "204", "204"]
intro_cca = ["robo", "girl guidesssssss wuhu", "robo", "shooting", "robo"]
intro_id = [861886075 ,1254075693, 1206367870, 1119686699, 712481525]

current_id = 975508200

unixtime = int(time.time())

def name_to_id(name):
    chat_id=0
    if name=="Min Min" or name=="min min" or name=="mm" or name=="min":
        chat_id=1214863553
    elif name=="Testing" or name=="testing":
        chat_id=-492168190
    elif name=="WW Cool" or name=="ww cool" or name=="WW cool":
        chat_id=-1001199978565
    elif name=="Cadence" or name=="cadence" or name=="Cadonk" or name=="cadonk" or name.startswith("cegg"):
        chat_id=861886075
    elif name.startswith("chloe") or name=="Crowee" or name=="crowee":
        chat_id=712481525
    elif name=="xf" or name=="xuefei" or name=="Xuefei" or name=='xf':
        chat_id=771649055
    elif name=="neha" or name=="Neha" or name.startswith("sk"):
        chat_id=1200619160
    elif name.startswith("adele") or name.startswith("Adele") or name.startswith("ADELE"):
        chat_id=1119686699
    elif name=="yx" or name=="yuxuan" or name=="Yuxuan":
        chat_id=1235169098
    elif name=="emma" or name=="EMMA" or name=="RMMA" or name=="rmma":
        chat_id=1206367870
    elif name=="Zanna" or name=="Zyles" or name=="zanna" or name=="zyles" or name=="zxnna":
        chat_id=1149401183
    elif name.startswith("Past Curfew") or name.startswith("past curfew"):
        chat_id=-434170116
    elif name=="teapot" or name=="Teapot" or name=="raewyn" or name=="Raewyn":
        chat_id=811427963
    elif name=="xavii" or name=="Xavii" or name=="Xaviera" or name=="xaviera":
        chat_id=1123398215
    elif name=="hihihi":
        chat_id=-452778702
    elif name=="celina":
        chat_id=877122271
    elif name=="safer":
        chat_id=-415464047
    else:
        chat_id=0
    return chat_id #if chat_id=0 then invalid

class TelegramBot:

    def __init__(self):
        """"
        Initializes an instance of the TelegramBot class.
        Attributes:
            chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
            text:str: Text of Telegram chat
            first_name:str: First name of the user who sent the message
            last_name:str: Last name of the user who sent the message
        """

        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None


    def parse_webhook_data(self, data):
        global unixtime
        global current_id

        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions
        Args:
            data:str: JSON string of data
        """ 

        # if data['update_id'] < current_id:
        #     self.incoming_message_text = "Edited message"
        #     return

        current_id = data['update_id']
        # if utils.helpers.effective_message_type(data) == "message":
        message = data['message']
        # else:
            # self.incoming_message_text = "Not a message"

        if message['date'] < unixtime:
            self.incoming_message_text = "rawre"
            return

        self.chat_id = message['chat']['id']

        self.incoming_message_text = message['text'].lower()

        self.first_name = message['from']['first_name']
        # self.last_name = message['from']['last_name']
        print(self.chat_id, end=", ")
        print(self.first_name, end=", ")
        print(current_id)


    def action(self):
        """
        Conditional actions based on set webhook data.
        Returns:
            bool: True if the action was completed successfully else false
        """
        global intros 
        global intro_cca
        global intro_names
        global intro_classes
        global intro_id

        success = None



        if self.incoming_message_text.startswith('/hello'):
            self.outgoing_message_text = "Hello {}!".format(self.first_name)
            success = self.send_message()
        
        if self.incoming_message_text.startswith('/start') and (not self.incoming_message_text.startswith('/startgame') and not self.incoming_message_text.startswith('/startchaos')):
            self.outgoing_message_text = "This is for managing ww cool - introductions mainly."
            success = self.send_message()

        if self.incoming_message_text.startswith('/intro'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success 
            if not self.chat_id in intro_id:
                intro_id.insert(intros, self.chat_id)
                self.outgoing_message_text = "What is your name? (use /name in front of your answer because the coder of this is lazy 😔)"
                success = self.send_message()
            else:
                self.outgoing_message_text = "If you haven't finished, pls go scroll to find where u left off bc i lazy"
                success = self.send_message()
                return success 
            # intro_names.insert(intros, self.first_name)

        if self.incoming_message_text.startswith('/name'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success
            if self.chat_id in intro_id:
                nname = self.incoming_message_text[6:]
                intro_names.insert(intros, nname)
                self.outgoing_message_text = "What is your class? (use /class in front of answer pls pls thank you) (also ignore if finished)"
                success = self.send_message()
                return success 

        if self.incoming_message_text.startswith('/class'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success
            if not self.chat_id in intro_id:
                self.outgoing_message_text = "Please type /intro to begin writing your introduction :c)"
                success = self.send_message()
                return success 
            y2_class = self.incoming_message_text[7:]
            intro_classes.insert(intros, y2_class)
            self.outgoing_message_text = "What CCA are you in? (use /cca in front of answer bc Lazy thank you) (Ignore if finished)"
            success = self.send_message()

        if self.incoming_message_text.startswith('/cca'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success
            if not self.chat_id in intro_id:
                self.outgoing_message_text = "Please type /intro to begin writing your introduction :c)"
                success = self.send_message()
                return success
            cca = self.incoming_message_text[5:]
            intro_cca.insert(intros, cca)
            print(intro_id[intros], end=", ")
            print(intro_names[intros], end=", ")
            print(intro_classes[intros], end=", ")
            print(intro_cca[intros])
            intros += 1
            self.outgoing_message_text = "Intro done! Try /getintro <name> to see intros :c)"
            success = self.send_message()

        if self.incoming_message_text.startswith('/getintro'):
            req_name = self.incoming_message_text[10:]
            for i in intro_names:
                if i.startswith(req_name):
                    index = intro_names.index(i)
                    self.outgoing_message_text = "Name: "
                    self.outgoing_message_text += intro_names[index]
                    self.outgoing_message_text += "\nClass: "
                    self.outgoing_message_text += intro_classes[index]
                    self.outgoing_message_text += "\nCCA: "
                    self.outgoing_message_text += intro_cca[index]
                    success = self.send_message()
                    return success 
            
            self.outgoing_message_text = "Person/intro not found."
            success = self.send_message()

        if self.incoming_message_text.startswith('/games'):
            self.outgoing_message_text = "Games:\n- Werewolf (/ww)\n- Bridge (/bridge)\n- Quizarium (/quizarium)\n- Word chain (/wordchain)"
            success = self.send_message()

        if self.incoming_message_text.startswith('/ww'):
            self.outgoing_message_text = "ww rules:\nIf you're good, find the bad guys. If you're bad, kill everyone else. If you're neutral, do as your role dictates. /rolelist for all roles."
            success = self.send_message()

        if self.incoming_message_text.startswith('/bridge'):
            self.outgoing_message_text = "Bridge rules: https://tinyurl.com/wwcoolbridgerules"
            success = self.send_message()

        if self.incoming_message_text.startswith('/quizarium'):
            self.outgoing_message_text = "Quizarium rules:\n- Answer the questions.\nPlease don't change the language, thanks :c)"
            success = self.send_message()

        if self.incoming_message_text.startswith('/wordchain'):
            self.outgoing_message_text = "Word chain!! Chain words."
            success = self.send_message()

        if "hello" in self.incoming_message_text:
            self.outgoing_message_text = "Hello!"
            success = self.send_message()

        if "fuck" in self.incoming_message_text or "shit" in self.incoming_message_text:
            self.outgoing_message_text = "Don't swear, " + self.first_name + '.'
            success = self.send_message()

        if "eww" in self.incoming_message_text or "disgusting" in self.incoming_message_text or "gross" in self.incoming_message_text:
            self.outgoing_message_text = "🤮"
            success = self.send_message()

        if " ww " in self.incoming_message_text or "werewolf" in self.incoming_message_text:
            self.outgoing_message_text = "🐺"
            success = self.send_message()

        if "haha" in self.incoming_message_text or "hehe" in self.incoming_message_text or ":cD" in self.incoming_message_text:
            replies = ["😃", "🤣", "😝", "😆", "😄", "🤪", "😛", "😁", "😀"]
            self.outgoing_message_text = replies[random.randint(0, len(replies)-1)]
            success = self.send_message()

        if "hmm" in self.incoming_message_text:
            self.outgoing_message_text = "🤔"
            success = self.send_message()

        if "awesome" in self.incoming_message_text or " orz " in self.incoming_message_text or " pro " in self.incoming_message_text:
            self.outgoing_message_text = "🤩"
            success = self.send_message()

        if "woohoo" in self.incoming_message_text or " woo" in self.incoming_message_text or "woo " in self.incoming_message_text:
            self.outgoing_message_text = "🥳"
            success = self.send_message()

        if "epic" in self.incoming_message_text or "cool" in self.incoming_message_text or "swag" in self.incoming_message_text:
            self.outgoing_message_text = "😎"
            success = self.send_message()

        if ":c(" in self.incoming_message_text or "Dc:" in self.incoming_message_text:
            self.outgoing_message_text = "Don't be ced. Be happy! :cD"
            success = self.send_message()

        if "please" in self.incoming_message_text or "cute" in self.incoming_message_text or " aww" in self.incoming_message_text or "aww " in self.incoming_message_text:
            self.outgoing_message_text = "🥺"
            success = self.send_message()

        if "smort" in self.incoming_message_text or "smart" in self.incoming_message_text:
            self.outgoing_message_text = "🤓"
            success = self.send_message()

        if "arso" in self.incoming_message_text:
            self.outgoing_message_text = "🔥"
            success = self.send_message()

        if self.incoming_message_text == "Left member!":
            self.outgoing_message_text = "So long!"
            success = self.send_message()

        if self.incoming_message_text == "New member!":
            self.outgoing_message_text = "Hello, and welcome to ww cool! Try /intro to set an intro (in pms)"
            success = self.send_message()

        # if self.incoming_message_text.startswith("/changeintro"):
        #     keyboard = [
        #     [
        #     InlineKeyboardButton("Name", callback_data=str(ONE)),
        #     InlineKeyboardButton("Class", callback_data=str(TWO)),
        #     InlineKeyboardButton("CCA", callback_data=str(THREE))
        #     ]
        #     ]

        #     reply_markup = InlineKeyboardMarkup(keyboard)
        #     self.outgoing_message_text = "Please choose info to change"
        #     res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text, reply_markup=reply_markup))
        #     return True if res.status_code == 200 else False 


        return success


    def send_message(self):
        """
        Sends message to Telegram servers.
        """

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

        return True if res.status_code == 200 else False
    

    @staticmethod
    def init_webhook(url):
        """
        Initializes the webhook
        Args:
            url:str: Provides the telegram server with a endpoint for webhook data
        """

        requests.get(url)