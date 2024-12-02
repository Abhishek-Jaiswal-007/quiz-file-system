import os
import json
import getpass

# File paths
USER_DATA_FILE = "user_data.json"
QUIZ_RESULTS_FILE = "quiz_results.json"

# Questions for each subject
questions = {
    "Python": {
        "What is the output of print(3 ** 2)?": {"a": "6", "b": "9", "c": "8", "d": "5", "answer": "b"},
        "Which of the following is mutable in Python?": {"a": "Tuple", "b": "Dictionary", "c": "String", "d": "Set", "answer": "b"},
        "Which keyword is used to define a class in Python?": {"a": "class", "b": "define", "c": "object", "d": "create", "answer": "a"},
        "What is the correct extension for a Python script?": {"a": ".py", "b": ".pt", "c": ".script", "d": ".pyth", "answer": "a"},
        "What will len('hello') return?": {"a": "4", "b": "5", "c": "6", "d": "Error", "answer": "b"},
        "What is the result of print('Python' * 3)?": {"a": "PythonPythonPython", "b": "Python 3", "c": "Python*3", "d": "Error", "answer": "a"},
        "Which operator is used for modulo operation in Python?": {"a": "//", "b": "%", "c": "/", "d": "^", "answer": "b"},
        "What will print(9 // 4) output?": {"a": "2.25", "b": "3", "c": "2", "d": "Error", "answer": "c"},
        "What does the break statement do in Python?": {"a": "Skips the loop iteration", "b": "Exits the loop entirely", "c": "Restarts the loop", "d": "Continues to the next iteration", "answer": "b"},
        "How can an empty set be created in Python?": {"a": "[]", "b": "set()", "c": "{}", "d": "()", "answer": "b"}
    },
    "DBMS": {
        "What does SQL stand for?": {"a": "Structured Query Language", "b": "Simple Query Language", "c": "Sequential Question Language", "d": "Standard Query Language", "answer": "a"},
        "Which of these is not a type of join in SQL?": {"a": "Left Join", "b": "Right Join", "c": "Inner Join", "d": "Outer Join", "answer": "d"},
        "What is the role of a primary key in a database?": {"a": "Ensures data uniqueness in a table", "b": "Allows duplicate values", "c": "Serves as a foreign reference", "d": "None of the above", "answer": "a"},
        "What does the ORDER BY clause do in SQL?": {"a": "Filters records based on a condition", "b": "Sorts the result set", "c": "Groups the result set", "d": "Joins multiple tables", "answer": "b"},
        "Which of these is an example of a NoSQL database?": {"a": "MySQL", "b": "Oracle", "c": "MongoDB", "d": "PostgreSQL", "answer": "c"},
        "What is the purpose of the HAVING clause in SQL?": {"a": "Filters records before grouping", "b": "Filters records after grouping", "c": "Sorts the grouped data", "d": "Joins multiple tables", "answer": "b"},
        "What is normalization in databases?": {"a": "Increasing the database size", "b": "Reducing redundancy and dependency", "c": "Creating backup copies", "d": "Creating indexes", "answer": "b"},
        "What is the default isolation level for SQL transactions?": {"a": "Read Committed", "b": "Serializable", "c": "Repeatable Read", "d": "Read Uncommitted", "answer": "a"},
        "Which command is used to delete data in a table in SQL?": {"a": "DELETE", "b": "REMOVE", "c": "ERASE", "d": "DROP", "answer": "a"},
        "What is an index in a database?": {"a": "A backup of a table", "b": "A tool for speeding up data retrieval", "c": "A foreign key", "d": "None of the above", "answer": "b"}
    },
    "DSA": {
        "Which data structure follows the FIFO (First In, First Out) principle?": {"a": "Stack", "b": "Queue", "c": "Linked List", "d": "Array", "answer": "b"},
        "What is the time complexity of finding an element in an unsorted list?": {"a": "O(log n)", "b": "O(n)", "c": "O(n^2)", "d": "O(1)", "answer": "b"},
        "Which traversal technique is used in Depth-First Search (DFS) for a graph?": {"a": "Level Order", "b": "Post-Order", "c": "Pre-Order", "d": "In-Order", "answer": "c"},
        "What is the time complexity of Quick Sort in the worst case?": {"a": "O(n log n)", "b": "O(n^2)", "c": "O(log n)", "d": "O(n)", "answer": "b"},
        "Which data structure is used to implement breadth-first search (BFS)?": {"a": "Stack", "b": "Queue", "c": "Linked List", "d": "Heap", "answer": "b"},
        "What is the space complexity of a recursive function using a stack?": {"a": "O(1)", "b": "O(n)", "c": "O(log n)", "d": "O(n^2)", "answer": "b"},
        "Which of the following sorting algorithms is not stable?": {"a": "Merge Sort", "b": "Quick Sort", "c": "Bubble Sort", "d": "Insertion Sort", "answer": "b"},
        "Which data structure is ideal for implementing a hash table?": {"a": "Stack", "b": "Queue", "c": "Array", "d": "Hash Map", "answer": "d"},
        "What is the time complexity of accessing an element in an array?": {"a": "O(1)", "b": "O(n)", "c": "O(log n)", "d": "O(n^2)", "answer": "a"},
        "Which of these is a divide and conquer algorithm?": {"a": "Merge Sort", "b": "Linear Search", "c": "Selection Sort", "d": "Insertion Sort", "answer": "a"}
    }
}


