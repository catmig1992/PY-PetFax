"""empty message

Revision ID: a728aaada7c3
Revises: effb1094e5df
Create Date: 2023-03-09 20:44:54.961535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a728aaada7c3'
down_revision = 'effb1094e5df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('pet_id', sa.Integer(), nullable=False),
    sa.Column('pet_name', sa.String(length=250), nullable=True),
    sa.Column('pet_photo', sa.String(length=500), nullable=True),
    sa.Column('pet_fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('pet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###