"""create roles table

Revision ID: d47a1f328b68
Revises: 2e50b9f1ffa3
Create Date: 2024-10-24 23:53:34.959170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd47a1f328b68'
down_revision: Union[str, None] = '2e50b9f1ffa3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(length=255), nullable=False, unique=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("roles")
