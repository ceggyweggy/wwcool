import requests

from config import TELEGRAM_SEND_MESSAGE_URL

import time 
import random 
import telegram_bot 
import telegram 
import telegram.ext 

random.seed()
# 712481525, chloe, 204, robo
# 1045960315, jennifer, 212, jingle bells 
# 861886075, cadence (or cegg(y) (weggy) or any variation of cadence, really), 212, robo 
intros = 0
intro_names = ["andreaaaaaa", "emma", "adele", "chloe", "jennifer", "peixin", "cadence", "snow", "xaviera"]
intro_classes = ["312!!!", "308", "204", "204/313", "308", "302.", "212/307", "302", "308"]
intro_cca = ["girl guidesssssss wuhu", "robo!!", "shooting", "robo", "jingle bells", "ncc.", "robo", "art club", "red cross"]
intro_id = [1254075693, 1206367870, 1119686699, 712481525, 1045960315, 1263449655, 861886075, 1196893557, 1123398215]
intro_subj = ['trip hist yay :))', 'cphl', 'nil', 'trip hist,', 'pchl', 'nil', 'pcghhh :c))', "trip geog", "cphl"]
intro_game = ['werewolf cuz idk it\'s fun hehe but bridge close second yay', 'everything but bridge cause it\'s too big brain for me',
'nil', 'a l l (or ma jiang)', 'nil', 'nil', 'bridge ha andrea', "all tbh", "ww"]

bridge_index = 0
bridge_name = ['cadence', 'jennifer', 'andrea', 'chloe']
bridge_score = [11, 6, 12, 11] 

# aries = [] 
# taurus = [] 
# gemini = [] 
# cancer = [] 
# leo = [] 
# virgo = [] 
# libra = [] 
# scorpio = [] 
# sagittarius = [] 
# capricorn = [] 
# aquarius = [] 
# pisces = [] 
# zodiac_names = []
# zodiac_ids = []
# remind_zodiac = []

current_id = 975526612
admin_id = 861886075

unixtime = int(time.time())
send_id = 0
msg_id = 0 
# parseMode = 'MarkdownV2'

# dispatcher.add_handler(MessageHandler(Filters.text, repeater))

def name_to_id(name):
    if name=="ww cool":
        chat_id=-1001199978565
    elif name=="cadence" or name=="cadonk" or name.startswith("cegg"):
        chat_id=861886075
    elif name.startswith("chloe") or name=="crowee":
        chat_id=712481525
    elif name=="xf" or name=="xuefei":
        chat_id=771649055
    elif name.startswith("adele") or name.startswith("defenestration") :
        chat_id=1119686699
    elif name=="yx" or name=="yuxuan":
        chat_id=1235169098
    elif name=="emma":
        chat_id=1206367870
    elif name=="zanna" or name=="zyles" or name=="zxnna":
        chat_id=1149401183
    elif name.startswith("past curfew"):
        chat_id=-434170116
    elif name=="teapot" or name=="raewyn":
        chat_id=811427963
    elif name.startswith("xavii") or name.startswith("xaviera"):
        chat_id=1123398215
    elif name=="hihihi":
        chat_id=-452778702
    elif name=="celina":
        chat_id=877122271
    elif name=="safer":
        chat_id=-1001219366779
    elif name.startswith('jen'):
        chat_id=1045960315
    elif name.startswith('andrea'):
        chat_id=1254075693
    elif name.startswith('pect') or name.startswith('peixin'):
        chat_id=1263449655
    elif name.startswith('snow'):
        chat_id=1196893557
    else:
        chat_id=0
    return chat_id

def id_to_name(chat_id):
    if chat_id==-1001199978565:
        username='ww cool'
    elif chat_id==861886075:
        username='cadence'
    elif chat_id==712481525:
        username='chloe'
    elif chat_id==771649055:
        username='xuefei'
    elif chat_id==1119686699:
        username='adele'
    elif chat_id==1235169098:
        username='yuxuan'
    elif chat_id==1206367870:
        username='emma'
    elif chat_id==1149401183:
        username='zanna'
    elif chat_id==-434170116:
        username='Past Curfew WW Cool'
    elif chat_id==811427963:
        username="raewyn"
    elif chat_id==1123398215:
        username="xaviera"
    elif chat_id==-452778702:
        username="hihihi"
    elif chat_id==877122271:
        username="celina"
    elif chat_id==-1001219366779:
        username='safer'
    elif chat_id==1045960315:
        username='jennifer'
    elif chat_id==1254075693:
        username='andrea'
    elif chat_id==1263449655:
        username='peixin'
    elif chat_id==1196893557:
        username='snow'
    else:
        username=''
    return username

