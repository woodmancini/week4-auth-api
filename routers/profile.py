from fastapi import APIRouter, Depends

import models
from security import get_current_user

router = APIRouter()

@router.get("/me")
def get_profile(current_user: models.User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    } 