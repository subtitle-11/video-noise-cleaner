import os
import subprocess

def extract_audio(video_path, audio_path):
    subprocess.run(["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path])

def generate_noise_profile(noise_sample, profile_path):
    subprocess.run(["sox", noise_sample, "-n", "noiseprof", profile_path])

def clean_audio(input_audio, output_audio, profile_path):
    subprocess.run(["sox", input_audio, output_audio, "noisered", profile_path, "0.21"])

def combine_audio_video(original_video, cleaned_audio, output_video):
    subprocess.run([
        "ffmpeg", "-i", original_video, "-i", cleaned_audio,
        "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0", output_video
    ])

def main():
    video = "input.mp4"
    extracted_audio = "extracted.wav"
    noise_sample = "noise_sample.wav"
    noise_profile = "noise.prof"
    cleaned_audio = "cleaned.wav"
    output_video = "output_cleaned.mp4"

    print("Extracting audio...")
    extract_audio(video, extracted_audio)

    print("Generating noise profile...")
    generate_noise_profile(noise_sample, noise_profile)

    print("Cleaning audio...")
    clean_audio(extracted_audio, cleaned_audio, noise_profile)

    print("Combining audio and video...")
    combine_audio_video(video, cleaned_audio, output_video)

    print("Done. Output:", output_video)

if __name__ == "__main__":
    main()
