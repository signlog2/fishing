"""empty message

Revision ID: ea926ff31c41
Revises: 1dc584803940
Create Date: 2022-02-01 15:49:48.858381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea926ff31c41'
down_revision = '1dc584803940'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=False))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(), nullable=False))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
