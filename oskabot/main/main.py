import os
import time
import httpx

class BotAPI:

    def __init__ (self,api):
        self.api = api
        self.request = None
        self.success = False
        self.result = []
        
    def getUpdates (self):
        self.request = httpx.get(self.api+"/getUpdates")
        self.success,self.result = self.request.json().values()
        return self.success,self.result
        
    def sendMessage (self,message):
        self.request = httpx.post(self.api+"/sendMessage",json = message)
        self.success,self.result = self.request.json().values()
        return self.success,self.result
        
  
class BaseObject:

    def __getitem__ (self,name):
        return super().__getattribute__(name)
        
    def __setitem__ (self,name,val):
        super().__setattr__(name,val)
        
        
class Update(BaseObject):
    
    __slots__ = (
        "update_id",
        "message",
        "edited_message",
        "channel_post",
        "edited_channel_post",
        "inline_query",
        "chosen_inline_result",
        "callback_query",
        "shipping_query",
        "pre_checkout_query",
        "poll",
        "poll_answer",
        "my_chat_member",
        "chat_member",
        "chat_join_request"
        )
    def __init__ (self):
        self.update_id = 0
        self.message = str()
        self.edited_message = str()
        self.channel_post = None
        self.edited_channel_post = None
        self.inline_query = None
        self.chosen_inline_result = None
        self.callback_query = None
        self.shipping_query = None
        self.pre_checkout_query = None
        self.poll = None
        self.poll_answer = None
        self.my_chat_member = None
        self.chat_member = None
        self.chat_join_request = None
        
class Message(BaseObject):
    
    __slots__ = (
        "message_id",
        "from_",
        "sender_chat",
        "date",
        "chat",
        "forward_from_chat",
        "forward_from_message_id",
        "forward_signature",
        "forward_sender_name",
        "forward_date",
        "is_automatic_forward",
        "reply_to_message",
        "via_bot",
        "edit_date",
        "has_protected_content",
        "media_group_id",
        "author_signature",
        "text",
        "entities",
        "animation",
        "audio",
        "document",
        "photo",
        "sticker"
        "video",
        "video_note",
        "voice",
        "caption",
        "caption_entities",
        "contact",
        "dice",
        "game",
        "poll",
        "venue",
        "location",
        "new_chat_members",
        "left_chat_member",
        "new_chat_title",
        "new_chat_photo",
        "delete_chat_photo",
        "group_chat_created"
        "supergroup_chat_created",
        "channel_chat_created",
        "message_auto_delete_timer_changed",
        "migrate_to_chat_id",
        "migrate_from_chat_id",
        "pinned_message",
        "invoice",
        "successful_payment",
        "connected_website",
        "passport_data",
        "proximity_alert_triggered",
        "video_chat_scheduled",
        "video_chat_started",
        "video_chat_ended",
        "video_chat_participants_invited",
        "web_app_data",
        "reply_markup",
        )
    def __init__ (self):
        self.message_id = 0
        self.from_ = None
        self.sender_chat = None
        self.date = None
        self.chat = None
        self.forward_from_chat = None
        self.forward_from_message_id = None
        self.forward_signature = None
        self.forward_sender_name = None
        self.forward_date = None
        self.is_automatic_forward = None
        self.reply_to_message = None
        self.via_bot = None
        self.edit_date = None
        self.has_protected_content = None
        self.media_group_id = None
        self.author_signature = None
        self.text = None
        self.entities = None
        self.animation = None
        self.audio = None
        self.document = None
        self.photo = None
        self.sticker = None
        self.video = None
        self.video_note = None
        self.voice = None
        self.caption = None
        self.caption_entities = None
        self.contact = None
        self.dice = None
        self.game = None
        self.poll = None
        self.venue = None
        self.location = None
        self.new_chat_members = None
        self.left_chat_member = None
        self.new_chat_title = None
        self.new_chat_photo = None
        self.delete_chat_photo = None
        self.group_chat_created = None
        self.supergroup_chat_created = None
        self.channel_chat_created = None
        self.message_auto_delete_timer_changed = None
        self.migrate_to_chat_id = None
        self.migrate_from_chat_id = None
        self.pinned_message = None
        self.invoice = None
        self.successful_payment = None
        self.connected_website = None
        self.passport_data = None
        self.proximity_alert_triggered = None
        self.video_chat_scheduled = None
        self.video_chat_started = None
        self.video_chat_ended = None
        self.video_chat_participants_invited = None
        self.web_app_data = None
        self.reply_markup = None
        
