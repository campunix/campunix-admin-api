"""create teacher_courses table

Revision ID: fe52becd5da1
Revises: e137b44f8044
Create Date: 2024-10-28 17:17:22.191290

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fe52becd5da1"
down_revision: Union[str, None] = "e137b44f8044"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "teacher_courses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("teacher_id", sa.BigInteger, nullable=False),
        sa.Column("course_id", sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(["teacher_id"], ["teachers.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("teacher_courses")
