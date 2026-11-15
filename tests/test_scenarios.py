import pytest

from elevator_sim.scenarios import SCENARIOS, generate


@pytest.mark.parametrize("scenario", sorted(SCENARIOS))
def test_generated_requests_are_valid_sorted_and_reproducible(scenario: str) -> None:
    requests = generate(scenario, floors=20, count=200, duration=100, seed=5)
    assert requests == generate(scenario, floors=20, count=200, duration=100, seed=5)
    assert requests != generate(scenario, floors=20, count=200, duration=100, seed=6)
    assert [r.time for r in requests] == sorted(r.time for r in requests)
    assert all(0 <= r.time < 100 for r in requests)
    assert all(1 <= r.source <= 20 and 1 <= r.dest <= 20 and r.source != r.dest for r in requests)
    assert [r.id for r in requests] == [f"p{i}" for i in range(1, 201)]


def test_morning_rush_is_mostly_from_the_lobby() -> None:
    requests = generate("morning_rush", floors=30, count=1000, duration=100, seed=1)
    share = sum(r.source == 1 for r in requests) / len(requests)
    assert 0.75 < share < 0.85


def test_two_floor_building() -> None:
    requests = generate("mixed", floors=2, count=10, duration=5, seed=0)
    assert all({r.source, r.dest} == {1, 2} for r in requests)


@pytest.mark.parametrize(
    ("args", "message"),
    [
        (("lunch", 10, 5, 5, 0), "unknown scenario"),
        (("uniform", 1, 5, 5, 0), "floors"),
        (("uniform", 10, 5, 0, 0), "duration"),
    ],
)
def test_bad_arguments(args: tuple, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        generate(*args)
