"""category_type

Revision ID: 6ba7788a95f9
Revises: 23f0f0cfd247
Create Date: 2024-02-19 22:25:57.952932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ba7788a95f9'
down_revision: Union[str, None] = '23f0f0cfd247'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Categories', sa.Column('type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Categories', 'type')
    # ### end Alembic commands ###