def check_zodiac(zodiac):
    if "aries" in zodiac:
        zodiac = "aries"
    elif "taurus" in zodiac:
        zodiac = "taurus"
    elif 'gemini' in zodiac:
        zodiac = 'gemini'
    elif 'cancer' in zodiac:
        zodiac = 'cancer'
    elif 'virgo' in zodiac:
        zodiac = 'virgo'
    elif 'libra' in zodiac:
        zodiac = 'libra'
    elif 'scorpio' in zodiac:
        zodiac = 'scorpio'
    elif 'sagittarius' in zodiac:
        zodiac = 'sagittarius' 
    elif 'capricorn' in zodiac:
        zodiac = 'capricorn'
    elif 'aquarius' in zodiac:
        zodiac = 'aquarius'
    elif 'pisces' in zodiac: 
        zodiac = 'pisces'
    elif 'leo' in zodiac:
        zodiac = 'leo'
    else:
        zodiac = ''
    return zodiac
'''
def check_compatible(zodiac):
    string = ''
    if zodiac == 'aries':
        if leo==[] and sagittarius=[]:
            string = "Hmm. No one has been found yet."
        else:
            string += "You are compatible with "
            for i in leo: 
                string += i
                string += ', '
            for i in sagittarius:
                string += i
                string += ', '
    elif zodiac=='taurus':
'''

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
        self.incoming_message_text = None
        self.outgoing_message_text = None 


    def parse_webhook_data(self, data):
        global unixtime
        global current_id
        global send_id 
        global msg_id 

        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions
        Args:
            data:str: JSON string of data
        """ 

        if data['update_id'] <= current_id:
            self.incoming_message_text = "Edited message"
            return

        current_id = data['update_id']
        # if utils.helpers.effective_message_type(data) == "message":
        message = data['message']
        # else:
            # self.incoming_message_text = "Not a message"

        if message['date'] < unixtime:
            self.incoming_message_text = "rawre"
            return

        self.chat_id = message['chat']['id']
        msg_id = self.chat_id

        self.incoming_message_text = message['text'].lower()

        self.first_name = message['from']['first_name']
        # self.last_name = message['from']['last_name']

        if self.chat_id > 0 and (not self.chat_id == admin_id):
            self.chat_id = admin_id
            self.outgoing_message_text = "Incoming message from: " + self.first_name + ": " + self.incoming_message_text
            success = self.send_message()
            self.chat_id = msg_id 
            # return success 


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
        global send_id 
        global intro_subj 
        global intro_game 
        global parseMode
        global bridge_score
        global bridge_name
        global aries
        global taurus 
        global gemini
        global cancer
        global leo 
        global virgo 
        global libra
        global scorpio 
        global sagittarius 
        global capricorn
        global aquarius
        global pisces
        global zodiac_names
        global zodiac_ids 

        success = None


        '''
        if self.incoming_message_text.startswith('/zodiac'):
            zodiac = self.incoming_message_text[8:]
            if self.first_name in zodiac_names:
                self.outgoing_message_text = "Hmm, you've already done it. Would you like to be reminded of future updates regarding compatible significant others? (/yes or /no)"
                success = self.send_message()
                return success
            zodiac_names.insert(0, self.first_name)
            zodiac = check_zodiac(zodiac)
            if zodiac == '':
                self.outgoing_message_text = "Zodiac not found?? Check spelling, I don't know."
                success = self.send_message()
                return success 
            self.outgoing_message_text = find_compatible(zodiac) 
            '''


        if self.incoming_message_text.startswith('/statsbridge'):
            self.outgoing_message_text = "Number of games won: "
            for i in bridge_name:
                index = bridge_name.index(i)
                self.outgoing_message_text += "\n"
                self.outgoing_message_text += bridge_name[index]
                self.outgoing_message_text += ": "
                self.outgoing_message_text += str(bridge_score[index])
            success = self.send_message()

        if self.incoming_message_text.startswith('/reportbridge'):
            name = self.incoming_message_text[14:]
            name1 = '' 
            name2 = '' 
            one = True 
            for i in range(0, len(name)):
                if name[i] == ',':
                    one = False
                elif name[i] == ' ':
                    continue 
                elif one: 
                    name1 += name[i]
                else:
                    name2 += name[i]

            name1 = id_to_name(name_to_id(name1))
            name2 = id_to_name(name_to_id(name2))

            if name1 == '' or name2 == '':
                self.outgoing_message_text = "Person(s) not found! (Remember to separate using comma?)"
                success = self.send_message()
                return success 

            one_found = False
            two_found = False

            for i in bridge_name:
                if i == name1:
                    index = bridge_name.index(i)
                    bridge_score[index] += 1
                    one_found = True 
                if i == name2:
                    index = bridge_name.index(i)
                    bridge_score[index] += 1
                    two_found = True 

            if not one_found:
                bridge_name.insert(bridge_index, name1)
                bridge_score.insert(bridge_index, 1)
                bridge_index += 1

            if not two_found:
                bridge_name.insert(bridge_index, name2)
                bridge_score.insert(bridge_index, 1)
                bridge_index += 1

            self.outgoing_message_text = "Update successful!"
            success = self.send_message()

        if self.incoming_message_text.startswith('/reset'):
            for i in bridge_score:
                index = bridge_score.index(i)
                bridge_score[index] = 0
            self.outgoing_message_text = "Scores reset!"
            success = self.send_message()

        
        if self.incoming_message_text.startswith('/start@wwcoolbot') and (not self.incoming_message_text.startswith('/startgame') and not self.incoming_message_text.startswith('/startchaos')):
            self.outgoing_message_text = "This is for managing ww cool - introductions mainly. Use /intro (in pms) to set your intro or /getintro <name> to figure out who someone is."
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
            p_class = self.incoming_message_text[7:]
            for i in intro_id:
                if i == self.chat_id:
                    req_index = intro_id.index(i)
                    break
            if req_index < intros:
                intro_classes[req_index] = p_class 
            else:
                intro_classes.insert(intros, p_class)
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
            for i in intro_id: 
                if i == self.chat_id: 
                    req_index = intro_id.index(i)
            cca = self.incoming_message_text[5:]
            if req_index < intros:
                intro_cca[req_index] = cca 
            else: 
                intro_cca.insert(intros, cca)
                # intros += 1 
            self.outgoing_message_text = "What's your subject combi? (use /subj in front of ans woo)"
            success = self.send_message()
            
        if self.incoming_message_text.startswith('/subj'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success
            if not self.chat_id in intro_id:
                self.outgoing_message_text = "Please type /intro to begin writing your introduction :c)"
                success = self.send_message()
                return success
            for i in intro_id:
                if i == self.chat_id:
                    index = intro_id.index(i)
            subj_combi = self.incoming_message_text[6:]
            if index < intros:
                intro_subj[index] = subj_combi
            else:
                intro_subj.insert(intros, subj_combi)
            self.outgoing_message_text = "What's your favourite game? WW, Bridge, Quizarium or Word Chain? (use /game in front of ans, thx)"
            success = self.send_message()

        if self.incoming_message_text.startswith('/game'):
            if self.chat_id < 0:
                self.outgoing_message_text = "Please PM me."
                success = self.send_message()
                return success
            if not self.chat_id in intro_id:
                self.outgoing_message_text = "Please type /intro to begin writing your introduction :c)"
                success = self.send_message()
                return success
            for i in intro_id:
                if i == self.chat_id:
                    index = intro_id.index(i)
            game = self.incoming_message_text[6:]
            if index < intros: 
                intro_game[index] = game 
            else:
                intro_game.insert(intros, game)
                intros += 1
            self.outgoing_message_text = "Intro done! Use /getintro <name> to get introduction of person"
            success = self.send_message()

        if self.incoming_message_text.startswith('/getintro'):
            req_name = self.incoming_message_text[10:]
            if req_name == 'all':
                for i in intro_id:
                    index = intro_id.index(i)
                    self.outgoing_message_text = "Name: "
                    self.outgoing_message_text += intro_names[index]
                    # self.outgoing_message_text += ' tg://user?id='+str(intro_id[index])
                    # self.outgoing_message_text += ' _testing_'
                    self.outgoing_message_text += "\nClass: "
                    self.outgoing_message_text += intro_classes[index]
                    self.outgoing_message_text += "\nCCA: "
                    self.outgoing_message_text += intro_cca[index]
                    self.outgoing_message_text += "\nSubject combi: "
                    self.outgoing_message_text += intro_subj[index]
                    self.outgoing_message_text += "\nFavourite game: "
                    self.outgoing_message_text += intro_game[index]
                    success = self.send_message()
                return success 
            req_id = name_to_id(req_name)
            if req_id == 0:
                for i in intro_names:
                    if i in req_name:
                        index = intro_id.index(i)
                        req_id = intro_id[index]
            for i in intro_id:
                if i == req_id:
                    index = intro_id.index(i)
                    self.outgoing_message_text = "Name: "
                    self.outgoing_message_text += intro_names[index]
                    # self.outgoing_message_text += ' tg://user?id='+str(intro_id[index])
                    # self.outgoing_message_text += ' @eggieandree test'
                    self.outgoing_message_text += "\nClass: "
                    self.outgoing_message_text += intro_classes[index]
                    self.outgoing_message_text += "\nCCA: "
                    self.outgoing_message_text += intro_cca[index]
                    self.outgoing_message_text += "\nSubject combi: "
                    self.outgoing_message_text += intro_subj[index]
                    self.outgoing_message_text += "\nFavourite game: "
                    self.outgoing_message_text += intro_game[index]
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

        if self.incoming_message_text.startswith('/id'):
            if not self.chat_id == admin_id: 
                self.outgoing_message_text = "Admin only!"
                success = self.send_message()
                return success 
            send_id = name_to_id(self.incoming_message_text[4:])
            self.outgoing_message_text = "ID set!"
            success = self.send_message()

        if self.incoming_message_text.startswith('/send'):
            if not self.chat_id == admin_id:
                self.outgoing_message_text = "Admin only!"
                success = self.send_message()
                return success 
            if send_id == 0:
                self.outgoing_message_text = "No ID set!"
                success = self.send_message()
                return success 
            mmessage = self.incoming_message_text[6:]
            self.outgoing_message_text = mmessage 
            self.chat_id = send_id
            success = self.send_message()
            self.chat_id = admin_id
            self.outgoing_message_text = "Message sent!"
            success = self.send_message()
            return success 

        if self.incoming_message_text.startswith('/update'):
            if not self.chat_id == admin_id:
                self.outgoing_message_text = "Admin only!"
                success = self.send_message()
                return success 
            self.outgoing_message_text = "hello. intros update - /subj (for subj combi). try!! thanks."
            for i in intro_id:
                self.chat_id = i
                success = self.send_message()

        if self.incoming_message_text.startswith('/hug'):
            req_id = name_to_id(self.incoming_message_text[5:])
            if req_id == 0:
                self.outgoing_message_text = "Person not found."
                success = self.send_message()
                return success 

            sender = id_to_name(self.chat_id)
            if sender == '':
                sender = self.first_name

            # self.chat_id = req_id 
            self.outgoing_message_text = id_to_name(self.chat_id) + " gave you a hug!"
            self.chat_id = req_id
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

        if (" ww " in self.incoming_message_text or "werewolf" in self.incoming_message_text) and not "ww cool" in self.incoming_message_text:
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

        if "epic" in self.incoming_message_text or "swag" in self.incoming_message_text:
            self.outgoing_message_text = "😎"
            success = self.send_message()

        if ":c(" in self.incoming_message_text or "dc:" in self.incoming_message_text or ":((" in self.incoming_message_text:
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

        if " sk " in self.incoming_message_text:
            self.outgoing_message_text = "🔪"
            success = self.send_message();

        if "hearts" in self.incoming_message_text:
            self.outgoing_message_text = "❤️"
            success = self.send_message()

        if "diamonds" in self.incoming_message_text:
            self.outgoing_message_text = "♦️"
            success = self.send_message()

        if "clubs" in self.incoming_message_text:
            self.outgoing_message_text = "♣️"
            success = self.send_message()

        if "spades" in self.incoming_message_text:
            self.outgoing_message_text = "♠️"
            success = self.send_message()

        if "spock" in self.incoming_message_text:
            self.outgoing_message_text = "🖖"
            success = self.send_message()

        if self.incoming_message_text == "left member!":
            self.outgoing_message_text = "So long!"
            success = self.send_message()

        if self.incoming_message_text == "new member!":
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
        global parseMode

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
