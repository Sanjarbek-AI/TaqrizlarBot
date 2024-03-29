"""empty message

Revision ID: cc4b50fd9528
Revises: 
Create Date: 2022-10-25 10:15:54.217496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc4b50fd9528'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('full_address', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('active', 'inactive', name='userstatus'), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='usergender'), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
