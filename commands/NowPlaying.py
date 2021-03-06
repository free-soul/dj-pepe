import discord.ext.commands as commands 
import discord

from classes.FormatDuration import formatDuration

class NowPlaying(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio
        
    @commands.command(aliases=["np"])
    async def nowplaying(self, ctx):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client.current:
            return await ctx.reply("π΅  λΈλκ° μ¬μλκ³  μμ§ μμ΅λλ€. (λΈλκ° μ¬μλλμ§ νμΈν΄μ£ΌμΈμ)", mention_author=False)
            
        return await ctx.reply("πΆ  {0} (`{1}`)λ₯Ό μ§κΈ μ¬μνκ³  μμ΅λλ€..".format(
            ctx.voice_client.current.title, formatDuration(ctx.voice_client.current.duration)), mention_author=False)

def setup(client):
    client.add_cog(NowPlaying(client))