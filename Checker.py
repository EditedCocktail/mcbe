import discord, asyncio, datetime, base64
from discord.ext import commands
from mcstatus import MinecraftBedrockServer

info = {
	"ip":"panda.de.freemcserver.net",
	"port":"25816",
	"motd":"EditedWorld",
	"version":"1.18.0"
}

server = MinecraftBedrockServer.lookup(info["ip"]+":"+info["port"])

client = commands.Bot(command_prefix="be.", intents=discord.Intents.all(), activity=discord.Game(name="Bedrock Server"), status=discord.Status.idle)
client.remove_command("help")

msg = False

@client.event
async def on_ready():
	global msg, info
	print(f"""------------------------------
Имя: {client.user.name}
Айди: {client.user.id}
Серверов: {len(client.guilds)}
------------------------------""")
	msg = await client.fetch_channel(826034127547138049)
	try:
		msg = await msg.fetch_message(936241607051735051)
	except:
		pass
	while True:
		online = True
		vars = [info['version'], info['motd']]
		try:
			info["status"] = server.status()
			vars = [info['status'].version.version, info['status'].motd]
		except:
			online = False
		embed = discord.Embed(title=vars[1], description=f"Айпи: `{info['ip']}`\nПорт: `{info['port']}`\nВерсия: `{vars[0]}`", timestamp=datetime.datetime.utcnow())
		if online:
			embed.color = discord.Color.green()
			embed.add_field(name="Статус: 🟢Онлайн", value=f"Игроки: {info['status'].players_online}/{info['status'].players_max}\nПинг: {round(info['status'].latency*1000)}ms", inline=False)
		else:
			embed.color = discord.Color.red()
			embed.add_field(name="Статус: 🔴Оффлайн", value="Игроки: 0/20\nПинг: 0ms", inline=False)
		if msg:
			await msg.edit(embed=embed)
		else:
			msg = await msg.send(embed=embed)
		await asyncio.sleep(10)

client.run(base64.b64decode("T0RFek56UXdNRE01TVRjd01qa3pPREl4LllEVHNkdy5SblhxemV1N1NRZUZ2ZVFwZ2lIU0pmSjl2Mlk=").decode("utf-8", "ignore"))