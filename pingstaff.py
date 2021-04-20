'''
Script: pingstaff.py
Author: Rakete175
LICENSE: BSD-3

This script lets mods and guards receive /admin messages.
'''


def apply_script(protocol, connection, config):
    class staffconnection(connection):
        def on_command(self, command, message):
            if command == "admin":
                for staffmembers in self.protocol.players.values():
                    if staffmembers.user_types.moderator or staffmembers.user_types.guard:
                        staffmembers.send_chat('To ADMINS from %s: %s' %
                             (self.name, ' '.join(message)))
            return connection.on_command(self, command, message)
    return protocol, staffconnection

