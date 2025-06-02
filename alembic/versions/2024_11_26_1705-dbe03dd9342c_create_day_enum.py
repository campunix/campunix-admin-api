"""Create day enum

Revision ID: dbe03dd9342c
Revises: ba34d6df389d
Create Date: 2024-11-26 17:05:43.517701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbe03dd9342c'
down_revision: Union[str, None] = 'ba34d6df389d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE day AS ENUM ('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY');")

def downgrade() -> None:
    op.execute("DROP TYPE day;")
