
"""Write your own unittest cases; do not import the instructor solution."""

import unittest
from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from telemetry_capstone import convert_pressure, convert_temperature


class TelemetryCapstoneTests(unittest.TestCase):

    def test_pressure_known_value(self):
        # Check that 100 psi converts correctly to kPa
        result = convert_pressure(100, "psi")
        self.assertAlmostEqual(result, 689.4757, places=3)

    def test_temperature_known_value(self):
        # Check that 212 F equals 100 C
        result = convert_temperature(212, "F")
        self.assertAlmostEqual(result, 100.0)


if __name__ == "__main__":
    unittest.main()
