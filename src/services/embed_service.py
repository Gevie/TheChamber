from typing import Optional, List

import discord

class EmbedService:
    """Used to easily build discord embed objects from passed fields"""

    @staticmethod
    def create_embed(
        title: str,
        description: str,
        fields: Optional[List[dict]] = None,
        color: discord.Color = discord.Color.default(),
    ) -> discord.Embed:
        """
        Creates a new embed object from parameters

        Args:
            title (str): The title of the card
            description (str): The description of the card
            fields (Optional[List[dict]]): The fields to include in the card
            color (discord.Color): The color of the card

        Returns:
            discord.Embed: The embeddable card
        """

        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        if not fields:
            return embed

        for field in fields:
            embed.add_field(
                name=field.get('name', 'No name'),
                value=field.get('value', 'No value'),
                inline=field.get('inline', False)
            )

        return embed