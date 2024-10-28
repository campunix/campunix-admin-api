"""create teacher_status enum type

Revision ID: 35a43ddc85aa
Revises: a07f284ba527
Create Date: 2024-10-28 16:55:24.254035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35a43ddc85aa'
down_revision: Union[str, None] = 'a07f284ba527'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE teacher_status AS ENUM ('ACTIVE', 'LEAVE', 'LPR', 'PRL', 'RETIRED');")


def downgrade() -> None:
    op.execute("DROP TYPE teacher_status;")
