from sqlalchemy.orm import Session

from app.database.conn import Base


async def create(session: Session, obj: Base, auto_commit=False, **kwargs):
    """
    Table Data Loading function
    :param session:
    :param obj: Table Model instance
    :param auto_commit:
    :param kwargs: Loading data
    :return:
    """
    for col in obj.all_colomns():
        col_name = col.name
        if col_name in kwargs:
            setattr(obj, col_name, kwargs.get(col_name))
    session.add(obj)
    session.flush()
    if auto_commit:
        session.commit()
    return obj
