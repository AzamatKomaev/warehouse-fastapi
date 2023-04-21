from sqlalchemy import Column as DefaultColumn


def Column(*args, **kwargs):
    """Custom Column with nullable=False by default."""
    if not kwargs.get('nullable'):
        kwargs.setdefault('nullable', False)
    return DefaultColumn(*args, **kwargs)
