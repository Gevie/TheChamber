from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

import discord

from src.dtos import EmbedFieldDto


@dataclass
class BaseEmbed(ABC):
    title: str
    description: str
    fields: Optional[List[EmbedFieldDto]] = field(default_factory=list)
    color: discord.Color = discord.Color.default()

    @abstractmethod
    def get(self) -> discord.Embed:
        pass

    def _create(self) -> discord.Embed:
        embed = discord.Embed(
            title=self.title,
            description=self.description,
            color=self.color
        )

        for embed_field in self.fields:
            embed.add_field(
                name=embed_field.name,
                value=embed_field.value,
                inline=embed_field.inline
            )

        return embed

    @abstractmethod
    def _set_embed_fields(self) -> None:
        pass
