from os import system
from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent

pull = input("Do you want to pull? (Y/n) ").lower()

if pull == "y" or pull == "n":
    pull = pull == "y"

else:
    raise ValueError("Type only (Y/n)!!")

if pull:
    system(f"cd {BASE_DIR} && git pull")
    exit(0)

status = input("Do you want to see git status? (Y/n) ").lower()

if status == "y" or status == "n":
    status = status == "y"

else:
    raise ValueError("Type only (Y/n)!!")

if status:
    system(f"cd {BASE_DIR} && git status")

commit_all = input("Commit all files? (Y/N) ").lower()
push = input("Pushing also? (Y/n) ").lower()

if commit_all == "y" or commit_all == "n":
    commit_all = commit_all == "y"

else:
    raise ValueError("Type only (Y/n)!!")

if push == "y" or push == "n":
    push = push == "y"

else:
    raise ValueError("Type only (Y/n)!!")

commit_message = input("Type the commit message: ")

if commit_all:
    system(f"cd {BASE_DIR} && git add .")
    system(f'cd {BASE_DIR} && git commit -m "{commit_message}"')
else:
    file_name = input("Type filename with extension: ")

    system(f"cd {BASE_DIR} && git add {file_name}")
    system(f'cd {BASE_DIR} && git commit -m "{commit_message}"')

if push:
    branch = input("Type the branch name: ")
    system(f"cd {BASE_DIR} && git push -u origin {branch}")
