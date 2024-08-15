from dagster import asset


@asset(
    description="This is some detailed description"
)
def some_other_asset():
    return "fighter"


@asset(
    description="This is some detailed description of asset 2",
    deps=[some_other_asset]
)
def some_other_asset2():
    return "fighter 12"
