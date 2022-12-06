from typing import TYPE_CHECKING
import schemas
from fastapi_sqlalchemy import db

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def create_user(user: schemas.User) -> schemas.User:
    with db():
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
    return schemas.User.from_orm(user)
