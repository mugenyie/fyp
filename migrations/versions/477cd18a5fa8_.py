"""empty message

Revision ID: 477cd18a5fa8
Revises: 9b9e61cfeda4
Create Date: 2019-05-28 11:43:26.963431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477cd18a5fa8'
down_revision = '9b9e61cfeda4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('group_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'projects', 'groups', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.drop_column('projects', 'group_id')
    # ### end Alembic commands ###