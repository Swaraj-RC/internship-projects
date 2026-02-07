# Keystroke Logger Tool 

## Overview
This project is a **keystroke logger demonstration tool** written in
**pure Python using only the standard library**.

It is intentionally designed to capture keystrokes **only when its own
console window is focused**, making it safe, visible, and ethical.

## Why This Exists
Many users underestimate how keystrokes can be observed by software.
This demo helps explain that risk **without using any malicious techniques**.

## Key Design Decisions

### 1. Single-Window Capture Only
This tool reads input exclusively from its own terminal window.
It does NOT:
- Capture global keystrokes
- Hook OS-level input
- Run in the background
- Log data to disk

This limitation is **intentional** and aligns with ethical security practices.

### 2. No External Libraries
- Uses only Python standard library (`msvcrt`)
- No third-party packages
- No OS hooks
- No persistence

## Platform
- Windows only

(Linux/macOS require different low-level input handling.)

## Usage
```bash
python keystroke_visualizer.py
