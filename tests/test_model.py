import pytest

from elevator_sim.model import BuildingConfig, CarSpec, Direction, PlannedStop, Request


def test_direction_of_and_opposite() -> None:
    assert Direction.of(1, 5) is Direction.UP
    assert Direction.of(5, 1) is Direction.DOWN
    assert Direction.of(3, 3) is Direction.IDLE
    assert Direction.UP.opposite is Direction.DOWN
    assert Direction.IDLE.opposite is Direction.IDLE


def test_request_direction_and_direct_time() -> None:
    r = Request(0, "p", 20, 1)
    assert r.direction is Direction.DOWN
    assert r.direct == 19


@pytest.mark.parametrize(
    ("placement", "expected"),
    [
        ("lobby", (1, 1, 1, 1)),
        ("spread", (1, 11, 21, 31)),
        ((5, 6, 7, 40), (5, 6, 7, 40)),
    ],
)
def test_placements(placement: object, expected: tuple[int, ...]) -> None:
    config = BuildingConfig.uniform(40, 4, 8, placement)  # type: ignore[arg-type]
    assert tuple(c.start_floor for c in config.cars) == expected
    assert all(c.capacity == 8 for c in config.cars)


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"floors": 1, "n_cars": 1, "capacity": 1}, "at least 2 floors"),
        ({"floors": 10, "n_cars": 0, "capacity": 1}, "at least 1 car"),
        ({"floors": 10, "n_cars": 1, "capacity": 0}, "capacity"),
        ({"floors": 10, "n_cars": 1, "capacity": 1, "door_time": -1}, "door_time"),
        ({"floors": 10, "n_cars": 2, "capacity": 1, "placement": (1,)}, "lists 1 floors"),
        ({"floors": 10, "n_cars": 1, "capacity": 1, "placement": (11,)}, "outside"),
        ({"floors": 10, "n_cars": 1, "capacity": 1, "placement": "middle"}, "unknown placement"),
    ],
)
def test_invalid_configs(kwargs: dict, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        BuildingConfig.uniform(**kwargs)


def test_config_rejects_no_cars_and_bad_served_floors() -> None:
    with pytest.raises(ValueError, match="at least 1 car"):
        BuildingConfig(10, ())
    with pytest.raises(ValueError, match="served_floors"):
        BuildingConfig(10, (CarSpec(4, 1, frozenset({1, 11})),))


def test_car_spec_can_serve() -> None:
    express = CarSpec(8, 1, frozenset({1, *range(21, 41)}))
    assert express.can_serve(Request(0, "a", 1, 30))
    assert not express.can_serve(Request(0, "b", 1, 10))
    assert CarSpec(8).can_serve(Request(0, "c", 3, 9))


def test_config_and_stop_round_trip_through_dicts() -> None:
    config = BuildingConfig(
        40, (CarSpec(8, 1), CarSpec(6, 21, frozenset({1, *range(21, 41)}))), door_time=2
    )
    assert BuildingConfig.from_dict(config.to_dict()) == config
    stop = PlannedStop(7, 12, ("a",), ("b", "c"))
    assert PlannedStop.from_dict(stop.to_dict()) == stop
