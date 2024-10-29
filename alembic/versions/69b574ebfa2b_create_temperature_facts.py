"""create temperature_facts

Revision ID: 69b574ebfa2b
Revises: 
Create Date: 2024-10-29 21:00:43.515550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision: str = '69b574ebfa2b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'temperature_facts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('min_temperature', sa.Float, nullable=False),
        sa.Column('max_temperature', sa.Float, nullable=False),
        sa.Column('fact', sa.Text, nullable=False),
        sa.Column('created', sa.TIMESTAMP, server_default=func.now(), nullable=False),
        sa.Column('updated', sa.TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('temperature_facts')
