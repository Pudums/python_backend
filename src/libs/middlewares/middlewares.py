from fastapi import Request
import logging

logger = logging.getLogger(__name__)


class Content_type_logger:
    async def __call__(self, request: Request, call_next):
        content_type = request.headers.get('Content-Type')
        logger.info(str(content_type))

        response = await call_next(request)
        return response
