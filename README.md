# Tunly

Voice-first song recognition web app built with Django. Tunly listens through your microphone and identifies the track using a local matcher. It can handle music playback and humming without extra setup.

## Features

- Microphone-based recognition
- Simple, modern UI with a one-tap record button
- Result card with artwork, title and artist

## Requirements

- Python 3.8+
- pip
- ffmpeg and ffprobe available on PATH (used for audio handling)

You can get ffmpeg from `https://ffmpeg.org` or via package managers.

## Quick start

```bash
pip install -r requirements.txt
python manage.py migrate  # first run only
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and click the record button to identify a song or hum a melody.

## Configuration (optional)

No configuration is required. Tunly will work out of the box with the built‑in matcher. Tunly can auto-detect it and try to leverage it if compatible, falling back gracefully if not.

## Project structure

- `Tunly/` – Django project settings and URLs
- `one/` – Main app (views, templates, static assets, matching core)
  - `templates/index.html` – UI shell
  - `static/one/js/script.js` – recording, UI interactions
  - `core/` – matching helpers

## How it works

1) Record
- The browser captures ~8 seconds of mono audio using MediaRecorder and sends it to the Django endpoint (`one/static/one/js/script.js`).

2) Condition
- The server converts the upload to 16 kHz, mono PCM using pydub (`one/getSong.py`). This reduces size and standardizes input.

3) Fingerprint (signature)
- A compact acoustic signature is generated from the samples by `SignatureGenerator` (`one/core/algorithm.py`). The signature encodes time‑frequency landmarks that are robust to noise and small timing shifts.

4) Match
- The signature is serialized and sent to Shazam’s discovery endpoint (`one/core/communication.py`). Shazam returns likely matches for that signature.

5) Display
- The UI renders title, artist, and artwork; Spotify/YouTube search links can be shown for convenience (`one/templates/index.html`).

## Development tips

- If you change audio duration or thresholds, see:
  - `one/static/one/js/script.js` – recording duration
  - `one/getSong.py` – audio preprocessing and matching parameters

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

Issues and pull requests are welcome. Please open an issue to discuss substantial changes before submitting a PR.

## About the author

Hi, I’m Mohamed Abdelhakeem — a backend engineer. I enjoy building reliable services, clean APIs, and performance‑minded systems. This project combines practical audio processing with a simple, user‑friendly Django app. If you have ideas to improve it or want to collaborate, feel free to open an issue or PR.