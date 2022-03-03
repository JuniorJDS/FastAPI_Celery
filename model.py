from pydantic import BaseModel


class Order(BaseModel):
    customer_name: str
    order_quantity: int
