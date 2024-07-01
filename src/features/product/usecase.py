from typing import List

import sqlalchemy as sa
from sqlalchemy import orm

from features.product.schemas.product_schema import ProductSchema
from features.product.models.product_model import (
    ProductModel,
    ProductCreateModel,
)  # noqa: E501


class ProductUsecase:
    def __init__(self, sql_engine: sa.Engine) -> None:
        # create database session
        self.__sql_session = orm.Session(sql_engine)

    def __del__(self) -> None:
        # close database session
        self.__sql_session.close()

    def get_all_products(self) -> List[ProductModel]:
        # query for latest 10 entries
        select_query = (
            sa.Select(ProductSchema)
            .order_by(ProductSchema.id.desc())
            .limit(10)  # noqa: E501
        )
        # make query to database
        query_data = self.__sql_session.scalars(select_query)

        # prase data as list of ProductModel and return
        return [ProductModel.model_validate(item) for item in query_data]

    def get_product_with_id(self, product_id: int) -> ProductModel | None:
        # query for record with id
        select_query = sa.Select(ProductSchema).where(
            ProductSchema.id == product_id
        )  # noqa: E501
        # make query to database
        query_data = self.__sql_session.scalar(select_query)

        # parse & return model
        return ProductModel.model_validate(query_data) if query_data else None

    def add_single_product(
        self,
        model: ProductCreateModel,
    ) -> ProductModel:
        # create product schema
        record = ProductSchema(**model.model_dump())

        # add record to table
        self.__sql_session.add(record)
        # commit transaction
        self.__sql_session.commit()

        # refresh record
        self.__sql_session.refresh(record)
        # create & return ProductModel from record
        return ProductModel.model_validate(record)
