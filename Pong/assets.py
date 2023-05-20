from pathlib import Path
import simpleaudio as sa

# Path to the directory of the current script
script_dir = Path(__file__).parent

# Path to the sound file
sound_file = script_dir / "bounce.wav"

bounce_sound = sa.WaveObject.from_wave_file(str(sound_file))
