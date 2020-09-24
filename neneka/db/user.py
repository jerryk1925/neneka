import sqlalchemy as sa
from neneka.migrations import metadata


users = sa.Table(
    'users', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(60), nullable=False),
    sa.Column('password_hash', sa.String(128), nullable=False)
)

