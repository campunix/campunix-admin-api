"""create teacher_status enum type

Revision ID: 15168c165e36
Revises: c92c40703264
Create Date: 2024-10-29 00:21:57.841048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15168c165e36'
down_revision: Union[str, None] = 'c92c40703264'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE teacher_status AS ENUM ('ACTIVE', 'LEAVE', 'LPR', 'PRL', 'RETIRED');")


def downgrade() -> None:
    op.execute("DROP TYPE teacher_status;")
