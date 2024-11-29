"""create syllabus table

Revision ID: ba34d6df389d
Revises: 38aff3239c4c
Create Date: 2024-10-30 23:11:07.569695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = 'ba34d6df389d'
down_revision: Union[str, None] = '38aff3239c4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "syllabuses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("department_id", sa.BigInteger, nullable=False),
        sa.Column("syllabus", JSONB, nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), onupdate=sa.text("NOW()"), nullable=True),
    )

    op.create_index(
        'ix_syllabus',
        'syllabuses',
        ['syllabus'],
        postgresql_using='gin',
        postgresql_ops={'syllabus': 'jsonb_ops'}
    )


def downgrade() -> None:
    op.drop_index('ix_syllabus', table_name='syllabuses')
    op.drop_table("syllabuses")
