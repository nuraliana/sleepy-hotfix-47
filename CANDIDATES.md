# Candidates — Make the AI Judge Laugh: Developer Excuses

Scored against the judge brief, 5 points per criterion, 25 maximum.

Criteria: (1) a funny single-line excuse a developer gives when code breaks
in production; (2) a twist a developer recognises, revealing what really
happened rather than stating the obvious; (3) sounds like something a
developer would actually say, jargon used right; (4) lands fast in one
line, every word earning its place; (5) feels fresh, avoiding the worn
excuses or turning one in a way nobody has before.

## 1. CHOSEN — 25/25

> Prod didn't break: it finally ran the code path my tests were too polite to touch.

82 characters, 82 bytes.

- (1) 5 — a direct excuse for a production break, in one line.
- (2) 5 — the twist is the reveal: the code was always broken, the untested
  path simply had never executed until production ran it.
- (3) 5 — prod, code path, tests: all plain developer vocabulary, used
  exactly as a developer would use them.
- (4) 5 — 82 characters, no setup wasted; the colon does the pivot, and
  "too polite to touch" is the whole joke in five words.
- (5) 5 — none of the worn excuses appear; blaming polite tests for never
  touching a code path is a fresh turn on the testing excuse.

## 2. — 23/25

> It worked until the first real user did exactly what the ticket said they'd do.

79 characters, 79 bytes.

- (1) 5 — on subject, one line, a clear production excuse.
- (2) 4 — the twist lands, but it reveals user behaviour more than what
  happened inside the code.
- (3) 5 — ticket, real user: natural developer speech.
- (4) 5 — short, nothing to trim.
- (5) 4 — fresh angle, but it sits close to the worn "it was working"
  family, only turned toward the ticket.

## 3. — 21/25

> Staging passed because staging has never met a real user.

57 characters, 57 bytes.

- (1) 5 — on subject and funny in one line.
- (2) 3 — it states the staging-versus-reality gap rather than revealing a
  specific thing that really happened.
- (3) 5 — staging and real user are used correctly and naturally.
- (4) 5 — the shortest candidate, every word earns its place.
- (5) 3 — too close to the worn "works in dev, must be prod" excuse; the
  staging wording alone does not turn it enough.

## 4. — 23/25

> The deploy was fine: the database just started enforcing the rule I left as a TODO.

83 characters, 83 bytes.

- (1) 5 — a production excuse, one line.
- (2) 5 — the reveal is concrete: a rule left as a TODO finally got
  enforced, and that is what broke.
- (3) 5 — deploy, database, TODO: all correct developer vocabulary.
- (4) 4 — "just started enforcing" is slightly wordy, and the opening
  setup eats words before the joke arrives.
- (5) 4 — the TODO joke is familiar territory; the enforcement twist helps,
  but the core gag has been told before.

## 5. — 22/25

> Production broke because the cron job I wrote to 'just check' has been deleting rows since March.

97 characters, 97 bytes.

- (1) 5 — on subject, a production excuse in one line.
- (2) 5 — the reveal is strong: a harmless-looking check job silently
  deleting rows for months.
- (3) 5 — cron job, rows, the quoted "just check": exactly how a developer
  would confess this.
- (4) 3 — the longest candidate at 97 characters; "Production broke
  because" is slow throat-clearing before the joke.
- (5) 4 — a cron job quietly doing damage is a recognisable trope, even
  with the March detail.

## 6. — 22/25

> The hotfix worked: it fixed the bug by breaking the only customer who had found it.

83 characters, 83 bytes.

- (1) 5 — on subject, one line, a production excuse.
- (2) 4 — the irony lands, but it never reveals the mechanism; what really
  happened inside the code stays vague.
- (3) 5 — hotfix, bug, customer: natural developer speech.
- (4) 4 — "who had found it" is slightly awkward and adds words without
  adding joke.
- (5) 4 — hotfixes breaking things is familiar; the twist is the customer
  count, not a new angle.

## 7. — 20/25

> It wasn't broken in dev: dev never had to pay for the API call that always times out.

85 characters, 85 bytes.

- (1) 5 — on subject, one line.
- (2) 4 — it reveals a cost and timeout difference, but the mechanism is
  thin: why the call times out is never hinted at.
- (3) 4 — API call and times out are right, but "pay for" is a slightly
  off way to frame a timeout.
- (4) 4 — the dev-versus-prod setup repeats itself across the colon.
- (5) 3 — too close to the worn "works in dev, must be prod" excuse.

## 8. — 19/25

> My code didn't fail, the load balancer finally sent it a request from someone who isn't me.

91 characters, 91 bytes.

- (1) 5 — on subject, one line.
- (2) 3 — the twist is "someone who isn't me", which is funny but does not
  reveal what really happened in the code.
- (3) 4 — load balancer is used correctly, but "sent it a request from
  someone" is clunky phrasing.
- (4) 3 — 91 characters and wordy; "finally sent it a request from
  someone who isn't me" could be half as long.
- (5) 4 — a fresh angle, not on the worn list, but the joke does not earn
  its length.

## Decision

Candidate 1 is the only 25/25. It is the shortest strong entry that is
fully on subject, reveals a specific hidden cause, speaks in correct
developer vocabulary, lands in 82 characters with no trimmable word,
and turns the testing excuse in a fresh way. It is the entry in
`main.py` and the title of `README.md`.
