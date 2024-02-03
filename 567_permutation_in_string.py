def checkInclusion(s1: str, s2: str) -> bool:
    s1_alphabet, s2_alphabet = {}, {}
    s1_len = len(s1)

    for s in s1:
        s1_alphabet[s] = 1 + s1_alphabet.get(s, 0)

    left = 0
    for i in range(len(s2)):
        s2_alphabet[s2[i]] = 1 + s2_alphabet.get(s2[i], 0)

        if (i - left + 1) < s1_len:
            continue
        else:
            if s1_alphabet == s2_alphabet:
                return True
            
            s2_alphabet[s2[left]] = s2_alphabet[s2[left]] - 1
            if s2_alphabet[s2[left]] == 0: 
                del s2_alphabet[s2[left]]
            
            left += 1

    return False

checkInclusion("ab", "eidbaooo")