# Utility functions to interact with the file system
def load_data(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump(default_data, file)
    with open(file_path, "r") as file:
        return json.load(file)

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Load user data and quiz results
user_data = load_data(USER_DATA_FILE, {})
quiz_results = load_data(QUIZ_RESULTS_FILE, {})

# Registration function
def register():
    print("\n--- Register ---")
    username = input("Enter your username: ")
    if username in user_data:
        print("Username already exists. Please try again.")
        return
    password = getpass.getpass("Enter your password: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    user_data[username] = {"password": password, "email": email, "age": age}
    save_data(USER_DATA_FILE, user_data)
    print("Registration successful!")

# Login function
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in user_data and user_data[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Quiz function
def take_quiz(username):
    print(f"\nWelcome {username}! Choose a subject:")
    for i, subject in enumerate(questions.keys()):
        print(f"{i + 1}. {subject}")
    subject_choice = int(input("Enter your choice (1/2/3): "))
    subject = list(questions.keys())[subject_choice - 1]

    print(f"\nStarting {subject} Quiz!")
    score = 0
    for i, (question, options) in enumerate(questions[subject].items(), start=1):
        print(f"\nQ{i}: {question}")
        for key, option in options.items():
            if key != "answer":
                print(f"  {key}) {option}")
        user_answer = input("Enter your answer (a/b/c/d): ").lower()
        if user_answer == options["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {options['answer']}) {options[options['answer']]}")

    # Save quiz results to file
    percentage = (score / len(questions[subject])) * 100
    result = {"subject": subject, "score": score, "total": len(questions[subject]), "percentage": percentage}
    if username not in quiz_results:
        quiz_results[username] = []
    quiz_results[username].append(result)
    save_data(QUIZ_RESULTS_FILE, quiz_results)

    print(f"\nQuiz finished! Your score: {score}/{len(questions[subject])}")
    print(f"Percentage: {percentage:.2f}%")

# Main function
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. View Results")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                take_quiz(username)
        elif choice == "3":
            print("\n--- Quiz Results ---")
            for user, results in quiz_results.items():
                print(f"\nUser: {user}")
                for result in results:
                    print(f"  Subject: {result['subject']}, Score: {result['score']}/{result['total']}, Percentage: {result['percentage']:.2f}%")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

#if _name_ == "_main_":
main()