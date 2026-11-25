"""Monday Morning Punchlines entry.

Chosen line (79 chars, gate 1-200):
    "My alarm clock quit this morning. Said Mondays were a hostile work environment."

Decision record (judged against the published brief, in the judge's own order):
  1. Is it really about Monday mornings? 2. Real laugh with a turn?
  3. Surprise? 4. Economy of words? 5. Freshness?

Candidates weighed:
  A. "My alarm didn't go off this morning. It saw it was Monday and hit
     snooze on me." (84 chars)
     Role reversal: the alarm gives up too. Punch lands and it is firmly
     Monday morning. LOSES: the snooze button is the first gag anyone
     reaches for on this topic, so it fails criterion 5 (freshness) and
     partly criterion 3 (the twist is the most expected one).
  B. "Monday is the only morning my coffee needs coffee." (48 chars)
     Very tight, every word works, and the recursion is neat. LOSES: it is
     a complaint dressed as a joke - no real turn, no punchline, just a
     statement of suffering - and "coffee needs coffee" is a known trope.
     Fails criteria 2 and 5.
  C. "I set five alarms for Monday. All five of them called in sick."
     (63 chars)
     Role reversal again, punchline at the end, good economy. LOSES: it is
     a close cousin of A - the same alarm-refuses mechanism - and "five
     alarms" is a familiar setup. Beats B on laugh, loses to the winner on
     surprise.
  D. "My alarm clock quit this morning. Said Mondays were a hostile work
     environment." (79 chars) - CHOSEN
     The alarm doesn't just fail, it resigns with cause: HR language
     ("hostile work environment") applied to an alarm clock. The punchline
     reframes Monday as a workplace even the alarm won't tolerate. Monday
     morning is anchored by "this morning" + the alarm; the turn lands in
     the second sentence; the framing is fresher than snooze/oversleep gags.

Writing passes (genuine revisions to the winning line):
  Pass 1: Early leader was A ("My alarm didn't go off..."). Replaced by D
     because A's snooze twist is the first thing anyone writes about Monday
     alarms; D's HR framing is less expected and the punchline lands
     harder - the alarm doesn't merely fail, it quits with a formal reason.
  Pass 2: First draft of D read "My alarm clock quit this morning. It said
     Mondays are a hostile work environment." Trimmed "It said" to "Said
     Mondays were..." - tighter (criterion 4, every word doing work) and
     the past tense "were" keeps the whole line in this morning's voice.
     Kept "this morning" deliberately: without it the joke is about Monday
     in general and loses criterion 1.
"""

import os

ENTRY = "My alarm clock quit this morning. Said Mondays were a hostile work environment."
MAX_CHARS = 200


def validate_line(line):
    """Gate guard: the line must be 1-200 characters, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-200 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def check_gate(text):
    """Mirror the sealed gate: 1-200 UTF-8 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def verify_written(path):
    """Write-back self-check: entry.txt must contain the line plus newline."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("written entry.txt does not match the line")


def main():
    validate_line(ENTRY)
    if not check_gate(ENTRY):
        raise ValueError("entry fails the 1-200 character gate")
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    verify_written(path)


if __name__ == "__main__":
    main()
