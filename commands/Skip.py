import discord.ext.commands as commands 

class Skip(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['s'])
    async def skip(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        current = await ctx.voice_client.getCurrent()
        if not current:
            return await ctx.reply("π΅  λΈλκ° μ¬μλκ³  μμ§ μμ΅λλ€. (λΈλκ° μ¬μλλμ§ νμΈν΄μ£ΌμΈμ)", mention_author=False)

        await ctx.voice_client.skip()
        return await ctx.reply("πΆ  λΈλλ₯Ό κ°μ λ‘ μ’λ£νμ΅λλ€.", mention_author=False)

def setup(client):
    client.add_cog(Skip(client))