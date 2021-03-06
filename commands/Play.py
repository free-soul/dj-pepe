import discord.ext.commands as commands 
import discodo, asyncio, re 

from classes.FormatDuration import formatDuration

class Play(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio
        self.youtube_matcher_url = re.compile(r'https?://(?:www\.)?.+')

    @commands.command()
    async def join(self, ctx):

        try:
            VC = await self.audio.connect(ctx.author.voice.channel)
        except discodo.NodeNotConnected:
            return await ctx.send("There is no available node.")
        except asyncio.TimeoutError:
            return await ctx.send("The connection is not established in 10 seconds.")

        await VC.setContext({"text_channel": ctx.channel.id})

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            await ctx.invoke(self.join)

        if self.youtube_matcher_url.match(query):

            source = await ctx.voice_client.loadSource(query)
            current = await ctx.voice_client.getCurrent()

            if isinstance(source, list):
                source = source[0]

            if not current:
                return await ctx.reply("πΆ  **{0}**(μ)λ₯Ό μ¬μν©λλ€..".format(source.title), mention_author=False)
            else:
                return await ctx.reply("πΆ  **{0}**(μ΄)κ° μ¬μ λͺ©λ‘μ μΆκ°λμμ΅λλ€".format(source.title), mention_author=False)

        sources = await ctx.voice_client.searchSources(query)
        if not sources:
            return await ctx.reply("π  **{0}**μ κ΄λ ¨λ λΈλλ₯Ό μ°Ύμ μ μμ΅λλ€..", mention_author=False)

        search_titles = ""
        check_numbers = []

        for number in range(0, int(len(sources))):

            if int(number + 1) <= 5:
                check_numbers.append(str(number + 1))
                search_titles += "**#{0}**. {1} ({2})\n".format(number + 1, sources[number].title, formatDuration(sources[number].duration))

        message = await ctx.send("`π μλμ νΈλ μ€ νλλ₯Ό μ νν΄ μ¬μν  μ μμ΅λλ€.`\n{0}".format(search_titles))
        
        def check(message) -> True:
            return message.author.id == message.author.id and message.channel == ctx.channel and message.content in check_numbers

        try:

            user = await self.client.wait_for('message', check=check, timeout=30)
            if user.channel == ctx.channel and user.content in check_numbers:

                await user.delete()
                await sources[int(user.content) - 1].put()

                current = await ctx.voice_client.getCurrent()
                if not current:
                    return await message.edit(content="πΆ  **{0}**(μ)λ₯Ό μ¬μν©λλ€..".format(sources[int(user.content) - 1].title), mention_author=False)
                else:
                    return await message.edit(content="πΆ  **{0}**(μ΄)κ° μ¬μ λͺ©λ‘μ μΆκ°λμμ΅λλ€".format(sources[int(user.content) - 1].title), mention_author=False)

        except asyncio.TimeoutError:
            return await message.edit(content="β±  μκ°μ΄ μ΄κ³Όλμ΄ μλμΌλ‘ νΈλ μ νμ΄ μ·¨μλμμ΅λλ€.", mention_author=False)

def setup(client):
    client.add_cog(Play(client))