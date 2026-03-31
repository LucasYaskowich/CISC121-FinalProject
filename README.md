# Selection Sort Card Game

## Demo video/gif/screenshot of test

## Problem Breakdown & Computational Thinking 

### Why I chose this

I chose selection sort since I had the idea to model the sorting with the process of sorting a hand of cards, and this is a very intuitive way of doing that. It's also a more fun way to learn how this sorting mechanism works, and is a process that many people are likely familiar with.

### How it works

The program uses Gradio to create an app interface. When a new game is initiated, a hand is "dealt", meaning a random sample of tuples (cards) containing rank and suit are created. The size of this sample (the hand) is determined by the user's score from the last round. New players get 5 cards, and after the first game 2 cards are dealt more than the player's score, to allow learning at the player's own speed. The hand size is capped at 12. Once a hand is dealt, the user has choice of selecting the lowest card out of the hand. The game then automatically swaps the two cards, adds one to the player's score, and the correctly sorted card turns green to show the "sorted" portion of the hand. The user continues swapping until the whole hand is in the sorted portion, just as selection sort works. If the user selects an incorrect option, the correct swap is shown, and the score remains unchanged. At the end of the game, the score is displayed, for feedback purposes.

### Decomposition
- Card generation: generate a random hand of N cards
- Hand rendering: display the hand with clear sorted/unsorted potions
- Turn handler: check user input against correct solution, perform the swap, update core
- Game loop: new game feature, state dictionary
- UI: displays cards and captures player input

### Pattern Recognition
Selection sort always scans the unsorted portion for the minimum
and swaps it to the front. Each round repeats this same scan-and-swap
pattern, the player learns this by doing it themselves.

### Abstraction
Cards are simplified to rank + suit. The algorithm's array indices
are hidden, instead the player just sees a hand of cards and picks
the smallest.

### Algorithm Design
Input: random hand → Processing: player picks min each round,
validated against selection sort logic → Output: sorted hand + score

## Steps to Run
1. Clone this repo
2. `pip install -r requirements.txt`
3. `python app.py`

## Hugging Face Link
[link here]

## Testing & Verification
<!-- Document your test cases here -->

## Author & Acknowledgments
