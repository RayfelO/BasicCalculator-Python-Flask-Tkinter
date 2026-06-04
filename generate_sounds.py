import math
import os
import struct
import wave


def generate_sound(filename, duration, sample_rate, sound_func):
    n_samples = int(sample_rate * duration)
    amplitude = 32767

    with wave.open(filename, "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        for i in range(n_samples):
            t = i / sample_rate
            sample = sound_func(t, duration, sample_rate)
            sample = max(-1.0, min(1.0, sample))
            wav.writeframes(struct.pack("h", int(sample * amplitude)))


def envelope(t, duration, attack=0.01, release=0.1):
    if t < attack:
        return t / attack
    if t > duration - release:
        return (duration - t) / release
    return 1.0


def click_sound(t, duration, sample_rate):
    noise = (hash(str(int(t * sample_rate))) % 1000 - 500) / 500.0
    env = envelope(t, duration, attack=0.001, release=0.05)
    return noise * env * 0.5


def hover_sound(t, duration, sample_rate):
    freq = 600.0 + 200.0 * (t / duration)
    env = envelope(t, duration, attack=0.05, release=0.1)
    return math.sin(2 * math.pi * freq * t) * env * 0.3


def error_sound(t, duration, sample_rate):
    freq = 300.0 - 150.0 * (t / duration)
    env = envelope(t, duration, attack=0.01, release=0.1)
    return math.sin(2 * math.pi * freq * t) * env * 0.4


def success_sound(t, duration, sample_rate):
    freq1 = 523.25
    freq2 = 659.25
    freq3 = 783.99
    env = envelope(t, duration, attack=0.01, release=0.2)
    if t < duration * 0.33:
        freq = freq1
    elif t < duration * 0.66:
        freq = freq2
    else:
        freq = freq3
    return math.sin(2 * math.pi * freq * t) * env * 0.3


if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "assets", "sounds")
    os.makedirs(out_dir, exist_ok=True)
    sample_rate = 44100

    generate_sound(
        os.path.join(out_dir, "button_click.wav"), 0.08, sample_rate, click_sound
    )
    generate_sound(
        os.path.join(out_dir, "button_hover.wav"), 0.15, sample_rate, hover_sound
    )
    generate_sound(
        os.path.join(out_dir, "button_error.wav"), 0.3, sample_rate, error_sound
    )
    generate_sound(
        os.path.join(out_dir, "button_success.wav"), 0.4, sample_rate, success_sound
    )

    print("Sounds generated successfully in", out_dir)
