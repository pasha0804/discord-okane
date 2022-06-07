# Discord coinbot written in python by vanshiyo#0001
# Copyright © vanshiyo 2022 - All Rights Reserved

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def flip(ctx):
    """Flips a coin... or a user.
    Looks through the messages history to check for user input.
    If no user is specified, the bot will flip itself.
    Keyword arguments:
    ctx -- the context of the invocation
    """

    # check if we're targeting someone specific
    try:
        user = ctx.message.mentions[0]
    except IndexError:
        user = ctx.message.author

    # 50% chance
    if random.randint(1, 2) == 1:
        await ctx.send(user.mention + " got heads!")
    else:
        await ctx.send(user.mention + " got tails!")

@bot.command(pass_context=True)
async def roll(ctx, number : int = 6):
    """Rolls a dice
    Defaults to 6 sided dice.
    Keyword arguments:
    ctx -- the context of the invocation
    number -- the number of sides on the dice
    """

    rl = str(random.randint(1, number))

    await ctx.send(ctx.message.author.mention + " rolled a " + rl)
    await ctx.send(rl + " has been added to your balance. Check with !balance")

    # open the balance file and read the current balance
    f = open("balances.txt", "r")
    balances = {}
    for line in f:
        # each line is in the format "name:balance"
        (name, balance) = line.split(":")
        balances[name] = int(balance)

    # write the file back out
    f = open("balances.txt", "w")
    for name in balances:
        f.write(name + ":" + str(balances[name]) + "\n")

    await ctx.send(ctx.message.author.mention + " now has " + str(balances[ctx.message.author.name]) + " coins!")

@bot.command(pass_context=True)
async def balance(ctx):
    """Displays a user's balance.
    Keyword arguments:
    ctx -- the context of the invocation
    """

    # open the balance file and read the current balance
    f = open("balances.txt", "r")
    balances = {}
    for line in f:
        # each line is in the format "name:balance"
        (name, balance) = line.split(":")
        balances[name] = int(balance)

    # check if the user is in the file
    if ctx.message.author.name in balances:
        await ctx.send(ctx.message.author.mention + " has " + str(balances[ctx.message.author.name]) + " coins!")
    else:
        await ctx.send(ctx.message.author.mention + " has no coins!")

bot.run('TOKEN') # here you just have to add your bot-token to get the bot working!
