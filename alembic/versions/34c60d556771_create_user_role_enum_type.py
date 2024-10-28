"""create user_role enum type

Revision ID: 34c60d556771
Revises: d5ebd0f8435a
Create Date: 2024-10-28 14:47:28.518130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34c60d556771'
down_revision: Union[str, None] = 'd5ebd0f8435a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE user_role AS ENUM ('ADMIN', 'STAFF', 'TEACHER', 'STUDENT');")


def downgrade() -> None:
    op.execute("DROP TYPE user_role;")
