"""create staff_designation enum type

Revision ID: 64de9738ce39
Revises: fe52becd5da1
Create Date: 2024-10-28 17:33:55.809943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64de9738ce39'
down_revision: Union[str, None] = 'fe52becd5da1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE staff_designation AS ENUM ('OFFICER', 'ASSISTANT_OFFICER', 'ACCOUNTANT', 'LIBRARIAN');"
    )


def downgrade() -> None:
    op.execute("DROP TYPE staff_designation;")
