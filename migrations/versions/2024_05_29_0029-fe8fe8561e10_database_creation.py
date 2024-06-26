"""Database creation

Revision ID: fe8fe8561e10
Revises: 
Create Date: 2024-05-29 00:29:02.956335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe8fe8561e10'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('creation_time', sa.TIMESTAMP(), nullable=True),
            sa.Column('change_time', sa.TIMESTAMP(), nullable=True),
            sa.Column('status', sa.String(), nullable=True),
            sa.Column('side', sa.String(), nullable=True),
            sa.Column('price', sa.Integer(), nullable=True),
            sa.Column('amount', sa.Integer(), nullable=True),
            sa.Column('instrument', sa.String(), nullable=True),
            sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application')
    # ### end Alembic commands ###
