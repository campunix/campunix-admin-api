"""create student_courses table

Revision ID: 5573f3eae528
Revises: dbd5d6a3f028
Create Date: 2024-10-28 17:50:19.947912

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5573f3eae528"
down_revision: Union[str, None] = "dbd5d6a3f028"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "student_courses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("student_id", sa.BigInteger, nullable=False),
        sa.Column("course_id", sa.BigInteger, nullable=False),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("student_courses")
