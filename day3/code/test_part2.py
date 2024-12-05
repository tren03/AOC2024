# test_example.py
import pytest
from part2 import betweeen_regex, start_regex


@pytest.mark.parametrize(
    "input_string,expected_output",
    [
        # Basic cases
        ("some text don't()", "some text "),
        ("do() some text don't()", None),
        ("some text", None),
        # Edge cases
        ("", None),
        ("don't()", ""),
        ("do()", None),
        # Multiple occurrences
        ("some text don't() and more text don't()", "some text "),
        ("do() some text don't() and do() more text don't()", None),
        # Complex patterns
        ("some text (nested (stuff)) don't()", "some text (nested (stuff)) "),
        ("text with $pecial ^haracters don't()", "text with $pecial ^haracters "),
        # Trailing/leading characters
        ("   some text don't()", "   some text "),
    ],
)
def test_start_regex(input_string, expected_output):
    assert start_regex(input_string) == expected_output


@pytest.mark.parametrize(
    "input_string,expected_output",
    [
        # Basic cases
        ("do() some text don't()", [" some text "]),
        ("do() text1 don't() do() text2 don't()", [" text1 ", " text2 "]),
        # Edge cases
        ("some random text", []),
        ("do() some text", []),
        ("some text don't()", []),
        # Complex cases
        ("do() nested (parentheses) don't()", [" nested (parentheses) "]),
        ("do() $pecial ^characters don't()", [" $pecial ^characters "]),
        ("do()   spaced text   don't()", ["   spaced text   "]),
        # Empty string
        ("", []),
        # Overlapping matches
        (
            "do() text1 don't() do() text2 don't() do() text3 don't()",
            [" text1 ", " text2 ", " text3 "],
        ),
        ("do() text1 don't() do() don't()", [" text1 "]),
    ],
)
def test_between_regex(input_string, expected_output):
    assert betweeen_regex(input_string) == expected_output
