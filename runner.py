import discord
from command import Command

class Runner(discord.Client):
    """
    Wraps the discord bot client and runs the commands for you
    """
    def __init__(self,token : str):
        super().__init__()
        self.token = token
        self.client = discord.Client()

    def add_command(self, cmd : Command):
        pass

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    def run(self):
        super(Runner,self).run(self.token)
    
