# EUCAST MIC Extractor

This Python script processes MIC (Minimum Inhibitory Concentration) tables from EUCAST xlsx files, specifically those in the format of breakpoint tables. The script extracts relevant data, processes it, and outputs the results as a JSON file.

## Features

- Loads an Breakpoint_Tables.xlsx workbook with one or more sheets.
- Extracts data related to MIC breakpoints from a specified sheet.
- Cleans and formats the data into a structured table with relevant information.
- Outputs the cleaned data as a JSON file in the `output/` directory.

## Requirements

- Run with Python 3.12
- Required Python libraries:
  - `pandas`
  - `openpyxl`
  - `re`
  - `argparse`
  - `json`

## Usage

Use the code directly (Starting Point: preprocessor.process()) or run the script from the command line, use the following syntax:
`python mic_processor.py <input_path> <sheet_name> <output_path>`

### Parameters:

- `input_path`: Path to the Excel file containing the MIC breakpoint tables (e.g., resources/v_12.0_Breakpoint_Tables.xlsx).
- `sheet_name`: The name of the sheet to process (e.g., Streptococcus A,B,C,G).
- `output_path`: Path to the folder where the output JSON file will be saved (e.g., output/example_streptococcus.json).

## Example

`python processor.py resources/v_14.0_Breakpoint_Tables.xlsx "Streptococcus A,B,C,G" output/example_streptococcus.json`

This will:

1. Load the workbook from resources/v_14.0_Breakpoint_Tables.xlsx.
2. Process the sheet named Streptococcus A,B,C,G.
3. Save the cleaned and processed data as a JSON file to the output/example_streptococcus.json (or any custom path specified).

You can find the example output file at output/example_streptococcus.json

## License

This script is provided under the MIT License.

## Troubleshooting

- Error: No such file or directory: 'output/shrunk_table.json'
  This error occurs if the output/ directory doesn’t exist. The script will now automatically create the directory if it’s missing.
- Error: Sheet not found
  If you get an error like Sheet 'Streptococcus A,B,C,G' not found in the workbook, ensure that the sheet name you provided is exactly correct and exists in the Excel file.

## Notes

Some information from the Excel file will be removed. These include:

- brackets -> Indicates that an effect as monotherapy has not been proven.
- superscripts -> Link to further information
- Empty MIC Values
