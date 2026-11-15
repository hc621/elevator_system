# Elevator System Simulation

A discrete-time simulation of a destination-dispatch elevator system: passengers give their origin and destination
when they make a request, the controller assigns them to one car straight away, and the simulation moves time forward
one tick (one floor of travel) at a time.

> Work in progress. Usage, design, assumptions, results and time spent will be written here as the build goes on.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest --cov
ruff check . && ruff format --check .
```
