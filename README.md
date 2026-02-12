📝 Django To-Do Web Application

A web-based to-do application built using Django, designed to help users manage recurring tasks efficiently. The application focuses on clean authentication flow and flexible task repetition logic.

🚀 Features

User authentication (login & logout)

Secure user-specific task management

Create and manage tasks with different recurrence types:

Daily

Weekly

Monthly

Yearly

Mark tasks as completed

Tasks are visible only to the logged-in user

Clean handling of date, month, and year changes

🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (default Django DB)

Frontend: HTML, CSS (Django Templates)

Authentication: Django built-in authentication system

📌 Project Status

This is the basic version of the project.

Planned Enhancements:

User dashboard

Productivity efficiency tracking

Improved UI/UX

Task analytics (weekly/monthly overview)

🧠 Key Learning Outcomes

Django authentication and user management

One-to-many relationship between users and tasks

Handling recurring tasks using rule-based logic

Date and time logic across days, months, and years

Clean backend design and separation of concerns

📂 How It Works (High Level)

Each task is stored as a recurrence rule (daily, weekly, etc.)

Tasks are filtered dynamically based on the current date

Task completion is tracked using completion history instead of duplicating tasks

This approach avoids issues with month/year changes and keeps the system scalable

🤝 Feedback

Feedback and suggestions are welcome to help improve the project further.
Feel free to open an issue or share your thoughts.

📄 License

This project is for learning and educational purposes.
