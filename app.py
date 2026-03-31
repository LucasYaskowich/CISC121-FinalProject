import random
import gradio as gr

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

def generate_hand(size=5):
    '''generate a deck, unique hand'''
    deck = [(rank, suit) for rank in ranks for suit in suits]
    hand = random.sample(deck, size)
    return hand

def render_hand(hand, sorted_count):
    '''render the hand as HTML, showing sorted and unsorted portions'''
    html = "<div style='display: flex; gap: 10px;'>"
    
    for i, card in enumerate(hand):
        rank, suit = card
        color = "red" if suit in ["Hearts", "Diamonds"] else "black"
        border = "2px solid green" if i < sorted_count else "1px solid gray"
        bg = "lightgreen" if i < sorted_count else "white"
        html += f"<div style='border: {border}; padding: 10px; text-align: center; color: {color}; background: {bg}; border-radius: 5px;'>{rank} of {suit}</div>" 
        

    html += "</div>"
    return html

def find_minimum(hand, sorted_count):
    '''find the minimum card in the unsorted portion of the hand'''
    unsorted = hand[sorted_count:]
    min_card = hand[sorted_count]
    for card in unsorted:
        if ranks.index(card[0]) < ranks.index(min_card[0]):
            min_card = card
    
    return min_card

def handle_turn(player_choice, state):
    hand = state["hand"]
    sorted_count = state["sorted_count"]
    
    correct = find_minimum(hand, sorted_count)
    correct_str = f"{correct[0]} of {correct[1]}"
    
    if player_choice == correct_str:
        chosen_index = hand.index(correct, sorted_count) # get the index of the chosen card in the unsorted portion
        hand[sorted_count], hand[chosen_index] = hand[chosen_index], hand[sorted_count] # swap
        state["sorted_count"] += 1
        state["score"] += 1
        message = f"Correct! The card was: {correct_str}"
        pass
    else:
        message = f"Incorrect. The correct card was: {correct_str}"
        chosen_index = hand.index(correct, sorted_count)
        hand[sorted_count], hand[chosen_index] = hand[chosen_index], hand[sorted_count] # swap
        state["sorted_count"] += 1
        pass
    
    state["total_steps"] += 1
    
    if state["sorted_count"] == len(hand):
        message = f"Game over! Final score: {state['score']}"
        pass

    # build the updated card display HTML
    card_html = render_hand(hand, state["sorted_count"])
    
    unsorted = hand[state["sorted_count"]:]
    
    radio_choices = gr.Radio(choices=[f"{rank} of {suit}" for rank, suit in unsorted])
 
    return state, card_html, radio_choices, message


def new_game(state):
    prev_score = state["score"] if state else 0
    
    if prev_score == 0:
        hand = generate_hand()
    elif prev_score > 10:
        hand = generate_hand(12)
    else:
        hand = generate_hand(prev_score + 2)
    state = {
        "hand": hand,
        "sorted_count": 0,
        "score": 0,
        "total_steps": 0
    }
    
    # Display cards as HTML
    card_html = render_hand(hand, 0)
    # Get the initial radio choices (all cards)
    radio_choices = gr.Radio(choices=[f"{rank} of {suit}" for rank, suit in hand])
    # Initial feedback (empty or welcome message)
    message = "Welcome to the Selection Sort card Game!"
    

    return state, card_html, radio_choices, message


# GRADIO STUFF ---------------------------------------------------------------------------------------

with gr.Blocks() as app:
    state = gr.State()  # holds the game dict
    
    gr.Markdown("# Selection Sort Card Game")
    gr.Markdown("## How to play: ")
    gr.Markdown("You are given a hand of 5 cards. Use the selection sort method to sort them in ascending order. Each turn, pick the smallest card from the unsorted portion of the hand. You will get a point for each correct choice. Try to get the highest score!")
    gr.Markdown("#### Note: Aces are high, suits do not affect the order.")
    card_display = gr.HTML()
    feedback = gr.Markdown()
    choice = gr.Radio(label="Pick the smallest card:")
    submit_btn = gr.Button("Submit")
    new_game_btn = gr.Button("New Game")
    
    submit_btn.click(
        fn=handle_turn,
        inputs=[choice, state],
        outputs=[state, card_display, choice, feedback]
    )
    
    new_game_btn.click(
        fn=new_game,
        inputs=[state],
        outputs=[state, card_display, choice, feedback]
    )

app.launch()