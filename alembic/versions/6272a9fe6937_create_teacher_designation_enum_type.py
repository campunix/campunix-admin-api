"""create teacher_designation enum type

Revision ID: 6272a9fe6937
Revises: 35a43ddc85aa
Create Date: 2024-10-28 17:00:14.001725

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6272a9fe6937"
down_revision: Union[str, None] = "35a43ddc85aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE TYPE teachers_designation AS ENUM ('PROFESSOR', 'ASSOCIATE_PROFESSOR', 'ASSISTANT_PROFESSOR', 'LECTURER');"
    )


def downgrade() -> None:
    op.execute("DROP TYPE teachers_designation;")
