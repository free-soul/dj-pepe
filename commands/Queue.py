import discord.ext.commands as commands 
import math

from classes.FormatDuration import formatDuration

class Queue(commands.Cog):

    def __init__(self, client) -> None:
        super().__init__()

        self.client = client
        self.audio = client.Audio

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page: int = 1):

        if not ctx.author.voice:
            return await ctx.reply("π΅  μμ± μ±λμ λ€μ΄κ° μνμμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ.", mention_author=False)

        if not ctx.voice_client:
            return await ctx.reply("π΅  μμ± μ±λμ λ΄μ΄ λ€μ΄μλμ§ νμΈν΄μ£ΌμΈμ.", mention_author=False)

        queues = ctx.voice_client.Queue
        maxpages = math.ceil(len(queues) / 10)

        if int(len(queues)) <= 0:
            return await ctx.reply("π΅  λκΈ° μ€μΈ μ¬μ λͺ©λ‘μ΄ λΉμ΄μμ΅λλ€.", mention_author=False)

        if int(page) > int(maxpages) or int(page) <= 0:
            return await ctx.reply("π΅  **0**νμ΄μ§λ³΄λ€ μκ±°λ λλ **{}**νμ΄μ§λ³΄λ€ ν°μ§ νμΈν΄μ£ΌμΈμ.".format(maxpages), mention_author=False)

        execute = (page - 1) * 10
        maxexecute = execute + 9

        queue_titles = ""
        for number in range(execute, maxexecute + 1):
            if int(number) < int(len(queues)):
                queue_titles += "**#{0}** {1} (`{2}`)\n".format(number + 1, queues[number].title, formatDuration(queues[number].duration))
                
        return await ctx.reply("`πΏ λ€μ λΈλμμ μ¬μλ  λͺ©λ‘μ λΆλ¬μμ΅λλ€. ({0}νμ΄μ§ μ€ {1}νμ΄μ§λ₯Ό λ‘λν¨)`\n{2}".format(maxpages, page, queue_titles), mention_author=False)

def setup(client):
    client.add_cog(Queue(client))