
class Order(BaseModel):
    order_id: int
    order_name: str
    delivery_add: str
    datetime: str
    order_type: str
    status: str
    payment_method: str
    price: str
    tax: str
    total: str
