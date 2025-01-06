from workflow import processor
import unittest
import json

class TestProcessor(unittest.TestCase):
    
    def testProcess(self):
        with open('output/example_streptococcus.json', 'r', encoding='utf-8') as file:
            loadedTable = json.load(file)
        generatedTable = processor.process('resources/v_14.0_Breakpoint_Tables.xlsx', 'Streptococcus A,B,C,G')
        vanilla_json = generatedTable.to_json(orient="records")
        parsed_json = json.loads(vanilla_json)
        self.assertEqual(loadedTable, parsed_json)

if __name__ == '__main__':
    unittest.main()