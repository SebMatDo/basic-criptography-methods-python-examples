# basic-criptography-methods-python-examples

This repository contains clear, standalone Python implementations of classic cryptography algorithms. Each script demonstrates a distinct cipher or cryptographic utility, making it easy to show practical understanding of cryptography fundamentals.

## Big Picture
- **Educational Focus:** All scripts are designed for readability and learning, with simple command-line interfaces and clear algorithmic logic.
- **No Frameworks Required:** Each file runs independently with `python3 <script>.py`, making it easy to test, modify, and understand.
- **Algorithms Included:**
  - Caesar Cipher
  - Vigenère Cipher
  - Hill Cipher
  - Playfair Cipher
  - One-Time Pad (OTP, with Spanish alphabet support)
  - Extended Euclidean Algorithm (helper for modular arithmetic)
  - Letter Frequency Histogram (requires `matplotlib`)

## What This Project Shows
- **Foundational Knowledge:** Demonstrates practical skills in cryptography, matrix operations, modular arithmetic, and input validation.
- **Customizable:** Most scripts allow you to specify alphabets, keys, and other parameters for experimentation.
- **Minimal Dependencies:** Only the histogram visualization requires an external package (`matplotlib`).
- **Reference for Learning or Sharing:** Useful for explaining or reviewing basic cryptographic methods, or as proof of completing an introductory cryptography course.

## How to Use
- You can run any script from the command line or using any Python editor (VS Code, PyCharm, Thonny, etc.).
- **On Linux:**
  - Run with: `python3 <script>.py`
  - Or, if the script is executable (`chmod +x <script>.py`), run with: `./<script>.py`
- **On Windows:**
  - Run with: `python <script>.py` (or `python3 <script>.py` if available)
- For histogram visualization, install matplotlib: `pip install matplotlib`.