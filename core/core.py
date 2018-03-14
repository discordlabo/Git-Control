if 1:
    try:
        print('  Git Control Discord Bot 0.2.0 Canary')
        import discord
        from discord.ext.commands import Bot
        from discord.ext import commands
        import asyncio
        from subprocess import Popen,STDOUT
        from json import load
        from shlex import split
        print('i Imported required modules (discord,asyncio,subprocess,json.load,shlex.split)')

        tokenFileObj = open('../variables/token.json','r')
        tokenFileJsonRaw = load(tokenFileObj)
        tokenFileObj.close()
        tokenBot = tokenFileJsonRaw['token']
        print('i Loaded ../variables/token.json')

        client = discord.Client()
        bot = commands.Bot(command_prefix = "?")
        print('i client,bot inited')

        @bot.event
        async def on_ready():
            print('i Online & Connected')

        @bot.event
        async def on_message(message):
            # print('i Message Received ({})'.format(message.content))
            if message.content == 'git:test':
                # print('i Message Responding (message[0:3] is {})'.format(message.content[0:3]))
                await bot.send_message(message.channel,'Git Control Bot 0.2.0 Canary is doing fine.')
                # bot.send_message(message.channel, ':weary: Git Control is not finished...')
                # print('i Message Sent ({})'.format(':weary: Git Control is not finished...'))
            elif message.content[0:4] == 'git:':
                message.content += ' '
                await bot.send_message(message.channel,'Running {}...'.format(message.content[4:-1]))
                gitProcess = Popen(split(message.content[4:-1]),stdout=-1,stderr=-1)
                stdout,stderr = gitProcess.communicate()
                await bot.send_message(message.channel,'Ran {}.'.format(message.content[4:-1]))
                # await bot.send_message(message.channel,'Stdout:\n{}\nStderr:\n{}'.format(stdout,stderr))
                await bot.send_message(message.channel,'{}'.format(stdout.decode('utf-8')))

        bot.run(tokenBot)
    except:
        print('i Restart')
