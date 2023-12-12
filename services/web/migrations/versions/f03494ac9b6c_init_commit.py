"""init commit

Revision ID: f03494ac9b6c
Revises: 
Create Date: 2023-12-12 01:44:30.971236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f03494ac9b6c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('passports',
    sa.Column('rp_number', sa.String(length=8), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=False),
    sa.Column('discord_tag', sa.String(length=128), nullable=False),
    sa.Column('issue_date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rp_number')
    )
    with op.batch_alter_table('passports', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_passports_nickname'), ['nickname'], unique=False)

    op.create_table('mariages',
    sa.Column('first_partner_id', sa.Integer(), nullable=False),
    sa.Column('second_partner_id', sa.Integer(), nullable=False),
    sa.Column('mariage_date', sa.DateTime(), nullable=False),
    sa.Column('divorce_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['first_partner_id'], ['passports.id'], ),
    sa.ForeignKeyConstraint(['second_partner_id'], ['passports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mariages')
    with op.batch_alter_table('passports', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_passports_nickname'))

    op.drop_table('passports')
    # ### end Alembic commands ###