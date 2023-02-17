#!/usr/bin/env python3

import argparse
from bashai import ai

def main():
    parser = argparse.ArgumentParser(description="An AI for debugging Bash scripts")
    parser.add_argument("-l", "--learning-mode", action="store_true", help="Enter learning mode")
    parser.add_argument("-d", "--debug-mode", action="store_true", help="Start Bashdb debugger")
    args = parser.parse_args()

    if args.learning_mode:
        ai.learning_mode()
    elif args.debug_mode:
        ai.start_debugger()
    else:
        ai.run()

if __name__ == "__main__":
    main()
