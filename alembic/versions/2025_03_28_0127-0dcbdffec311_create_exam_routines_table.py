"""Create exam_routines table

Revision ID: 0dcbdffec311
Revises: 5f1a0abeacdf
Create Date: 2025-03-28 01:27:25.852318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '0dcbdffec311'
down_revision: Union[str, None] = '5f1a0abeacdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "exam_routines",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("routine_id", sa.BigInteger, nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("calendar_year", sa.String(length=255), nullable=True),
        sa.Column("is_active", sa.Boolean, default=False, nullable=False),
        sa.Column("exam_routine", JSONB, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["routine_id"], ["routines.id"], ondelete="CASCADE"
        ),
    )


def downgrade() -> None:
    op.drop_table("exam_routines")
