import sqlalchemy as sa
from neneka.migrations import metadata


question = sa.Table(
    'question', metadata,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('name', sa.String(200), nullable=False),
)
