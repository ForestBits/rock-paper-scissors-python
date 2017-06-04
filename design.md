# Stab, Slash, Swing

AKA rock-paper-scissors with swords and other stuff.

## Inspiration
rock-paper-scissors is, at heart, a mindgame. However, it is limited in scope and gets boring quickly. It could be modified with more choices, but this largely just makes it feel more random.

This new concept changes two things. First, it is themed - no scissors here, I am afraid. We need swords now.

Second, the rules are different. We need to extend the mindgames. Rather than selecting one action per turn, you select multiple actions - and try to extend your predictions about what your opponent will do.

For example, suppose you can choose two actions per turn. P1 chooses to jump, then attack. P2 chooses to attack, then block. P2 misses on turn 1, then block P1's attack on turn 2, leaving both players as they were.

But there were other possibilities. For example, P1 could duck on turn 1 and turn 2, and perhaps never get hit at all.

## Rules

On each turn, players choose **3** actions. Each pair of actions - P1 and P2's action 1, P1 and P2's action 2, and so on - are done at the same time - one does not go before the other. As a result, every action pair has a defined and consistent result.

##### Winning

The objective of the game is to kill your opponent. Each player has health - they can take **5** damage. Damage is the result of being hit with certain types of moves that are not countered in some way, such as blocking or dodging. The first player to take 5 damage loses. The game proceeds until this is the case - repeated selections of 3 moves are played out until a player has won.

##### Turn

Each turn, each player chooses their sequence of actions to perform. Actions have varying states and possibilities attached to them. For example, if you jump on turn 1, you are, conceptually, in the air at the start of turn 2. Therefore, you would not be allowed to duck an attack on turn 2.

Actions can take multiple time units. For example, perhaps a strong attack "charges" on turn 1, but hits for 3 damage on turn 2, provided it isn't interrupted.

States and times work cross-turn. Thus, each turn you really have 3 **time-units**. You could use a move that takes 2 units and a move that requires 1 unit, or 3 one-unit moves, or perhaps a 3-unit move. If you choose a move for time unit 3 that requires 2 time units, the first part takes place in this turn, and the next part takes place the following turn. There would then only be 2 remaining time-units in the next turn.

This leaves a question: if you have 3 time-units per turn, but can choose an action sequence longer than 3 time-units... how does that work? Each turn, you can choose at least one action. If you have remaining time units left after this, you can choose another action. Alternatively, if you keep choosing large actions, it behaves less as if you pick a sequence, and more as if you are continuously picking actions. However, your opponent's actions are independent from yours.

Thus, state - health, timings, possible other effects - carry over each turn. This adds to the extended mindgame element.

##### States

On a given time-unit or turn, the player may be in a number of states. A player can have multiple states in effect at once, although some states will replace other states, as they are mutually exclusive. The moves available for a given time unit are determined by the states the player is in.

- **Standing** - this is the neutral state, such as at the start of the game. It indicates the player is on the ground, but not ducking or blocking.
- **Air** - the player is in the air, such as after jumping.  
- **Standing Block** - the player is blocking while standing.
- **Ducking** - the player is ducking. This makes some attacks miss.
- **Standing Attack** - the player is attacking while standing.
- **Air Attack** - the player attacks from the air.
- **Duck Attack** - the player attacks while ducked/crouching (no actual ducks involved).
- **Block Low** - the player blocks attacks from ducking opponents.

##### Actions

TBD.
