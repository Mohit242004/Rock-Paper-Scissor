# ✊✋✌️ Rock, Paper, Scissor Game

A simple **Python-based Rock, Paper, Scissor Game** where the user competes against the computer. The computer randomly selects its move, and the program determines the winner based on the classic game rules. This project is ideal for beginners to learn **Python fundamentals, conditional statements, random module usage, and user interaction**. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

- 🎮 Play Rock, Paper, Scissor against the computer
- 🤖 Computer generates a random choice
- ⚖️ Automatically determines the winner
- 🤝 Detects tie situations
- 💻 Simple command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Random Module (`random`)
- Lists
- Conditional Statements (`if-elif-else`)
- User Input (`input()`)
- String Formatting (`f-strings`)

---

## 📂 Project Structure

```
Rock-Paper-Scissor/
│
├── Rock, Paper, Scissor.py
└── README.md
```

---

## 🎯 Game Rules

| User Choice | Computer Choice | Result |
|------------|----------------|---------|
| Rock | Rock | Tie |
| Rock | Paper | Paper Wins |
| Rock | Scissor | Rock Wins |
| Paper | Paper | Tie |
| Paper | Rock | Paper Wins |
| Paper | Scissor | Scissor Wins |
| Scissor | Scissor | Tie |
| Scissor | Rock | Rock Wins |
| Scissor | Paper | Scissor Wins |

The program compares the user's choice with the computer's randomly selected choice and displays the appropriate result. :contentReference[oaicite:1]{index=1}

---

## ⚙️ Workflow

1. User enters **Rock**, **Paper**, or **Scissor**.
2. The computer randomly selects one of the three options.
3. Both choices are displayed.
4. The program evaluates the winner using conditional statements.
5. The final result is printed.

---

## ▶️ How to Run

### Step 1: Install Python

Download and install **Python 3.x**.

### Step 2: Clone the Repository

```bash
git clone https://github.com/Mohit242004/Rock-Paper-Scissor.git
```

### Step 3: Navigate to the Project Folder

```bash
cd Rock-Paper-Scissor
```

### Step 4: Run the Program

```bash
python "Rock, Paper, Scissor.py"
```

---

## 📸 Sample Output

### Example 1

```
Enter your move = Rock, Paper, Scissor = Rock

User Choice = Rock
Computer Choice = Scissor

Rock Smashes Scissor = You win
```

---

### Example 2

```
Enter your move = Rock, Paper, Scissor = Paper

User Choice = Paper
Computer Choice = Scissor

Scissor Cuts Paper = Computer win
```

---

### Example 3

```
Enter your move = Rock, Paper, Scissor = Scissor

User Choice = Scissor
Computer Choice = Scissor

Both Choices are Same = Match Tie
```

---

## 📖 Concepts Covered

- Python Lists
- Random Module
- User Input Handling
- Conditional Statements
- Decision Making
- Basic Game Logic

---

## 🚀 Future Improvements

- 🔄 Allow multiple rounds using loops
- 📊 Maintain player and computer scores
- 🏆 Display the overall winner after several rounds
- 🎯 Validate invalid user inputs
- 🎨 Build a graphical interface using Tkinter
- 🌐 Create an online version using Flask or Django
- 👥 Add a two-player mode

---

## 🎯 Learning Outcome

This project helps beginners understand:

- How to generate random values using Python
- How to implement game logic with conditional statements
- How to take and process user input
- How to compare multiple conditions
- How to build a simple interactive console application

---

## 👨‍💻 Author

**Mohit Chaudhari**

If you enjoyed this project, feel free to ⭐ the repository and contribute with new features or improvements!
