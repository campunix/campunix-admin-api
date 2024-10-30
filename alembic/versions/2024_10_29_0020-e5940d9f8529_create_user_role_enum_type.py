"""create user_role enum type

Revision ID: e5940d9f8529
Revises: 
Create Date: 2024-10-29 00:20:54.271231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5940d9f8529'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE user_role AS ENUM ('ADMIN', 'STAFF', 'TEACHER', 'STUDENT');")


def downgrade() -> None:
    op.execute("DROP TYPE user_role;")
