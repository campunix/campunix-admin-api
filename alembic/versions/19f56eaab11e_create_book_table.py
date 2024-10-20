"""create book table

Revision ID: 19f56eaab11e
Revises: bd4b8b49093d
Create Date: 2024-10-20 23:50:44.676327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f56eaab11e'
down_revision: Union[str, None] = 'bd4b8b49093d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), sa.Identity(always=False), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("author", sa.String(), nullable=False),
        sa.Column("publication_year", sa.Integer(), nullable=False),
        sa.Column("summary", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("book_pkey")),
    )

    op.execute("ALTER TABLE books ADD COLUMN search_vector tsvector GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || author)) STORED;")

    op.execute("CREATE INDEX search_vector_idx ON books USING GIN (search_vector);")

def downgrade() -> None:
    op.drop_table("books")
