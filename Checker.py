import nextcord, asyncio, datetime, base64
from nextcord.ext import commands
from mcstats import mcstats

class Bot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.bg_task = self.loop.create_task(self.my_background_task())

	async def my_background_task(self):
		await self.wait_until_ready()
		global msg, info
		try:
			channel = self.get_channel(1004339729988333658)
			msg = await channel.fetch_message(1004342422551134308)
		except Exception as e:
			print(e)
			exit()
		while not self.is_closed():
			try:
				with mcstats(info["ip"], port=info["port"], timeout=10) as server:
					online = True
			except:
				online = False
			embed = nextcord.Embed(title=info["motd"], description=f"Айпи: `{info['ip']}`\nПорт: `{info['port']}`\nВерсия: `{info['version']}`\nСкачать версию: https://mcpedl.org/uploads_files/26-07-2022/minecraft-1-19-11.apk", timestamp=datetime.datetime.utcnow())
			if online:
				embed.color = nextcord.Color.green()
				embed.add_field(name="Статус: 🟢Онлайн", value=f"Игроки: {server.num_players}/{server.max_players}\nПинг: {round(server.ping_id/1000%60)}ms", inline=False)
			else:
				embed.color = nextcord.Color.red()
				embed.add_field(name="Статус: 🔴Оффлайн", value="""Попросите запустить сервер!""", inline=False)
			await msg.edit(embed=embed)
			await asyncio.sleep(20)

info = {
	"ip":"game7.falixserver.net",
	"port":43819,
	"motd":"EditedWorld",
	"version":"1.19.11"
}
msg = False

client = Bot(command_prefix="b.", intents=nextcord.Intents.all(), activity=nextcord.Game(name="EditedWorld Bedrock Server"), status=nextcord.Status.idle)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"""------------------------------
Имя: {client.user.name}
Айди: {client.user.id}
Серверов: {len(client.guilds)}
------------------------------""")

client.run(base64.b64decode("T0RFek56UXdNRE01TVRjd01qa3pPREl4Lkdvb2V6VC5wZzlueWpPYUctaHdHdi1heGltb1AyWkNkR2NlU2RjeFN4dGtFWQ==").decode("utf-8", "ignore"))