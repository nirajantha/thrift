"""goods table

Revision ID: b655c7127177
Revises: 518605001046
Create Date: 2022-04-20 21:05:12.155869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b655c7127177'
down_revision = '518605001046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goods', 'price')
    # ### end Alembic commands ###
