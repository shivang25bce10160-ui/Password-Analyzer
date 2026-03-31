import string

class PasswordAnalyzer:
    def __init__(self):
        # Configuration as a class attribute for maintainability 
        self.min_length = 10
        self.weightage = {
            "upper": 20, "lower": 20, "digits": 20, "characters": 20,
            "length_bonus": 15, "randomness_bonus": 5,
            "sequence_penalty": -20, "repetition_penalty": -20
        }
        self.symbols = string.punctuation

    def _check_sequence(self, password, seq_length=3):
        """Internal helper to detect keyboard patterns."""
        p_low = password.lower()
        for i in range(len(p_low) - seq_length + 1):
            segment = p_low[i:i+seq_length]
            if segment in string.ascii_lowercase or segment in string.ascii_lowercase[::-1]:
                return True
            digits = "0123456789"
            if segment in digits or segment in digits[::-1]:
                return True
        return False

    def _check_repetition(self, password, max_rep=3):
        """Internal helper to detect character spam."""
        for i in range(len(password) - max_rep + 1):
            segment = password[i:i+max_rep]
            if all(char == segment[0] for char in segment):
                return True
        return False

    def analyze(self, password):
        """Core analysis logic returning score and feedback list."""
        score = 0
        feedback = []
        found = {"upper": False, "lower": False, "digits": False, "characters": False}

        # 1. Type Check
        for char in password:
            if char.isupper(): found["upper"] = True
            elif char.islower(): found["lower"] = True
            elif char.isdigit(): found["digits"] = True
            elif char in self.symbols: found["characters"] = True

        for key, present in found.items():
            if present:
                score += self.weightage[key]
            else:
                feedback.append(f"Missing {key} characters.")

        # 2. Length & Entropy
        length = len(password)
        if length >= self.min_length:
            score += self.weightage["length_bonus"]
        elif length < 6:
            feedback.append("Critical: Password is too short.")

        if len(set(password)) >= length * 0.75 and length >= 8:
            score += self.weightage["randomness_bonus"]

        # 3. Penalties
        if self._check_sequence(password):
            score += self.weightage["sequence_penalty"]
            feedback.append("Penalty: Sequential pattern detected.")
        
        if self._check_repetition(password):
            score += self.weightage["repetition_penalty"]
            feedback.append("Penalty: Repeating characters detected.")

        return score, feedback
