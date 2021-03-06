"""Initial Migration

Revision ID: 6bbccadcecc9
Revises: 9cb5dbc4ebf8
Create Date: 2018-09-03 06:21:45.022973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bbccadcecc9'
down_revision = '9cb5dbc4ebf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
