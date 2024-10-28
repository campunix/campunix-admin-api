"""create courses table

Revision ID: 452195b50ff0
Revises: 003e724152eb
Create Date: 2024-10-28 16:12:17.203133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '452195b50ff0'
down_revision: Union[str, None] = '003e724152eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=255), nullable=False, unique=True),
        sa.Column("department_id", sa.BigInteger, nullable=False),
        sa.Column("type", sa.Enum(name="course_type"), nullable=False),
        sa.ForeignKeyConstraint(["department_id"], ["departemnts.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("courses")
