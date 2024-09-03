import json
import os
import random
import textwrap

def load_story(file_path):
    """Load a single story from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading story file {file_path}: {e}")
        return {}

def list_story_files(directory):
    """List all JSON story files in the directory."""
    try:
        return [f for f in os.listdir(directory) if f.endswith('.json')]
    except FileNotFoundError:
        print(f"Directory {directory} not found.")
        return []
    except Exception as e:
        print(f"Error listing story files: {e}")
        return []

def print_story(text, choices):
    """Prints the current part of the story and available choices with text wrapping."""
    wrapper = textwrap.TextWrapper(width=70, expand_tabs=False, replace_whitespace=False)
    wrapped_text = wrapper.fill(text)
    print("\n" + "="*72)
    print(f"  {wrapped_text}")
    print("="*72)
    if choices:
        print("\nChoices:")
        for key, choice in choices.items():
            print(f"  {key}. {choice['text']}")

def get_choice(choices):
    """Prompts user to select a choice."""
    while True:
        choice = input("Choose an option (number): ").strip()
        if choice in choices:
            return choice
        else:
            print("Invalid choice, please try again.")

def print_help():
    """Prints the help information with formatting."""
    help_text = (
        "\nAvailable Commands:\n"
        "  start [story_number] - Start a specific story by number.\n"
        "  start random - Start a random story.\n"
        "  stop - Stop the current story and return to the main menu.\n"
        "  list - List all available stories.\n"
        "  help - Show this help message.\n"
        "  exit - Exit the game."
    )
    print("\n" + "="*72)
    print(f"  {help_text}")
    print("="*72)

def main():
    story_dir = 'stories'
    story_files = list_story_files(story_dir)

    intro_message = (
        "Welcome to Giggles & Quests!\n\n"
        "Explore a world of adventures and make choices that shape your story.\n"
        "Type 'help' at any time to see a list of available commands."
    )

    print("="*72)
    print(f"  {intro_message}")
    print("="*72)

    current_story = None  # Track if a story is currently being played

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command.startswith('start '):
                try:
                    if command == 'start random':
                        if story_files:
                            story_file = random.choice(story_files)
                            story_path = os.path.join(story_dir, story_file)
                            story_data = load_story(story_path)

                            current_section = "start"
                            current_story = story_data  # Set current story

                            while True:
                                section = story_data.get(current_section, {})
                                text = section.get("text", "End of story.")
                                choices = section.get("choices", {})

                                print_story(text, choices)

                                if not choices:
                                    break

                                choice = get_choice(choices)
                                current_section = choices[choice]['next']

                        else:
                            print("No stories available to start.")

                    else:
                        story_choice = int(command.split()[1]) - 1
                        if 0 <= story_choice < len(story_files):
                            story_file = story_files[story_choice]
                            story_path = os.path.join(story_dir, story_file)
                            story_data = load_story(story_path)

                            current_section = "start"
                            current_story = story_data  # Set current story

                            while True:
                                section = story_data.get(current_section, {})
                                text = section.get("text", "End of story.")
                                choices = section.get("choices", {})

                                print_story(text, choices)

                                if not choices:
                                    break

                                choice = get_choice(choices)
                                current_section = choices[choice]['next']

                        else:
                            print("Invalid story number.")
                            continue

                except (IndexError, ValueError):
                    print("Invalid story selection or command. Please try again.")

            elif command == 'stop':
                if current_story:
                    print("Stopping the current story and returning to the main menu.")
                    current_story = None
                else:
                    print("No story is currently being played.")

            elif command == 'list':
                if story_files:
                    print("\nAvailable Stories:")
                    for idx, file in enumerate(story_files, start=1):
                        print(f"{idx}. {file}")
                else:
                    print("No stories found.")

            elif command == 'help':
                print_help()

            elif command == 'exit':
                print("Exiting Giggles & Quests. Goodbye!")
                break

            else:
                print("Unknown command. Use 'help' for a list of commands.")

        except KeyboardInterrupt:
            print("\nExiting due to keyboard interrupt.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
