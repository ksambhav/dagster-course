from dagster import Definitions, load_assets_from_package_module

from wb_etl import assets

all_assets = load_assets_from_package_module(package_module=assets)

defs = Definitions(
    assets=[*all_assets]
)
