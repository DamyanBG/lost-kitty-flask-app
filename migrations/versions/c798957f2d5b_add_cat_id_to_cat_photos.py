"""Add cat_id to cat_photos

Revision ID: c798957f2d5b
Revises: b429f600d0b2
Create Date: 2023-12-22 21:36:49.601694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c798957f2d5b'
down_revision = 'b429f600d0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat_photos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cat_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'cats', ['cat_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat_photos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cat_id')

    # ### end Alembic commands ###
