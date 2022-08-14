# MariahsModels

1. Install the latest Python and Julia
2. Open a terminal and `cd` into the directory for this project
3. Run `python -m pip -r requirements.txt` to install Python dependencies
4. Run `julia config.jl` to install Julia dependencies
5. Add `sentences.csv` to the `data` folder
6. Run `python preprocess.py` to prepare the coded data. If you need to add/modify regexes, do it here
7. Run `julia main.jl` to run all models on the coded data. If you need to add/modify to `main.jl` and don't want to wait forever between runs, instead run `julia`, then in the Julia REPL run `include("main.jl")` each time you want to re-load the main to see changes.
8. Find results in the `models` subfolders, bigger numbers are more recent