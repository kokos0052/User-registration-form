import json
import os
from typing import TYPE_CHECKING

import pika
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

import models
from services import create_user
from db import DATABASE_PARAMS

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = FastAPI()



app.add_middleware(DBSessionMiddleware, **DATABASE_PARAMS)


def handle_message(ch, method, properties, body):
    user_data = json.loads(body)
    user_instance = models.User(**user_data)
    create_user(user=user_instance)


@app.on_event('startup')
async def startup_event():
    connection_parameters = pika.ConnectionParameters(os.environ.get('queue_host'), os.environ.get('queue_port'))
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue='queue')
    channel.basic_consume(on_message_callback=handle_message,
                          queue='queue', auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=os.environ.get('port'))
