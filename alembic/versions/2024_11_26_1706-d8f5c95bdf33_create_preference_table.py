"""Create preference  table

Revision ID: d8f5c95bdf33
Revises: dbe03dd9342c
Create Date: 2024-11-26 17:06:04.481253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd8f5c95bdf33'
down_revision: Union[str, None] = 'dbe03dd9342c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "preferences",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("teacher_id", sa.BigInteger, nullable=False),
        sa.Column("day", postgresql.ENUM(name='day', create_type=False), nullable=False),
        sa.Column("slot_no", sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(["teacher_id"], ["teachers.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        # Adding a unique constraint on teacher_id and course_id
        sa.UniqueConstraint("teacher_id", "day", "slot_no", name="uq_preferences")
    )


def downgrade() -> None:
    op.drop_table("preferences")
