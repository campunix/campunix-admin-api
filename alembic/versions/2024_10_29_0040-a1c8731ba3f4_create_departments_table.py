"""create departments table

Revision ID: a1c8731ba3f4
Revises: 020b0bae7bf4
Create Date: 2024-10-29 00:40:04.775082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1c8731ba3f4'
down_revision: Union[str, None] = '020b0bae7bf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=255), nullable=False, unique=True),
        sa.Column("admin_group", sa.BigInteger, nullable=False),
        sa.Column("created_by", sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(["admin_group"], ["admin_groups.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("departments")
