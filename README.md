CSCI6032
Working safely with agents, git, docker, and skills
https://github.com/gbradham/csci6032-hw2-gbradham
MacOS Tahoe

This is the respository for homework 2 of CSCI6032.

## Text statistics

Run the command-line program with one UTF-8 text file:

```bash
python3 src/text_stats.py sample.txt
```

It prints JSON containing the number of `lines`, whitespace-separated `words`,
and Unicode `characters`. For example, the included `sample.txt` produces:

```json
{"lines": 6, "words": 6, "characters": 28}
```

Run the tests with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover -s tests
```
