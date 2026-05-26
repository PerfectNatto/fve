from mido import MidiFile

INPUT = "input.mid"
OUTPUT = "output_480.mid"

TARGET_TPQN = 480

mid = MidiFile(INPUT)

old_tpqn = mid.ticks_per_beat

if old_tpqn <= 0:
    raise ValueError("SMPTE time division のMIDIかもしれません。TPQN形式ではありません。")

print("old ticks_per_beat:", old_tpqn)
print("new ticks_per_beat:", TARGET_TPQN)

def scale_track_delta_times(track, old_tpqn, new_tpqn):
    old_abs = 0
    new_prev_abs = 0

    for msg in track:
        old_abs += msg.time

        # 絶対tick位置をスケールしてから、delta timeに戻す
        # 960 -> 480なら実質 half
        new_abs = (old_abs * new_tpqn + old_tpqn // 2) // old_tpqn

        msg.time = new_abs - new_prev_abs
        new_prev_abs = new_abs

for track in mid.tracks:
    scale_track_delta_times(track, old_tpqn, TARGET_TPQN)

mid.ticks_per_beat = TARGET_TPQN
mid.save(OUTPUT)

print("saved:", OUTPUT)
