from typing import Union

from odd_models.models import DataEntity, DataSet, DataEntityType, DataEntityGroup, DataSetField, DataSetFieldType, Type
from oddrn_generator import PostgresqlGenerator



#from .metadata import append_metadata_extension
from .types import TYPES_MONGO_TO_ODD

from odd_mongo_adapter.mongo_generator import MongoGenerator



def map_column(
        column_metadata, oddrn_generator: MongoGenerator,
        parent_oddrn_path: str
) -> DataSetField:
    # print(column_metadata)
    name: str = column_metadata["title"]
    data_type: str = column_metadata["bsonType"]
    dsf: DataSetField = DataSetField(
        oddrn=oddrn_generator.get_oddrn_by_path(f'columns', name),
        name=name,
        metadata=[],
        type=DataSetFieldType(
            type=TYPES_MONGO_TO_ODD.get(data_type, Type.TYPE_UNKNOWN),
            is_nullable=column_metadata["bsonType"] != 'partition_key'
        )
    )

    # append_metadata_extension(
    #     dsf.metadata, _data_set_field_metadata_schema_url, column_metadata, _data_set_field_metadata_excluded_keys
    # )
    return dsf
