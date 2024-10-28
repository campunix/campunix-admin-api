"""create staff_status enum type

Revision ID: 1826137946ce
Revises: 15168c165e36
Create Date: 2024-10-29 00:22:12.939457

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1826137946ce"
down_revision: Union[str, None] = "15168c165e36"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE staff_status AS ENUM ('ACTIVE', 'LEAVE', 'LPR', 'PRL', 'RETIRED');"
    )


def downgrade() -> None:
    op.execute("DROP TYPE staff_status;")
