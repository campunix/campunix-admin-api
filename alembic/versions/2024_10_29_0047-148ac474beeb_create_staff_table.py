"""create staff table

Revision ID: 148ac474beeb
Revises: 18e077f85792
Create Date: 2024-10-29 00:47:41.277412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '148ac474beeb'
down_revision: Union[str, None] = '18e077f85792'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "staff",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger, nullable=False),
        sa.Column("designation", postgresql.ENUM(name='staff_designation', create_type=False), nullable=False),
        sa.Column("status", postgresql.ENUM(name='staff_status', create_type=False), nullable=False),
        sa.Column("department_id", sa.BigInteger, nullable=True),
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
    op.drop_table("staff")