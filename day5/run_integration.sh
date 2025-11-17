#!/bin/bash

uv run adk eval home_automation_agent home_automation_agent/integration.evalset.json --config_file_path=home_automation_agent/test_
config.json --print_detailed_results
