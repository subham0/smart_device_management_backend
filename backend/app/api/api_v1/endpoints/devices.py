from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Device)
def create(
    *,
    db: Session = Depends(deps.get_db),
    device_in: schemas.DeviceCreate,
    # get_current_user: schemas.Device = Depends(deps.get_current_user)

):
    device = crud.device.create(db, obj_in=device_in)
    # call 
    return device

@router.put("/{id}", response_model=schemas.Device)
def update(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    device_in: schemas.DeviceCreate,
    # get_current_user: schemas.Device = Depends(deps.get_current_user)

):
    device = crud.device.update(db, obj_in=device_in, id=id)
    return device


@router.get("/{id}")
def get(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    start_date: datetime,
    end_date: datetime,
    # get_current_user: schemas.Device = Depends(deps.get_current_user)
):
    return crud.device.get(db, id=id, start_date=start_date, end_date=end_date)


@router.get("/get_room_devices/{room_id}")
def get_room_devices(
    room_id: int,
    db: Session = Depends(deps.get_db),
    # get_current_user: schemas.Device = Depends(deps.get_current_user)
):
    return crud.device.get_by_room_id(db, room_id=room_id)


# @router.get("/get_anamoly{device_id}")
# def send_anamoly_report(
#     *,
#     db: Session = Depends(deps.get_db),
#     device_id: int
# )

@router.get("/get_by_category/")
def get_room_devices(
    category_name: str,
    user_id: int,
    db: Session = Depends(deps.get_db),
    # get_current_user: schemas.Device = Depends(deps.get_current_user)
):
    return crud.device.get_by_category(category_name, user_id, db)
