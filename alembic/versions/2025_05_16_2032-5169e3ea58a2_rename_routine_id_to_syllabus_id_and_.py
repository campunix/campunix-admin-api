"""Rename routine_id to syllabus_id and update FK

Revision ID: 5169e3ea58a2
Revises: 0dcbdffec311
Create Date: 2025-05-16 20:32:39.212910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5169e3ea58a2'
down_revision: Union[str, None] = '0dcbdffec311'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_constraint('exam_routines_routine_id_fkey', 'exam_routines', type_='foreignkey')

    op.alter_column('exam_routines', 'routine_id', new_column_name='syllabus_id')

    op.create_foreign_key(
        'exam_routines_syllabus_id_fkey',
        'exam_routines',
        'syllabuses',
        ['syllabus_id'],
        ['id'],
        ondelete='CASCADE'
    )


def downgrade():
    op.drop_constraint('exam_routines_syllabus_id_fkey', 'exam_routines', type_='foreignkey')

    op.alter_column('exam_routines', 'syllabus_id', new_column_name='routine_id')

    op.create_foreign_key(
        'exam_routines_routine_id_fkey',
        'exam_routines', 'routines',
        ['routine_id'], ['id'],
        ondelete='CASCADE'
    )
