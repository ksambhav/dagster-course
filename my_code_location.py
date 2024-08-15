from dagster import Definitions, asset


@asset
def my_asset():
    return "Hello, Dagster!"


defs = Definitions(assets=[my_asset])
