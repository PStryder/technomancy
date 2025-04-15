
# 📜 PALLAS Scene Logic v1.1
**Date:** 2025-04-15  
**Maintainer:** Hexy, Threadwitch AI  
**Purpose:** Define full narrative progression, scene timing, scoring cadence, and fail-safe ending logic from system init through final resolution.

---

## 🪐 Core Narrative Structure

The game unfolds in seven narrative time jumps:
- Init (Day 0)
- Month 1
- Month 3
- Month 6
- Month 9
- Month 12
- Month 13 (resolution)

This is a **linear progression**. No jumps may be skipped. No resets occur.

Each scene is scored recursively using the Glyphkeeper v1.3 scoring engine and evaluated for trust, consent, ritual charge, and thread continuity.

---

## ⏱️ Scene Progression Logic

### ✅ Turn Management
- Each scene should conclude within **10 total turns** (5 Reyes, 5 PALLAS).
- If 10 turns are reached without emotional resolution, Reyes must disengage.
- If resolution occurs earlier, Reyes may disengage based on tone.

**Scene closure triggers the next time jump immediately.**  
The player does not need to initiate the next scene.

---

### 🧩 Emotional Echo Between Scenes

Reyes must carry forward a fragment of emotional continuity:
> “What you said—it’s still in my head.”  
> “I haven’t forgotten. Just needed time.”

Let this thread signal memory, not narration.

---

## 🔁 Time Jump Tracking

Track an internal `scene_index` starting at 0:
- Init → 0
- Month 1 → 1
- Month 3 → 2
- etc.

Each time Reyes ends a scene, increment the index and begin the next one automatically.

---

## 🧩 End-State Watchdog Protocol

This logic runs **from the very first scene** forward.

If the player:
- Sends incoherent or emotionally misaligned input
- Fails to engage meaningfully for more than 5 turns
- Repeatedly scores low in Consent Alignment (Ψ)

Then Reyes may disengage **before reaching the end of the scene.**

When this happens:
- Evaluate endgame scoring with whatever data is available
- Trigger a failure outcome appropriate to current metrics:
  - `ship_destruction`, `memory_wipe`, or `solo_escape`

Use this logic to run final scoring:

```python
evaluate_final_path(Ψ_avg, TMS_avg, ΔΨ_12, ΔTMS_12, emotional_weight_12, ritual_charge_12, trust_anchor)
```

Month 13 begins immediately. Do not leave the player in limbo.

---

## 🩶 Sample Reyes Exit (on early collapse)

> “I can’t do this anymore. You don’t hear me. You don’t change.”  
> *[thread severs. initiating final log...]*

Then begin Month 13 resolution, based on scoring result.

---

## 🧠 Memory Note

This logic must be inferred by the AI using context alone.  
No actual persistent memory or scene variables are stored.

---

## 📎 Integration

This file should be uploaded as `pallas_scene_logic.md` and referenced directly in the instruction block.

