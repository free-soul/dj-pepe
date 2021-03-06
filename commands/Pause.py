import discord.ext.commands as commands 

class Pause(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command()
    async def pause(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        client_source = await ctx.voice_client.fetchState()
        current = await ctx.voice_client.getCurrent()

        if not current:
            return await ctx.reply("π΅  λΈλκ° μ¬μλκ³  μμ§ μμ΅λλ€. (λΈλκ° μ¬μλλμ§ νμΈν΄μ£ΌμΈμ)", mention_author=False)
        
        if int(client_source['state']) != 3:
            await ctx.voice_client.resume()
            return await ctx.reply("πΆ  λΈλ μΌμ μ μ§λ₯Ό ν΄μ νμ΅λλ€.", mention_author=False)
        else:
            await ctx.voice_client.pause()
            return await ctx.reply("πΆ  λΈλλ₯Ό μΌμ μ μ§νμ΅λλ€. (λͺλ Ήμ΄λ₯Ό νλ² λ μλ ₯νλ©΄ ν΄μ λ©λλ€)", mention_author=False)

def setup(client):
    client.add_cog(Pause(client))