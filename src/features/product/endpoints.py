from typing import Dict, List
from datetime import datetime
from fastapi import APIRouter, Request, Response

from features.product.schemas.schema import ENGINE
from features.product.usecase import ProductUsecase
from features.product.models.error_model import ErrorModel
from features.product.models.product_model import (
    ProductModel,
    ProductCreateModel,
)  # noqa: E501


# api router
product_router = APIRouter()
# product usecase
product_usecase = ProductUsecase(ENGINE)


@product_router.get("/api/products/health")
def health_check(_: Request) -> Dict:
    return {
        "status": "healthy",
        "path": "/api/products",
        "timestamp": datetime.now(),
    }


@product_router.get(
    "/api/products",
    response_model=List[ProductModel],
)
def get_all_products() -> List[ProductModel]:
    # get all products and return
    return product_usecase.get_all_products()


@product_router.post(
    path="/api/products/{product_id}",
    response_model=ProductModel | ErrorModel,
    # for OpenAPI documentation
    responses={
        200: {"model": ProductModel},
        400: {"model": ErrorModel},
    },
)
def get_single_product(
    response: Response,
    product_id: int,
) -> ProductModel | ErrorModel:
    # get single product
    product = product_usecase.get_product_with_id(product_id)

    # if product is None
    if product is None:
        # bad request
        response.status_code = 400
        return ErrorModel(message=f"invalid product_id: {product_id}")

    # otherwise return product
    return product


@product_router.post("/api/products", response_model=ProductModel)
def add_products(
    response: Response,
    model: ProductCreateModel,
) -> ProductModel:
    # add & return new product
    response.status_code = 201
    return product_usecase.add_single_product(model)
