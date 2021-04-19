'''
LICENSE: The Unlicense
'''

from piqueserver.commands import command, get_player
from twisted.internet.reactor import callLater

def resettimer(self):
    self.messagecount = 0
    self.timerbeingset = False

def apply_script(protocol, connection, config):
    class muteconnection(connection):
        lastmessage = ""
        howoftenthisonefuckingmessage = 0
        messagecount = 0
        timerbeingset = False
        spammer = False
        
        def on_command(self, command, args):
            if command == "pm":
                try:
                    playboy = get_player(self.protocol, args[0])
                    
                except:
                    playboy = None
                self.messagecount +=1
                if self.messagecount > 15:
                    self.mute = True
                    self.spammer = True
                if not self.timerbeingset:
                    callLater(60, resettimer, self)
                    self.timerbeingset = True
                if self.lastmessage == ' '.join(args[1:]):
                    self.howoftenthisonefuckingmessage+=1
                elif self.lastmessage != ' '.join(args[1:]):
                    self.howoftenthisonefuckingmessage = 0
                if self.howoftenthisonefuckingmessage > 5:
                    self.mute = True
                    self.spammer = True
                if self.mute:
                    self.send_chat("You are muted"+(self.spammer)*(" due to abuse of the pm command")+". To be able to send /pm's, write us with /admin")
                    return False
                
                if playboy is not None:
                    self.lastmessage = ' '.join(args[1:])
            return connection.on_command(self, command, args)
    return protocol, muteconnection
