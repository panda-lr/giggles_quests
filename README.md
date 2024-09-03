Giggles & Quests is a text-based story game where players embark on adventures by making choices that shape their story. Developed in Python, this game allows users to start specific stories, choose random stories, and navigate through engaging narratives.

Features

Start Specific Stories: Begin a specific story by selecting its number from the list.
Start Random Story: Randomly select a story to start.
Stop Current Story: Stop the current story and return to the main menu.
List Available Stories: View a list of all available stories.
Help Command: Get information on how to use the game.

Getting Started:

Prerequisites

Python 3.x installed on your system.

Installation

Clone the Repository

git clone https://github.com/yourusername/giggles-and-quests.git

cd giggles-and-quests

Setup Environment
No additional setup is required for this game.

Usage:

Prepare Stories

Place your story files in the stories directory. Each story file should be a JSON file with the following format:

{
  "start": {
    "text": "You find yourself in a dark forest.",
    "choices": {
      "1": {
        "text": "Follow the path",
        "next": "path"
      },
      "2": {
        "text": "Turn back",
        "next": "turn_back"
      }
    }
  },
  "path": {
    "text": "The path leads to a clearing.",
    "choices": {
      "1": {
        "text": "Examine the clearing",
        "next": "clearing"
      },
      "2": {
        "text": "Continue walking",
        "next": "continue_walking"
      }
    }
  },
  "clearing": {
    "text": "You find a hidden treasure!",
    "choices": {}
  },
  "continue_walking": {
    "text": "You keep walking and find your way out of the forest.",
    "choices": {}
  },
  "turn_back": {
    "text": "You turn back and go home.",
    "choices": {}
  }
}

Run the Game

python game.py

Commands
start [story_number]: Start a specific story by number.
start random: Start a random story.
stop: Stop the current story and return to the main menu.
list: List all available stories.
help: Show this help message.
exit: Exit the game.

Contributing
Feel free to fork the repository and submit pull requests. Contributions to improve the game, add new stories, or enhance functionality are welcome!

License
This project is licensed under the GNU General Public License (GPL) v3.0. See the LICENSE file for details.
