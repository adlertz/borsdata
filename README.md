# Setup

We probably want to use pandas (https://pandas.pydata.org) so it can be good to
install this on your machine. For Arch Linux it's just as simple as `pacman -S
python-pandas`.

For now though it's not needed.

# Run

Set the environment variable `BORSDATA_AUTH_KEY` with the API key from
Börsdata. Then run `python main.py` or just `./main.py`.

```
export BORSDATA_AUTH_KEY=...
python main.py
```

For now the script just loads the (first 20) available branches at Börsdata.
