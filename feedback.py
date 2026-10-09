def evaluate(target, guess):
    result = ["gray"] * len(guess)
    target_counts = {}
    for ch in target:
        target_counts[ch] = target_counts.get(ch, 0) + 1
        
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            target_counts[ch] -= 1
            
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if target_counts.get(ch, 0) > 0:
            result[i] = "yellow"
            target_counts[ch] -= 1
            
    return result
