"""make_preference_day_slot_nullable

Revision ID: cd26923dbddb
Revises: 5169e3ea58a2
Create Date: 2025-05-28 10:43:36.164592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd26923dbddb'
down_revision: Union[str, None] = '5169e3ea58a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'preferences', 'day',
        existing_type=sa.Enum(name='day'),
        nullable=True
    )
    op.alter_column(
        'preferences', 'slot_no',
        existing_type=sa.BigInteger(),
        nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        'preferences', 'day',
        existing_type=sa.Enum(name='day'),
        nullable=False
    )
    op.alter_column(
        'preferences', 'slot_no',
        existing_type=sa.BigInteger(),
        nullable=False
    )
