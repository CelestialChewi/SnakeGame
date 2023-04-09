## How the game works
I'm sure you play Snake Game before right 🤨 so I'm going to explain how I break it into smaller chunks and build the game in PyCharm

### Steps on how to make the game
1. Create a snake body
   * I built my snake with segments instead of elongated square so you can move the snake left and right 
2. Move the snake
   * So how my move function does is moving the last segment (tail/butt) to the 2nd segment position and then the 2nd segment moves to first segment position (head).
   * Left/Right is based on setheading(). (Without != would make your snake goes backward)
3. Create snake's food
   * Randomly generate one food in any coordinates 
4. Detect collision with food
   * +1 to the score if collides with it 
5. Detect collision with wall
   * Reset the snake position and continue the game
6. Detect collision with tail
   * Reset the snake position and continue the game 
7. Create a scoreboard
   * Keep track of current and highscore.
   * I created the highscore.txt so that the highscore is recorded after you quit the programme


