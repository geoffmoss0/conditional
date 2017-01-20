"""empty message

Revision ID: 65943c537c84
Revises: 983d69afb7f8
Create Date: 2016-12-18 15:16:12.922122

"""

# revision identifiers, used by Alembic.
revision = '65943c537c84'
down_revision = '983d69afb7f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('in_housing_queue',
    sa.Column('uid', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('in_housing_queue')
    ### end Alembic commands ###
