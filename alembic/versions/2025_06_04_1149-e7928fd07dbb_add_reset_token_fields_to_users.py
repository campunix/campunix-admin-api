"""add reset_token fields to users

Revision ID: e7928fd07dbb
Revises: cd26923dbddb
Create Date: 2025-06-04 11:49:37.739947
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7928fd07dbb'
down_revision: Union[str, None] = 'cd26923dbddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('reset_token', sa.String(), nullable=True))
    op.add_column('users', sa.Column('reset_token_expiry', sa.DateTime(), nullable=True))
    op.create_index('ix_users_reset_token', 'users', ['reset_token'])


def downgrade() -> None:
    op.drop_index('ix_users_reset_token', table_name='users')
    op.drop_column('users', 'reset_token_expiry')
    op.drop_column('users', 'reset_token')
