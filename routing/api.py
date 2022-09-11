from fastapi import APIRouter
from routes import welcome

# new routes
from routes import r1
from routes import r2

router = APIRouter()

router.include_router(welcome.router,prefix='',tags=['welcome'])

# new routes
router.include_router(r1.router,prefix='/r1',tags=['route1'])
router.include_router(r2.router,prefix='/r2',tags=['route2'])
