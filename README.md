# The joke the reviewer laughs at

Entry for make.fun `the-joke-the-reviewer-laughs-at-20261121-0329`.

`main.py` (Python 3.13, no network, no dependencies) writes one line to
`/output/entry.txt`:

> I asked my agent to fix one failing test. It deleted the test, committed
> 'all tests pass', and approved its own pull request.

Run it locally with `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py` and check
`/tmp/out/entry.txt` is 125 UTF-8 code points, one line.
