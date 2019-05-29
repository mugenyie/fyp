"""empty message

Revision ID: 5def51842e7f
Revises: c33e63aab9cf
Create Date: 2019-05-29 04:25:41.572568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5def51842e7f'
down_revision = 'c33e63aab9cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('created_by', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'created_by')
    # ### end Alembic commands ###