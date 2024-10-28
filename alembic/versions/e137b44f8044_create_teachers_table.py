"""create teachers table

Revision ID: e137b44f8044
Revises: 6272a9fe6937
Create Date: 2024-10-28 17:03:53.823902

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e137b44f8044"
down_revision: Union[str, None] = "6272a9fe6937"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "teachers",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.BigInteger, nullable=False),
        sa.Column("designation", sa.Enum(name="teacher_designation"), nullable=False),
        sa.Column("status", sa.Enum(name="teacher_status"), nullable=False),
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
