"""color table

Revision ID: 63b22a471d58
Revises: 
Create Date: 2019-12-06 10:48:38.520119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63b22a471d58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('r', sa.SmallInteger(), nullable=True),
    sa.Column('g', sa.SmallInteger(), nullable=True),
    sa.Column('b', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_color_name'), 'color', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_color_name'), table_name='color')
    op.drop_table('color')
    # ### end Alembic commands ###