class Chat(BaseObject):

    __slots__ = (
        "id",
        "type",
        "title",
        "username",
        "first_name",
        "last_name",
        "photo",
        "bio",
        "has_private_forwards",
        "description",
        "invite_link",
        "pinned_message",
        "permissions"
        "slow_mode_delay",
        "message_auto_delete_time",
        "has_protected_content",
        "sticker_set_name",
        "can_set_sticker_set",
        "linked_chat_id",
        "location",
        )
    def __init__ (self):
        self.id = 0
        self.type = None
        self.title = None
        self.username = None
        self.first_name = None
        self.last_name = None
        self.photo = None
        self.bio = None
        self.has_private_forwards = None
        self.description = None
        self.invite_link = None
        self.pinned_message = None
        self.permissions = None
        self.slow_mode_delay = None
        self.message_auto_delete_time = None
        self.has_protected_content = None
        self.sticker_set_name = None
        self.can_set_sticker_set = None
        self.linked_chat_id = None
        self.location = None

class User(BaseObject):

    __slots__ = ("id",
        "is_bot",
        "first_name",
        "last_name",
        "username",
        "language_code",
        "can_join_groups",
        "can_read_all_group_messages",
        "supports_inline_queries",
        )
    def __init__ (self):
        self.id = 0
        self.is_bot = False
        self.first_name = None
        self.last_name = None
        self.username = None
        self.language_code = None
        self.can_join_groups = None
        self.can_read_all_group_messages = None
        self.supports_inline_queries = None
    
class MessageEntity(BaseObject):

    __slots__ = (
        "type",
        "offset",
        "length",
        "url",
        "user",
        "language",
        )
    def __init__ (self):
        self.type = None
        self.offset = None
        self.length = None
        self.url = None
        self.user = None
        self.language = None
        
objs = {
    "message":Message(),
    "chat":Chat(),
    "user":User(),
    "entity":MessageEntity()
    }
    
class BotProgram:
    
    def __init__(self,botapi):
    
        self.botapi = botapi
        self.wait_for = 5*60 # wait for 5 minutes before making an api request.
        self.processed_ids = set()

    def main_program(self):
        #to be implemented in the subclass
        raise NotImplementedError
        
    def run (self):
        self.main_program()
        
    def process_update (self,update,k = None,*,cont = False,cont_obj = None):
        
        upobj = objs[k] if k else cont_obj if cont and cont_obj else Update()
        try:
            for key in update:
                if key in objs:
                    upobj[key] = self.process_update(update.pop(key),key)
                    
                elif key == "from":
                    upobj["from_"] = update.pop(key)
                    
                elif key == "entities":
                    upobj[key] = [self.process_update(update,"entity") for _ in update.pop(key)]
                    
                elif key == "new_chat_members":
                    upobj[key] = [self.process_update(update,"user") for _ in update.pop(key)]
                    
                else:
                    upobj[key] = update.pop(key)
                    
            return upobj 
            
        except RuntimeError:
            self.process_update(update,cont = True,cont_obj = upobj)
            
        return upobj
        
        
class Sanyu(BotProgram):

    def main_program(self):
        print("starting bot program...")
        
        while True:
            succ,res = self.botapi.getUpdates()
            if succ:
                for update in res:
                    if (uid := update["update_id"]) in self.processed_ids:
                        continue
                    self.processed_ids.add(uid)
                    update_obj = self.process_update(update)
                    try:
                        print(update_obj.message.text, end = "\n\n")
                    except:
                        print("has not message")
                    
            time.sleep(self.wait_for)
                    
if __name__ == "__main__":
    bot_api = "insert bot api here before use"
    Sanyu(BotAPI(bot_api)).run()