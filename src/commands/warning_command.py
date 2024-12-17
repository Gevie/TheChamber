from discord.app_commands.checks import has_permissions
from discord.ext import commands

from src.commands import BaseCommand
from src.services import WarningService

class WarningCommand(BaseCommand):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
        self.warning_service = WarningService()

    @commands.command(name='warn')
    @has_permissions(administrator=True)
    async def warn(self, ctx, user: commands.MemberConverter, reason:str) -> None:
        warn_issuer = ctx.message.author

        warning = self.warning_service.warn(user, warn_issuer, reason)

        