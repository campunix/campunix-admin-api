"""create course_type enum type

Revision ID: 955f70d7f2a6
Revises: e5940d9f8529
Create Date: 2024-10-29 00:21:24.824673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '955f70d7f2a6'
down_revision: Union[str, None] = 'e5940d9f8529'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE course_type AS ENUM ('THEORY', 'LAB', 'RESEARCH', 'VIVA');")


def downgrade() -> None:
    op.execute("DROP TYPE course_type;")