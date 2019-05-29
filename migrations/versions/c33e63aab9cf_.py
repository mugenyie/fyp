"""empty message

Revision ID: c33e63aab9cf
Revises: dc125809ef9c
Create Date: 2019-05-29 03:10:14.631405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c33e63aab9cf'
down_revision = 'dc125809ef9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projectslog_project_id_fkey', 'projectslog', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('projectslog_project_id_fkey', 'projectslog', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###