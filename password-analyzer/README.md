# Password Strength Analyzer

A Python-based utility to analyze password strength, detect weaknesses,
and recommend secure password practices.

## Features
- Rule-based password scoring
- Weak pattern detection
- Actionable security suggestions
- Modular code structure

## Project Structure

password-analyzer/

├── main.py          # CLI interface and program loop  
├── analyzer.py      # Core password analysis logic  
├── utils.py         # Helper functions for character checks  
├── patterns.py      # Common weak password patterns  
├── README.md  

## How It Works

1. The user enters a password.
2. The analyzer checks:
   - Minimum length
   - Use of uppercase and lowercase letters
   - Use of digits and special characters
   - Presence of common weak patterns
3. A strength rating is generated.
4. Suggestions are displayed if weaknesses are found.
5. The program continues running until the user presses the ESC key.

## Usage

Run the application using:
```bash
python main.py
```
## Note
This project is a basic educational implementation.
Real-world password validation involves hashing, entropy calculation,
and breach-database checks.
