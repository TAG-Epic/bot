"""
MIT License
Copyright (c) 2019 GamingGeek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from discord.ext import commands
import datetime
import discord
import traceback


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        misc = self.bot.get_cog("Miscellaneous")
        await misc.loadutils()
        try:
            self.bot.load_extension("cogs.sk1erdiscord")
        except Exception:
            pass
        self.bot.logger.info("$GREEN-------------------------")
        self.bot.logger.info(f"$GREENBot: {self.bot.user}")
        self.bot.logger.info(f"$GREENID: {self.bot.user.id}")
        self.bot.logger.info(f"$GREENGuilds: {len(self.bot.guilds)}")
        self.bot.logger.info(f"$GREENUsers: {len(self.bot.users)}")
        self.bot.logger.info("$GREEN-------------------------")
        self.bot.logger.info(f"$BLUELOGGING START ON {datetime.datetime.utcnow()}")


def setup(bot):
    try:
        bot.add_cog(Ready(bot))
    except Exception as e:
        errortb = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        print(f'Error while adding cog "Ready";\n{errortb}')