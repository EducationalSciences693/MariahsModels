# MariahsModels

1. Install the latest Python and Julia
2. Run `python -m pip -r requirements.txt` to install Python dependencies
3. Run `julia config.jl` to install Julia dependencies
4. Add `sentences.csv` to the `data` folder
5. Run `python preprocess.py` to prepare the coded data. If you need to add/modify regexes, do it here
6. Run `julia main.jl` to run all models on the coded data. If you need to add/modify to `main.jl` and don't want to wait forever between runs, instead run `julia`, then in the Julia REPL run `include("main.jl")` each time you want to re-load the main to see changes.
7. Find results in the `models` subfolders, bigger numbers are more recent