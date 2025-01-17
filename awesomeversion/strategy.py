"""Strategies for AwesomeVersion."""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Pattern, Tuple

from .utils.regex import (
    RE_BUILDVER,
    RE_CALVER,
    RE_PEP440,
    RE_SEMVER,
    RE_SIMPLE,
    RE_SPECIAL_CONTAINER,
    generate_full_string_regex,
)


class AwesomeVersionStrategy(str, Enum):
    """Strategy enum."""

    BUILDVER = "BuildVer"
    CALVER = "CalVer"
    SEMVER = "SemVer"
    SIMPLEVER = "SimpleVer"
    PEP440 = "PEP 440"

    UNKNOWN = "unknown"

    SPECIALCONTAINER = "SpecialContainer"


@dataclass
class AwesomeVersionStrategyDescription:
    """Description of a strategy."""

    strategy: AwesomeVersionStrategy
    regex_string: str
    pattern: Pattern[str]


COMPARABLE_STRATEGIES = [
    strategy
    for strategy in AwesomeVersionStrategy
    if strategy
    not in (AwesomeVersionStrategy.UNKNOWN, AwesomeVersionStrategy.SPECIALCONTAINER)
]

VERSION_STRATEGIES: Tuple[AwesomeVersionStrategyDescription, ...] = (
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.BUILDVER,
        regex_string=RE_BUILDVER,
        pattern=generate_full_string_regex(RE_BUILDVER),
    ),
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.CALVER,
        regex_string=RE_CALVER,
        pattern=generate_full_string_regex(RE_CALVER),
    ),
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.SEMVER,
        regex_string=RE_SEMVER,
        pattern=generate_full_string_regex(RE_SEMVER),
    ),
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.SPECIALCONTAINER,
        regex_string=RE_SPECIAL_CONTAINER,
        pattern=generate_full_string_regex(RE_SPECIAL_CONTAINER),
    ),
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.SIMPLEVER,
        regex_string=RE_SIMPLE,
        pattern=generate_full_string_regex(RE_SIMPLE),
    ),
    AwesomeVersionStrategyDescription(
        strategy=AwesomeVersionStrategy.PEP440,
        regex_string=RE_PEP440,
        pattern=generate_full_string_regex(RE_PEP440),
    ),
)


VERSION_STRATEGIES_DICT: Dict[
    AwesomeVersionStrategy, AwesomeVersionStrategyDescription
] = {description.strategy: description for description in VERSION_STRATEGIES}
