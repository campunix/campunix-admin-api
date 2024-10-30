"""create teacher_designation enum type

Revision ID: ed696a6b1f2c
Revises: 1826137946ce
Create Date: 2024-10-29 00:22:24.620475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed696a6b1f2c'
down_revision: Union[str, None] = '1826137946ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE teacher_designation AS ENUM ('PROFESSOR', 'ASSOCIATE_PROFESSOR', 'ASSISTANT_PROFESSOR', 'LECTURER');"
    )


def downgrade() -> None:
    op.execute("DROP TYPE teacher_designation;")
