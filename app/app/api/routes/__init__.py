from fastapi import APIRouter
from app.api.controllers import auth, ancestor_data, match, application, genealogy, chat, activity, culture

api_router = APIRouter(prefix="/api")

api_router.include_router(auth.router)
api_router.include_router(ancestor_data.router)
api_router.include_router(match.router)
api_router.include_router(application.router)
api_router.include_router(genealogy.router)
api_router.include_router(chat.router)
api_router.include_router(activity.router)
api_router.include_router(culture.router)
