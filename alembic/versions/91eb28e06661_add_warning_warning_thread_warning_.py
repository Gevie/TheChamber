"""Add warning, warning_thread, warning_reason, ban, guild, user model tables.

Revision ID: 91eb28e06661
Revises: 69b574ebfa2b
Create Date: 2024-11-18 11:25:57.349601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '91eb28e06661'
down_revision: Union[str, None] = '69b574ebfa2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('guilds',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('discord_id', sa.String(), nullable=False),
        sa.Column('warning_channel_id', sa.String(), nullable=False),
        sa.Column('warning_forum_id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('discord_id')
    )
    op.create_table('warning_reasons',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('description')
    )
    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('discord_id', sa.String(), nullable=False),
        sa.Column('guild_id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('discriminator', sa.String(), nullable=False),
        sa.Column('nickname', sa.String(), nullable=True),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['guild_id'], ['guilds.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('discord_id')
    )
    op.create_table('bans',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warning_threads',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('thread_id', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('thread_id')
    )
    op.create_table('warnings',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('issuer_id', sa.Integer(), nullable=False),
        sa.Column('reason_id', sa.Integer(), nullable=True),
        sa.Column('thread_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('reason_text', sa.String(), nullable=True),
        sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['issuer_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['reason_id'], ['warning_reasons.id'], ),
        sa.ForeignKeyConstraint(['thread_id'], ['warning_threads.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('warnings')
    op.drop_table('warning_threads')
    op.drop_table('bans')
    op.drop_table('users')
    op.drop_table('warning_reasons')
    op.drop_table('guilds')
