# Using Python programming to train a bot for Mega run (an endless runner game)

Explorations of Using Python to play Mega run, mainly for the purposes of creating self-driving cars and other vehicles.

We read frames directly from the desktop, rather than working with the game's code itself. This means it works with more games than just Mega run, and it will basically learn (well, attempt to learn...) whatever you put in front of it based on the frames as input and key presses as output.

Currently, to use the latest version of this AI, you will need to run first "create_training_data.py," then balance this data with "balance_Data.py."

When creating training data, this works when you have the game in windowed mode, 800x600 resolution, at the top left of your screen. You need this for both training and testing. Eventually we can go off the window's name, but, for now, the current code wants the window in the corner.

Next, Train the model with train_model.py.

Finally, use the model in game with test_model.py. 
