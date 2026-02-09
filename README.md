# Expo-Shortner

A simple and efficient URL shortener project, designed to convert long URLs into short, manageable links. This project is built using Python and Flask, providing a clean and intuitive web interface for users to shorten their URLs.

## Features

*   **URL Shortening**: Convert long, cumbersome URLs into concise, easy-to-share links.
*   **Custom Short Codes (Future)**: Option to create custom short codes for personalized links.
*   **Redirection**: Seamlessly redirect users from the shortened URL to the original long URL.
*   **Analytics (Future)**: Basic tracking of click-through rates for shortened URLs.
*   **Simple Interface**: User-friendly web interface for quick URL shortening.

## Technologies Used

*   **Python**: The core programming language.
*   **Flask**: A micro web framework for Python, used for building the web application.
*   **SQLite**: A lightweight, file-based database used for storing URL mappings.
*   **HTML/CSS**: For the front-end user interface.

## Project Structure

```
Expo-Shortner/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── config/
│   └── settings.py
├── templates/
│   ├── index.html
│   └── shortened.html
├── run.py
├── utils.py
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Expo-Shortner.git
    cd Expo-Shortner
    ```
2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application**:
    ```bash
    python run.py
    ```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:5000/`.
2.  Enter a long URL into the provided input field.
3.  Click the "Shorten" button.
4.  A shortened URL will be displayed, which you can then copy and share.

## Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for any bugs, features, or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
