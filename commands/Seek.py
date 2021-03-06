import discord.ext.commands as commands 

from classes.FormatDuration import formatDuration

class Seek(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    def formatDuration(self, seconds):
        
        seconds = int(seconds)
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)

        return (f"{hour:02}:" if hour else "") + f"{minute:02}:{second:02}"

    @commands.command()
    async def seek(self, ctx, offset: int):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        current = await ctx.voice_client.getCurrent()
        if not current:
            return await ctx.reply("π΅  λΈλκ° μ¬μλκ³  μμ§ μμ΅λλ€. (λΈλκ° μ¬μλλμ§ νμΈν΄μ£ΌμΈμ)", mention_author=False)

        if not 0 < offset < current.duration:
            return await ctx.reply(f"π΅  μ΅μ **0**λΆν° μ΅λ **{formatDuration(current.duration)}**κΉμ§ μλ ₯ν  μ μμ΅λλ€.", mention_author=False)

        await ctx.voice_client.seek(offset)
        await ctx.reply(f"πΆ  μ¬μ μ€μΈ μκ°μ **{formatDuration(offset)}**λ‘ κ±΄λλ°μμ΅λλ€.", mention_author=False)

def setup(client):
    client.add_cog(Seek(client))