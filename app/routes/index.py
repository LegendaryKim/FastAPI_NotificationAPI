from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    """
    ELB status checking API
    :return:
    """
    # # Original way
    # # user = Users(status='active', name="Hwanpyo")
    # # session.add(user)
    # # session.commit()
    #
    # # Editor's
    # Users().create(session, auto_commit=True, name="Hwanpyo")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
