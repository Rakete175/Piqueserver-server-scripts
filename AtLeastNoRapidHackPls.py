'''
This script just deactivates the rapid hack detection of Piqueserver.
Useful, because the autokicks are mostly false detects (usually too many registered block destructions) and appear due to latency issues.
LICENSE: BSD-3
'''

def apply_script(protocol, connection, config):
    class RapidHackConnection(connection):
        def on_hack_attempt(self, reason):
            if reason == 'Rapid hack detected':
                self.rapid_hack_detect = False
                print("rApId hAcK dEtEcTeD: " +self.name)
                return False
            return connection.on_hack_attempt(self, reason)
    return protocol, RapidHackConnection
