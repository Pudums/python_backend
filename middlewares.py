from fastapi import Request
import logging


class ContentTypeLogger:
    async def __call__(self, request: Request, call_next):
        content_type = request.headers.get('Content-Type')
        logging.Info(content_type)

        response = await call_next(request)
        return response
