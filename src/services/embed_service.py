from typing import Optional, List

import discord

class EmbedService:
    @staticmethod
    def create_embed(
        title: str,
        description: str,
        fields: Optional[List[dict]] = None,
        color: discord.Color = discord.Color.default(),
    ) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        for field in fields:
            embed.add_field(
                name=field.get('name', 'No name'),
                value=field.get('value', 'No value'),
                inline=field.get('inline', False)
            )

        return embed