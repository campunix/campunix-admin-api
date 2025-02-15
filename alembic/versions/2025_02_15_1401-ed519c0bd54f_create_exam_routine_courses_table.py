"""create exam_routine_courses table

Revision ID: ed519c0bd54f
Revises: 506ad8c1ffcb
Create Date: 2025-02-15 14:01:06.655561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ed519c0bd54f'
down_revision: Union[str, None] = '506ad8c1ffcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "exam_routine_courses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )

def downgrade() -> None:
    op.drop_table("exam_routine_courses")
