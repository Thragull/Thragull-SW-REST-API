"""empty message

Revision ID: a5708c49865d
Revises: 123524dab705
Create Date: 2024-03-29 17:46:41.960491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5708c49865d'
down_revision = '123524dab705'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourite_characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    with op.batch_alter_table('favourite_planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    with op.batch_alter_table('favourite_starships', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    with op.batch_alter_table('starship_crew', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starship_crew', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    with op.batch_alter_table('favourite_starships', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    with op.batch_alter_table('favourite_planets', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    with op.batch_alter_table('favourite_characters', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###