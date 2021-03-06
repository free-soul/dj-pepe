import discord.ext.commands as commands 

class Volume(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['vol', 'v'])
    async def volume(self, ctx, volume : int):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        if not 0 < volume < 101:
            return await ctx.reply("π΅  μ΅μ **1** λΆν° μ΅λ **100**κΉμ§λ§ λΆλ₯¨μ μ€μ ν  μ μμ΅λλ€.", mention_author=False)

        await ctx.voice_client.setVolume(volume / 100)
        return await ctx.reply(f"π  λΆλ₯¨μ **{volume}%**λ‘ μ€μ νμ΅λλ€.", mention_author=False)

def setup(client):
    client.add_cog(Volume(client))