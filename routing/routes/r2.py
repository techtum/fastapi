from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get():
    return {'msg': 'This is route #2.'}
