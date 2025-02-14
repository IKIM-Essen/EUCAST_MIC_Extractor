# Copyright 2025 by Miriam Balzer & Julian Welling, University of Duisburg-Essen
# Licensed under the MIT License
# This file may be copied, modified, and distributed under the terms of the MIT License.

import unittest
import json
import processor


class TestProcessor(unittest.TestCase):
    def test_process(self):
        with open("output/example_streptococcus.json", "r", encoding="utf-8") as file:
            loaded_table = json.load(file)
        generated_table = processor.process(
            "resources/v_14.0_Breakpoint_Tables.xlsx", "Streptococcus A,B,C,G"
        )
        vanilla_json = generated_table.to_json(orient="records")
        parsed_json = json.loads(vanilla_json)
        self.assertEqual(loaded_table, parsed_json)


if __name__ == "__main__":
    unittest.main()
