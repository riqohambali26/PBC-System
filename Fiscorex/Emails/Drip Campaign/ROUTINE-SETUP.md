# Run the Fiscorex drip as a routine on claude.ai

Goal: a fresh Claude session starts every day, sends whatever is due through Wawai Mail, and saves progress to this repo. It no longer depends on the long-running session.

I have not seen the routines screen, so button names below may differ slightly. Follow the order, not the exact labels.

## Steps

1. Open claude.ai and go to **Routines** (scheduled tasks). Choose **New routine**.
2. **Name:** `Fiscorex drip daily run`.
3. **Schedule:** daily at 15:17 UTC. Pick your own time zone in the screen if it offers one (15:17 UTC is about 8:17 am Pacific / 11:17 am Eastern). Weekdays only is fine if you prefer; the schedule catches up on missed days.
4. **Repository:** add `riqohambali26/pbc-system` with permission to push, on branch `claude/inspiring-brown-p166g9`. The routine reads and saves `drip-state.json` there.
5. **Connectors:** turn on **Wawai Mail**. This is the part that cannot be done from inside a Claude Code session. Without it the routine cannot send.
6. **Prompt:** paste everything under "Prompt to paste" below.
7. **Permissions:** allow the routine to run without asking for approval (auto or "always allow"), otherwise it will wait for you to click.
8. **Test first, without sending:** use **Run now** (or "Run with message") and add the words `DRY RUN` to the message. The routine should report four things and send nothing: the repo and last saved step, whether Wawai answers, whether it can save to the repo, and which steps are due today. If any of those fails, fix it before going on.
9. **Switch off the old daily task** so both do not send. Tell Claude in the long-running session: "disable the old drip task". Until then, keep the new routine paused.
10. **Turn the routine on.** Check `drip-state.json` in the repo the next morning: new entries with today's date mean it worked.

## Things to know

- Credit: Wawai shows $0 with 1,000 free sends. If a send is refused for credit, the routine stops and says so. Add credit in Wawai before then.
- Each run saves a line per step to `drip-state.json`. A run that cannot save sends nothing, so a step is never sent twice.
- Failed addresses are tagged into the Wawai group `Invalid-Email`. The spreadsheet list (`invalid-emails.csv`) is not in the repo, so names and second emails are only on the long-running session's disk.
- Stop the campaign any time by pausing the routine.

## Prompt to paste

Fiscorex drip campaign daily run, started fresh each day (the user approved this automation on 2026-10-27).

DRY RUN: if the message that started this run contains the words DRY RUN, send nothing, import nothing, commit nothing. Only report: (a) whether the repo is readable and the last entry of "done" in drip-state.json; (b) whether Wawai select_account and list_segments work; (c) whether `git push --dry-run` works; (d) which steps would be due today. Then stop.

SETUP. The repo is GitHub riqohambali26/pbc-system, branch claude/inspiring-brown-p166g9. If /home/user/PBC-System does not exist, clone it, then check out the branch and git pull. Work in "Fiscorex/Emails/Drip Campaign". Read WAWAI-AUTOMATION.md and drip-state.json. Before sending anything run `git push --dry-run`; if it fails, send nothing and report, because progress could not be saved.

WHAT IS DUE. Today's UTC date. For each group g=1..12 (Wawai group Drip-gg, zero padded) and each step day d in step_days (step index i = 1-based position) the step is due if starts[g] + (d-1) days == today and it is not already in "done". Also run overdue steps not in "done", oldest first. Before each send, call list_active_campaigns (large output: read the saved file with python) and confirm no campaign for that group and step went out in the last 20 hours, so a repeated run never double-sends.

SENDING. Select Wawai account f723af01-f6f2-4edf-b3a6-9f1b0161273b (select_account) before any Wawai call. from_name is "John Krowiak". Get HTML and subject with `python3 -I to_wawai.py <email-NN file>` (stdout is the HTML, the first stderr line is the subject; for the Day 3 EMAIL-01 resend use the "resend:" subject). Odd i: send EMAIL-((i+1)/2). Even i: resend EMAIL-(i/2) to non-clickers.
Audiences, always delivered contacts only (failed addresses are never emailed again):
- Main send, groups 1 to 6: use the existing group Drip-01-NC-2, Drip-02-NC-2, ... Drip-06-NC-2 (they hold the delivered contacts).
- Main send, groups 7 to 12: build group Drip-gg-OK with import_contacts from the group's first EMAIL-01 campaign recipients (get_campaign_recipients, all pages): delivered=true and no clicked_links containing "unsubscribe". The first EMAIL-01 send itself goes to the whole group Drip-gg.
- Resend: from the group's previous send in "done", contacts with delivered=true, no clicked link containing "calendly" and none containing "unsubscribe"; import them into a fresh group Drip-gg-NC-<i>. Skip if nobody qualifies.
Then preview_campaign(segment, native), check recipient_count matches, confirm_send with the converter HTML.

FAILURES. The day after a group's first EMAIL-01, contacts in that group with no delivered=true record are reported only: tag them into the Wawai group Invalid-Email with import_contacts. Never email them again and do not use Email 2.

RECORDING. Immediately after each confirm_send succeeds, append {group, day, date, campaign_id, recipients} to "done" in drip-state.json, then git add, commit and push (message ends with "Co-Authored-By: Claude <noreply@anthropic.com>"). Never commit invalid-emails.csv or drip-contacts.csv.

If a send fails (for example not enough Wawai credit), do not retry; record it as blocked in drip-state.json and say so plainly. If nothing is due, stay silent. Final message: one or two lines.
