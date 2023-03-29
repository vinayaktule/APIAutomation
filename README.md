# APIAutomation
#Pytest Framework for basic API automation

## Installing framework dependencies

```bash
pip install -r requirement.txt 
```

## CLI command to run test file using pytest
```bash
pytest <file_path>/<test_file>.py
```

## CLI command to run generate html report for test
```bash
pytest <file_path>/<test_file>.py --html=report.html
```

## CLI command to run generate allure report for test
```bash
pytest --alluredir=<report_path> <test_file>.py
allure serve <path to report directory>
```

