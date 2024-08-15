from dagster import Definitions, load_assets_from_package_module

from another_code_location.assets import orders

# orders_asset = load_assets_from_modules([orders], group_name="order_group")

orders_asset = load_assets_from_package_module(package_module=assets)

defs = Definitions(
    assets=[*orders_asset]
)
