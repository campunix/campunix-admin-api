"""create course_type enum type

Revision ID: 003e724152eb
Revises: ea79a89610c6
Create Date: 2024-10-28 15:57:50.238109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '003e724152eb'
down_revision: Union[str, None] = 'ea79a89610c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE course_type AS ENUM ('THEORY', 'LAB', 'RESEARCH', 'VIVA');")


def downgrade() -> None:
    op.execute("DROP TYPE course_type;")
