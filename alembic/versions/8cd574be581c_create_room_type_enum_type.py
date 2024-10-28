"""create room_type enum type

Revision ID: 8cd574be581c
Revises: 452195b50ff0
Create Date: 2024-10-28 16:20:02.969834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cd574be581c'
down_revision: Union[str, None] = '452195b50ff0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE room_type AS ENUM ('LECTURE', 'LAB', 'LIBRARY', 'SEMINAR', 'COMMON', 'OFFICE', 'DINING', 'OTHERS');")


def downgrade() -> None:
    op.execute("DROP TYPE room_type;")
