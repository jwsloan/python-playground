from typecats import Cat
import typing as ty


@Cat
class Denomination:
    value: int


@Cat
class Envelope:
    name: str
    denominations: ty.List[Denomination]


@Cat
class Budget:
    month: int
    year: int
    envelopes: ty.List[Envelope]


one = Denomination(value=1)
envelope = Envelope(
    name='Groceries',
    denominations=[one]
)

jan20 = Budget(
    month=1,
    year=2020,
    envelopes=[envelope]
)
