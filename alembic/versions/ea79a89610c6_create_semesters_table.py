"""create semesters table

Revision ID: ea79a89610c6
Revises: 66a196d388e6
Create Date: 2024-10-28 15:54:23.120946

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ea79a89610c6"
down_revision: Union[str, None] = "66a196d388e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "semesters",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("year", sa.Integer, nullable=False),
        sa.Column("number", sa.Integer, nullable=False),
        sa.Column("department_id", sa.BigInteger, nullable=True),
        sa.ForeignKeyConstraint(
            ["department_id"], ["departments.id"], ondelete="CASCADE"
        ),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("semesters")
