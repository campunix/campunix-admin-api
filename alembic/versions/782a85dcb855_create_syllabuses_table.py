"""Create syllabuses table

Revision ID: 782a85dcb855
Revises: d47a1f328b68
Create Date: 2024-10-28 00:54:22.576838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '782a85dcb855'
down_revision: Union[str, None] = 'd47a1f328b68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "syllabuses",
        sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column("department_id", sa.BigInteger, nullable=False, unique=True),
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
