"""create staff_designation enum type

Revision ID: f17cb9d56eed
Revises: ed696a6b1f2c
Create Date: 2024-10-29 00:22:34.900232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f17cb9d56eed'
down_revision: Union[str, None] = 'ed696a6b1f2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE staff_designation AS ENUM ('OFFICER', 'ASSISTANT_OFFICER', 'ACCOUNTANT', 'LIBRARIAN');"
    )


def downgrade() -> None:
    op.execute("DROP TYPE staff_designation;")
