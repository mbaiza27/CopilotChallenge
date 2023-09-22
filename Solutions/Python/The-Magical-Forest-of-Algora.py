lox_moves = ["Twirl", "Leap", "Spin", "Twirl", "Leap"]
drako_moves = ["Spin", "Twirl", "Leap", "Leap", "Spin"]

effects = {
  "TwirlTwirl": "Fireflies light up the forest.",
  "LeapSpin": "Gentle rain starts falling.",
  "SpinLeap": "A rainbow appears in the sky."
}

def dance_effect(lox_move, drako_move):
  return effects[f"{lox_move}{drako_move}"] if f"{lox_move}{drako_move}" in effects else "A mysterious effect takes place."

def simulate_dance(lox_moves, drako_moves):
  return [dance_effect(lox_move, drako_moves[index]) for index, lox_move in enumerate(lox_moves)]

print(simulate_dance(lox_moves, drako_moves))