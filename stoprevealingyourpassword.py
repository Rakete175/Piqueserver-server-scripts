'''
This script prevents accidentally typing a staff password.
Keep in mind that it doesn't prevent against brute force. Please only use safe passwords.

Author: Rakete175
License: BSD-3
'''

from twisted.internet.reactor import callLater
from pyspades.contained import ChatMessage
chat_message = ChatMessage()



def apply_script(protocol, connection, config):
    class dontrevealyourpasswordconnection(connection):
        def on_chat(self, value, type):
            for jobs, passwords in self.protocol.passwords.items():
                if value in passwords:
                    if "client" in self.client_info:
                        if self.client_info["client"] == "OpenSpades":
                            callLater(0.5, self.send_chat_error, "Error occured")
                        elif self.client_info["client"] == "BetterSpades":
                            chat_message.player_id = self.player_id
                            chat_message.chat_type = 6
                            chat_message.value = "Error occured"
                            callLater(0.5, self.send_contained, chat_message)
                        else:
                            callLater(0.5, self.send_chat, "Error occured")
                    else:
                        callLater(0.5, self.send_chat, "Error occured")
                    return False
            return connection.on_chat(self, value, type)
    return protocol, dontrevealyourpasswordconnection
