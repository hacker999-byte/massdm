import os

try:
  import discord
  from discord.ext import commands
except ModuleNotFoundError:
  os.system("pip install discord")

try:
  import time
  from time import sleep
except ModuleNotFoundError:
  os.system("pip install time")

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

guild = input('Enter Guild Id To Massdm: ')
timetosleepxd = input('Enter Cooldown To Sleep: ')
msg = input("msg") 
perms = input("Do You Have Perms In Guild yes or no: ")
token = input("tera token dal idher")

print("Server Massdmer By Vishw  (Inactive)#0009")

@client.event
async def on_connect():
	await client.wait_until_ready()
	guildOBJ = client.get_guild(int(guild))
	members = await guildOBJ.chunk()
	timetosleep = int(timetosleepxd)
	for mem in members:
		try:
			await mem.send(msg)
		except:
			continue
			time.sleep(timetosleep)

gxd = guild

@client.event
async def on_ready():
	await client.wait_until_ready()
	guild = client.get_guild(int(gxd))
	timetosleep = int(timetosleepxd)
	if perms == "no" or perms == "No":
		for mem in list(guild.members):
			try:
				await mem.send(msg)
			except:
					continue
					time.sleep(timetosleep)

client.run(token, bot=False) #Make It True If You Are Putting Bot Token
