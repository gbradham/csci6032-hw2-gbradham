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

Pass `--top N` to also report the N most frequent whitespace-separated words.
Words are grouped case-insensitively and sorted by decreasing frequency, then
alphabetically to break ties:

```bash
python3 src/text_stats.py sample.txt --top 3
```

The JSON output includes a `top` list of `word`/`count` objects. Without
`--top`, the output contains only the basic statistics above.

Run the tests with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover -s tests
```

## Docker development environment

The Docker image uses the small `python:3.13-slim-trixie` base image and
installs Python/pip, Git, `gh`, and GitHub Copilot CLI `1.0.83` (the stable
`latest` release resolved on 2026-09-15). The Copilot version is pinned by the
`COPILOT_VERSION` build argument in `Dockerfile`; it is not a prerelease.

Build on macOS:

```bash
docker build --tag csci6032-hw2-agent .
```

Run with the repository mounted at `/workspace`:

```bash
docker run --rm --interactive --tty \
  --mount type=bind,source="$PWD",target=/workspace \
  csci6032-hw2-agent
```

This opens a Bash shell in the Linux container; run `python`, `pip`, Git,
`gh`, or `copilot` from there.

For persistent, Docker-managed authentication state, use named volumes rather
than mounting host credential directories:

```bash
docker volume create csci6032-gh-config
docker volume create csci6032-copilot-config
docker run --rm --interactive --tty \
  --mount type=bind,source="$PWD",target=/workspace \
  --mount type=volume,source=csci6032-gh-config,target=/home/dev/.config/gh \
  --mount type=volume,source=csci6032-copilot-config,target=/home/dev/.copilot \
  csci6032-hw2-agent
```

The image does not copy repository files or credentials and does not require a
browser profile or Docker socket. On native Linux, build with the host user's
UID/GID to keep the bind-mounted files writable:

```bash
docker build \
  --build-arg DEV_UID="$(id -u)" \
  --build-arg DEV_GID="$(id -g)" \
  --tag csci6032-hw2-agent .
```
