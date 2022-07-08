import discord, asyncio, datetime, base64
from discord.ext import commands
from mcstats import mcstats

info = {
	"ip":"46.4.71.235",
	"port":43819,
	"motd":"EditedWorld",
	"version":"1.19.2"
}

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
	msg = await client.fetch_channel(939644567240724510)
	try:
		msg = await msg.fetch_message(939645619138617394)
	except Exception as e:
		print(e)
		exit()
	while True:
		try:
			with mcstats(info["ip"], port=info["port"], timeout=10) as server:
				online = True
		except:
			online = False
		embed = discord.Embed(title=info["motd"], description=f"Айпи: `{info['ip']}`\nПорт: `{info['port']}`\nВерсия: `{info['version']}`", timestamp=datetime.datetime.utcnow())
		if online:
			embed.color = discord.Color.green()
			embed.add_field(name="Статус: 🟢Онлайн", value=f"Игроки: {server.num_players}/{server.max_players}\nПинг: {round(server.ping_id/1000%60)}ms", inline=False)
		else:
			embed.color = discord.Color.red()
			embed.add_field(name="Статус: 🔴Оффлайн", value="""Попросите запустить сервер!""", inline=False)
		if msg:
			await msg.edit(embed=embed)
		else:
			msg = await msg.send(embed=embed)
		await asyncio.sleep(10)

client.run(base64.b64decode("T0RFek56UXdNRE01TVRjd01qa3pPREl4LllEVHNkdy5SblhxemV1N1NRZUZ2ZVFwZ2lIU0pmSjl2Mlk=").decode("utf-8", "ignore"))
