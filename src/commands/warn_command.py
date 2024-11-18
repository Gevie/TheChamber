from discord.app_commands.checks import has_permissions
from discord.ext import commands

from src.commands import BaseCommand
from src.services import WarnService

class WarnCommand(BaseCommand):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
        self.warn_service = WarnService()

    @commands.command(name='warn')
    @has_permissions(administrator=True)
    async def warn(self, ctx, user: commands.MemberConverter, *, reason:str) -> None:
        warn_issuer = ctx.message.author
        tagged_user = user

        warning_id = self.warn_service.log(tagged_user, warn_issuer, reason)

        