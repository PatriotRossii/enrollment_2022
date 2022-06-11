"""Initial

Revision ID: 883c53b19249
Revises: 
Create Date: 2022-06-11 13:57:49.533445

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "883c53b19249"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "price_updates",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("unit_id", sa.Integer(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["unit_id"],
            ["price_updates.id"],
            name=op.f("fk__price_updates__unit_id__price_updates"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__price_updates")),
    )
    op.create_index(op.f("ix__price_updates__id"), "price_updates", ["id"], unique=False)
    op.create_table(
        "shop_units",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column("is_category", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"], ["shop_units.id"], name=op.f("fk__shop_units__parent__shop_units"), ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__shop_units")),
    )
    op.create_index(op.f("ix__shop_units__id"), "shop_units", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix__shop_units__id"), table_name="shop_units")
    op.drop_table("shop_units")
    op.drop_index(op.f("ix__price_updates__id"), table_name="price_updates")
    op.drop_table("price_updates")
    # ### end Alembic commands ###
