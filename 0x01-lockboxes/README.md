# Interview Question: Lockboxes

## Overview

This directory contains a solution to the "Lockboxes" interview question. The problem is a classic example of using algorithms to solve puzzles involving keys and boxes. Each box may contain keys to other boxes. The goal is to determine if all boxes can be unlocked starting from the first box, which is initially unlocked.

## Problem Statement

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a function that determines if all the boxes can be unlocked. The first box (`box 0`) is unlocked. A box can be unlocked if one of the previously unlocked boxes contains a key to it. In other words, you need to check if there's a way to unlock all boxes given the keys you find along the way.

## Solution

The solution provided in this repository uses a straightforward approach to solve the problem. It iterates through each box, starting with the first one, and collects keys found in unlocked boxes. It keeps track of which boxes can be unlocked with the keys found so far. The algorithm ensures that it only attempts to unlock a box if it hasn't been unlocked already.

## How to Run

To run the solution, ensure you have Python installed on your system. You can run the script from the terminal as follows:

```bash
python lockboxes.py