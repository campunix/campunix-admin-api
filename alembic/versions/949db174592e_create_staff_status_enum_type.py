"""create staff_status enum type

Revision ID: 949db174592e
Revises: 64de9738ce39
Create Date: 2024-10-28 17:36:56.449381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '949db174592e'
down_revision: Union[str, None] = '64de9738ce39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE staff_status AS ENUM ('ACTIVE', 'LEAVE', 'LPR', 'PRL', 'RETIRED');")


def downgrade() -> None:
    op.execute("DROP TYPE staff_status;")
