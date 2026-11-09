"""@brief Smoke test: the package imports and its constants are consistent."""

import sys

from library_project import constants


def test_python_version_is_3_13_or_newer() -> None:
    """@brief The project requires Python 3.13 or newer."""
    assert sys.version_info >= (3, 13)


def test_rating_bounds_are_ordered() -> None:
    """@brief The lowest rating is below the highest rating."""
    assert constants.RATING_MIN < constants.RATING_MAX


def test_routes_start_with_a_slash() -> None:
    """@brief Every route constant is an absolute path."""
    routes = [
        constants.ROUTE_HOME,
        constants.ROUTE_ADD,
        constants.ROUTE_EDIT,
        constants.ROUTE_DELETE,
    ]
    assert all(route.startswith("/") for route in routes)
