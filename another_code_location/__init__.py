from dagster import Definitions, load_assets_from_modules

from another_code_location.assets import orders

orders_assert = load_assets_from_modules([orders], group_name="order_group")

defs = Definitions(
    assets=[*orders_assert]
)
