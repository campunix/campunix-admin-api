"""create routine table

Revision ID: 7178cb2ef7df
Revises: 3f0606bd28f0
Create Date: 2025-03-26 23:12:13.794003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '7178cb2ef7df'
down_revision: Union[str, None] = '3f0606bd28f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.create_table(
        "routines",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("syllabus_id", sa.BigInteger, nullable=False),
        sa.Column("title", sa.String(length=255), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("calendar_year", sa.String(length=255), nullable=True),
        sa.Column("is_active", sa.Boolean, default=False, nullable=False),
        sa.Column("routine", JSONB, nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), onupdate=sa.text("NOW()"), nullable=True),
        sa.ForeignKeyConstraint(
            ["syllabus_id"], ["syllabuses.id"], ondelete="CASCADE"
        ),
    )


def downgrade() -> None:
    op.drop_table("routines")
