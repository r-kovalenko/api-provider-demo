from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Provider Demo", version="0.1.0")
v1 = FastAPI(title="Customer API", version="1.0.0")
v2 = FastAPI(title="Customer API", version="2.0.0")


class CustomerV1(BaseModel):
    id: int
    name: str


class CustomerV2(BaseModel):
    id: int
    full_name: str


def check_customer(customer_id: int) -> None:
    if customer_id != 1:
        raise HTTPException(status_code=404, detail="Customer not found")


@v1.get("/customers/{customer_id}", response_model=CustomerV1)
def get_customer_v1(customer_id: int) -> CustomerV1:
    check_customer(customer_id)
    return CustomerV1(id=customer_id, name="Demo Customer")


@v2.get("/customers/{customer_id}", response_model=CustomerV2)
def get_customer_v2(customer_id: int) -> CustomerV2:
    check_customer(customer_id)
    return CustomerV2(id=customer_id, full_name="Demo Customer")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.mount("/v1", v1)
app.mount("/v2", v2)
