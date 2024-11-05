"""create teacher_courses table

Revision ID: 18e077f85792
Revises: 325dafef86a1
Create Date: 2024-10-29 00:46:54.974573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18e077f85792'
down_revision: Union[str, None] = '325dafef86a1'
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
        # Adding a unique constraint on teacher_id and course_id
        sa.UniqueConstraint("teacher_id", "course_id", name="uq_teacher_course")
    )


def downgrade() -> None:
    op.drop_constraint('uq_teacher_course', 'teacher_courses', type_='unique')
    op.drop_table("teacher_courses")
