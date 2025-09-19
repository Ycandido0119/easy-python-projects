# Python Projects Collection

A collection of Python projects demonstrating various programming concepts and practical applications. This repository contains 9 different projects ranging from simple calculators to interactive quiz applications.

## 🚀 Projects Overview

### 1. Quiz Application (`quiz_app.py`)
An interactive quiz game with multiple difficulty levels and question management.

**Features:**
- Three difficulty levels: Easy, Medium, Hard
- JSON-based question storage with automatic file creation
- Add custom questions dynamically
- Flexible answer matching (case-insensitive, multiple acceptable answers)
- Score tracking and accuracy calculation
- Review wrong answers after quiz completion
- Random question shuffling

**Usage:**
```bash
python quiz_app.py
```

### 2. Simple Calculator (`calculator.py`)
A command-line calculator that performs basic arithmetic operations.

**Features:**
- Addition, subtraction, multiplication, and division
- Input validation and error handling
- Division by zero protection
- Interactive menu system
- Continuous calculation option

**Usage:**
```bash
python calculator.py
```

### 3. GIF Creator (`create_gif.py`)
Creates animated GIFs from a series of PNG images.

**Features:**
- Combines multiple PNG images into a single GIF
- Customizable duration and loop settings
- Uses imageio library for image processing

**Requirements:**
```bash
pip install imageio
```

**Usage:**
```bash
python create_gif.py
```

### 4. Expense Tracker (`expense_tracker.py`)
A personal finance management tool to track daily expenses.

**Features:**
- Add expenses with categories (Food, Transport, Entertainment, Utilities)
- View expense summaries
- Date range filtering
- CSV data storage
- Input validation

**Requirements:**
```bash
pip install pandas
```

**Usage:**
```bash
python expense_tracker.py
```

### 5. Word Guessing Game (`guess_game.py`)
A fun word guessing game with football team names.

**Features:**
- Random word selection from football teams
- Letter-by-letter guessing mechanism
- Limited attempts (10 tries)
- Visual word progress display
- Win/lose conditions

**Usage:**
```bash
python guess_game.py
```

### 6. QR Code Generator (`qr_code.py`)
Generates QR codes for URLs or text content.

**Features:**
- Creates QR codes from text/URLs
- Customizable size and border settings
- Saves as PNG image
- Black and white color scheme

**Requirements:**
```bash
pip install qrcode[pil]
```

**Usage:**
```bash
python qr_code.py
```

### 7. Roman Numeral Converter (`roman_numerals.py`)
Converts Roman numerals to decimal numbers.

**Features:**
- Supports standard Roman numeral characters (I, V, X, L, C, D, M)
- Simple character-by-character conversion
- Interactive input system

**Usage:**
```bash
python roman_numerals.py
```

### 8. To-Do List Application (`tdl_app.py`)
A simple task management application for organizing daily activities.

**Features:**
- Add new tasks
- View all tasks with numbering
- Delete specific tasks
- Input validation
- Interactive menu system

**Usage:**
```bash
python tdl_app.py
```

### 9. Weather Tracker (`weather_tracker.py`)
Real-time weather information fetcher using OpenWeatherMap API.

**Features:**
- Current weather data for any city
- Temperature in Celsius
- Weather description and conditions
- Error handling for invalid cities
- Multiple city lookup support

**Requirements:**
```bash
pip install requests
```

**Setup:**
You'll need to get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and replace the `api_key` variable in the code.

**Usage:**
```bash
python weather_tracker.py
```

## 📁 Repository Structure

```
├── quiz_app.py          # Interactive quiz application
├── questions.json       # Quiz questions database
├── calculator.py        # Basic arithmetic calculator
├── create_gif.py       # GIF creation from images
├── expense_tracker.py  # Personal expense management
├── guess_game.py      # Word guessing game
├── qr_code.py         # QR code generator
├── roman_numerals.py  # Roman to decimal converter
├── tdl_app.py        # To-do list manager
├── weather_tracker.py # Weather information fetcher
├── imgs/             # Directory for images and generated files
└── README.md         # This file
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd python-projects
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install pandas imageio qrcode[pil] requests
   ```

4. **Create necessary directories:**
   ```bash
   mkdir imgs
   ```

## 🎯 Learning Objectives

These projects demonstrate various Python concepts:

- **Basic Programming:** Variables, functions, loops, conditionals
- **Data Structures:** Lists, dictionaries, strings
- **File I/O:** Reading/writing CSV files, image handling
- **Error Handling:** Try-catch blocks, input validation
- **API Integration:** HTTP requests, JSON parsing
- **Third-party Libraries:** pandas, imageio, qrcode, requests
- **User Interface:** Command-line interfaces, menu systems

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for:
- Bug fixes
- Feature enhancements
- Code optimization
- Additional projects
- Documentation improvements

## 📝 Notes

- Some projects require external libraries - make sure to install dependencies
- The weather tracker requires a valid API key from OpenWeatherMap
- Image files should be placed in the `imgs/` directory for the GIF creator and QR code generator
- Expense data is stored in `expenses.csv` file

## 🔮 Future Enhancements

Potential improvements for these projects:
- GUI interfaces using tkinter or PyQt
- Database integration for data persistence
- Web-based versions using Flask/Django
- Enhanced error handling and logging
- Unit tests for all functions
- Configuration files for settings

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Happy coding! 🐍✨
