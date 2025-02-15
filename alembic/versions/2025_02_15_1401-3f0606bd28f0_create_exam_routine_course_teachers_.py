"""create exam_routine_course_teachers table

Revision ID: 3f0606bd28f0
Revises: ed519c0bd54f
Create Date: 2025-02-15 14:01:46.998182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f0606bd28f0'
down_revision: Union[str, None] = 'ed519c0bd54f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "exam_routine_course_teachers",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("exam_routine_course_id", sa.BigInteger, nullable=False),
        sa.Column("teacher_id", sa.BigInteger, nullable=False),
        sa.Column("is_chief", sa.Boolean),
        sa.ForeignKeyConstraint(["exam_routine_course_id"], ["exam_routine_courses.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["teacher_id"], ["teachers.id"], ondelete="CASCADE"),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("exam_routine_course_teachers")
