# Multi-File Data Analytics Interface

A terminal-based Python application for cross-analyzing multiple large CSV datasets, built for ENDG 233 (University of Calgary). Uses NumPy for high-performance numerical computation and Matplotlib for automated, user-driven visualizations.

## Features

- Reads and processes multiple large CSV datasets (population, country, and threatened species data)
- Dynamic, menu-driven comparison of metrics across datasets
- Automated calculation of averages and other statistical measures using NumPy
- Automated, comparative Matplotlib visualizations

## Files

- `design_project.py` — main program entry point and menu logic
- `np_functions.py` — NumPy-based data analysis functions
- `user_csv.py` — CSV reading/parsing utilities
- `data_files/` — source CSV datasets
- `final_plots/` — generated output visualizations

## Running

```bash
python design_project.py
```
