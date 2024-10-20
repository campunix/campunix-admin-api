"""create user table

Revision ID: ca222d31ddac
Revises: e2bba2faede3
Create Date: 2024-10-21 00:06:42.199055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca222d31ddac'
down_revision: Union[str, None] = 'e2bba2faede3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(length=255), nullable=False, unique=True),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('disabled', sa.Boolean, default=False),
    )

def downgrade():
    op.drop_table('user')