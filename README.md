# Aqua Frenzy 🐟🫧

A 2D Feeding-Frenzy‑style game built with PyGame + PyOpenGL.

## Overview

Aqua Frenzy is a lightweight, arcade‑style underwater game inspired by Feeding Frenzy. You control a fish that follows the mouse. Eat smaller fish to grow, collect bubbles and stars for points, and grab extra‑life pickups to survive. But beware—larger fish can eat you! As you grow, the game ramps up difficulty by spawning fish faster and making them swim quicker.

This project is designed as a learning demo for:

* Immediate‑mode OpenGL 2D rendering through PyOpenGL

* Integrating PyGame for windowing, events, input, audio, and image loading

* Drawing everything from basic primitives (triangles, quads, ellipses, bezier curves)

* Custom colliders (ellipse‑ellipse & ellipse‑circle) for simple gameplay physics

## Screenshots

<img width="2385" height="1482" alt="Screenshot 2025-07-16 231811" src="https://github.com/user-attachments/assets/39fcd11a-c1cb-4e41-8a7c-57cb9d1996e3" />
<img width="2396" height="1479" alt="Screenshot 2025-07-16 231439" src="https://github.com/user-attachments/assets/e0a0daeb-5222-4f2e-94fc-c40ae934941f" />
<img width="2388" height="1481" alt="Screenshot 2025-07-16 231531" src="https://github.com/user-attachments/assets/64c0458a-7b50-48e2-9848-a59b4b5c147a" />

## Gameplay Summary

* Move your mouse; your fish follows with easing (lag motion).

* Eat smaller fish → gain size + score.

* Hit larger fish → lose a life (unless immune).

* Pick up bubbles, stars, extra lives drifting vertically.

* Level up when your fish reaches a growth threshold:

  - Score bonus

  - Size resets to initial baseline (keeps scale readable)

  - Global fish speed increases (increases difficulty)

  - Spawn interval shortens (more traffic)

If you lose all lives: you're met with the GAME OVER screen with final score and restart prompt.

## Scoring & Leveling

* Eat fish smaller than you

* Collect bubbles: +1

* Collect stars: +10

* Extra Life: lives +1`

* Level Up trigger: when player size exceeds 1.05 of current scale.

  - +100 bonus score

  - Player size resets to Player.initial_size

  - Fish.speed_multiplier *= 1.1 (capped at 5)

  - Fish spawn rate reduced by 20% (floor: 1000 ms)


## Installation

### 1. Clone repo

```
git clone https://github.com/<your-username>/aqua-frenzy.git 
cd aqua-frenzy
```

### 2. Create virtual environment (recommended)
```
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# or
.venv\Scripts\activate      # Windows PowerShell
```

### 3. Install dependencies

`pip install pygame PyOpenGL PyOpenGL_accelerate`

Audio files are MP3 — ensure your pygame install supports mixer playback for them.

## Running the Game

`python aqua_frenzy.py`

Ensure assets/ folder (background + audio + optional screenshot) is present in the same directory as the script, or adjust the assets_path in main().
