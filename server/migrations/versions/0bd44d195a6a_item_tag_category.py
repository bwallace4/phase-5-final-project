"""<item,tag,category >

Revision ID: 0bd44d195a6a
Revises: a55be58d296a
Create Date: 2023-10-02 03:44:49.053046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bd44d195a6a'
down_revision = 'a55be58d296a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_category',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name=op.f('fk_item_category_category_id_category')),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], name=op.f('fk_item_category_item_id_item')),
    sa.PrimaryKeyConstraint('item_id', 'category_id')
    )
    op.create_table('item_tag',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], name=op.f('fk_item_tag_item_id_item')),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name=op.f('fk_item_tag_tag_id_tag')),
    sa.PrimaryKeyConstraint('item_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_tag')
    op.drop_table('item_category')
    op.drop_table('tag')
    op.drop_table('category')
    # ### end Alembic commands ###