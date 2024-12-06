### General Observations
I've just finished Day 5 puzzles and although I've solved everything to date, I've already found some to be challenging.

In general I could definitely benefit from some knowledge of things like graph theory. I'm sure that many of my solutions will show my lack of experienece in this regard.

Additionally I have not had the time to refactor parts of the code which I know to be inefficent or inelegant.

To that end I will try to make some high-level notes so that when/if I revisit some of these at a future date, I have some reminders.

### Some Puzzle Notes
- Day 5
    - I didn't think my puzzle 1 solution was too bad. Notes below relate to puzzle 2:
    - `reorder_update` is not great. I solved it by swapping pairs and re-running rules, there might be a better way to do it.
    - I wrote a second function for getting the middle page number `new_middle_page` and this worked by sorting each `update` dictionary by it's values, and then finding the middle index value. Obviously sorting dictionaries each time is not great.
    

