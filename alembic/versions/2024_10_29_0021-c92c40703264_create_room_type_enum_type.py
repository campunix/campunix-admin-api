"""create room_type enum type

Revision ID: c92c40703264
Revises: 955f70d7f2a6
Create Date: 2024-10-29 00:21:36.186927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c92c40703264'
down_revision: Union[str, None] = '955f70d7f2a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE room_type AS ENUM ('LECTURE', 'LAB', 'LIBRARY', 'SEMINAR', 'COMMON', 'OFFICE', 'DINING', 'OTHERS');")


def downgrade() -> None:
    op.execute("DROP TYPE room_type;")
