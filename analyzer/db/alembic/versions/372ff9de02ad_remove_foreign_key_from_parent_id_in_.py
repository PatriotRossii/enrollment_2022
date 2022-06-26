"""Remove foreign key from parent_id in shop_units

Revision ID: 372ff9de02ad
Revises: 4b1034d5040c
Create Date: 2022-06-25 18:03:38.949360

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "372ff9de02ad"
down_revision = "4b1034d5040c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk__shop_units__parent_id__shop_units", "shop_units", type_="foreignkey")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        "fk__shop_units__parent_id__shop_units", "shop_units", "shop_units", ["parent_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###
