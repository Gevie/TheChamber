from dataclasses import dataclass


@dataclass
class EmbedFieldDto:
    name: str
    value: str
    inline: bool = False