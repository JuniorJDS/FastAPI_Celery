#import celery
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery_worker import create_order, celery
#from celery.result import AsyncResult
from model import Order


app = FastAPI()


@app.post('/order')
def add_order(order: Order):

    # use delay() method to call the celery task
    task = create_order.delay(order.customer_name, order.order_quantity)

    return {"task_id": task.id, "message": "Order Received! Thank you for your patience."}


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = celery.AsyncResult(task_id)

    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)

from sse_starlette.sse import EventSourceResponse

@app.get("/status/stream/{task_id}")
def get_status_stream(task_id):
    task_result = celery.AsyncResult(task_id)

    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return EventSourceResponse(task_result) #JSONResponse(result)
