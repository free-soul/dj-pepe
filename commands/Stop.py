import discord.ext.commands as commands 

class Stop(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command()
    async def stop(self, ctx):

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        await ctx.voice_client.destroy()
        return await ctx.reply("πΆ  λΈλλ₯Ό μ’λ£ν©λλ€.. (λͺ¨λ  μ¬μ λͺ©λ‘μ μ΄κΈ°ννμ΅λλ€)", mention_author=False)

def setup(client):
    client.add_cog(Stop(client))