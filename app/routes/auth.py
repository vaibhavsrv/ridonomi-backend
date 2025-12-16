from fastapi import APIRouter

router = APIRouter()

@router.get("/heath")

def auth_health():
    return {"status": "auth ok"}