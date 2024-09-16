"""empty message

Revision ID: a7dc6e42fead
Revises: a5cffa318ac2
Create Date: 2024-09-16 21:32:44.667628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7dc6e42fead'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('excuse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_excuse', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('excuse')
    # ### end Alembic commands ###
