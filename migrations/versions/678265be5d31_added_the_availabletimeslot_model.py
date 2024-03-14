"""Added the AvailableTimeSlot model

Revision ID: 678265be5d31
Revises: c9173002629e
Create Date: 2024-03-10 00:13:16.846250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '678265be5d31'
down_revision = 'c9173002629e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('available_time_slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('time_slot', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('available_time_slot')
    # ### end Alembic commands ###
