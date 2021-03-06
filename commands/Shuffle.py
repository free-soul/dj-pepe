import discord.ext.commands as commands 

class Shuffle(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['sh', 'shuff'])
    async def shuffle(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        queues = ctx.voice_client.Queue
        if int(len(queues)) <= 0:
            return await ctx.reply("π΅  λ€μμ μ¬μ λͺ©λ‘μ΄ λΉμ΄μμ΅λλ€. (μΆκ°ν ν λ€μ μλ ₯ν΄μ£ΌμΈμ)", mention_author=False)

        await ctx.voice_client.shuffle()
        return await ctx.reply("πΆ  λκΈ° μ€μΈ λͺ¨λ  μ¬μ λͺ©λ‘μ λλ€μΌλ‘ λ€μμμ΅λλ€.", mention_author=False)

def setup(client):
    client.add_cog(Shuffle(client))