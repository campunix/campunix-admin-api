"""create teachers table

Revision ID: 325dafef86a1
Revises: bba5a332bf7f
Create Date: 2024-10-29 00:44:04.783078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '325dafef86a1'
down_revision: Union[str, None] = 'bba5a332bf7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "teachers",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger, nullable=False, unique=True),
        sa.Column("designation", postgresql.ENUM(name='teacher_designation', create_type=False), nullable=False),
        sa.Column("status", postgresql.ENUM(name='teacher_status', create_type=False), nullable=False),
        sa.Column("department_id", sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["department_id"], ["departments.id"], ondelete="CASCADE"
        ),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("teachers")
