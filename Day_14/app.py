def start_game():
    # Initial game prompt
    print("\n🌲 You wake up in a dark forest. It's cold and silent.")
    print("You see two paths ahead:")
    print("1️⃣ Follow the mysterious light.")
    print("2️⃣ Walk toward the sound of water.")

    # Get user choice
    choice = input("Enter 1 or 2: ")

    # Call the appropriate function based on user choice
    if choice == "1":
        mysterious_light()
    elif choice == "2":
        sound_of_water()
    else:
        # Handle invalid choice and restart the game
        print("❌ Invalid choice! Try again.")
        start_game()

def mysterious_light():
    # Scenario for following the mysterious light
    print("\n💡 You follow the glowing light and reach a strange cabin.")
    print("The door is slightly open. Do you:")
    print("1️⃣ Enter the cabin.")
    print("2️⃣ Walk away.")

    # Get user choice
    choice = input("Enter 1 or 2: ")

    # Handle user choice for the mysterious light scenario
    if choice == "1":
        print("\n🏚 You step inside... It's a trap! You are captured! ❌ Game Over.")
    elif choice == "2":
        print("\n🏃 You walk away safely and find a road! 🎉 You win!")
    else:
        # Handle invalid choice and restart the mysterious light scenario
        print("❌ Invalid choice! Try again.")
        mysterious_light()

def sound_of_water():
    # Scenario for following the sound of water
    print("\n💦 You reach a river with a small boat. Do you:")
    print("1️⃣ Take the boat across.")
    print("2️⃣ Follow the river on foot.")

    # Get user choice
    choice = input("Enter 1 or 2: ")

    # Handle user choice for the sound of water scenario
    if choice == "1":
        print("\n🚣 The boat has a hole! You sink! ❌ Game Over.")
    elif choice == "2":
        print("\n🚶 You follow the river and find a village! 🎉 You win!")
    else:
        # Handle invalid choice and restart the sound of water scenario
        print("❌ Invalid choice! Try again.")
        sound_of_water()

# Start the game
start_game()
