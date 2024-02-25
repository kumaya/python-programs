
def isPalindrome(s):
    return s[:] == s[::-1]

def longestPalindrome(s):
    if isPalindrome(s):
        return s
    start = 0
    window = 1
    for i in range(1, len(s)):
        if i-window>=0 and isPalindrome(s[i-window:i+1]):
            start = i - window
            window += 1
        elif i-window>=1 and isPalindrome(s[i-window-1:i+1]):
            start = i - window - 1
            window += 2
    return s[start:start+window]

def longestPalindrome2(s):
    ls = len(s)
    maxLength = 1
    res = s[0]
    for i in range(0, ls):
        for j in range(0, i+1):
            if s[i-j:i+j] == s[i-j:i+j][::-1] and maxLength < len(s[i-j:i+j]):
                maxLength = len(s[i-j:i+j])
                res = s[i-j:i+j]
                # print(s[i-j:i+j])
            elif s[i-j:i+j+1] == s[i-j:i+j+1][::-1] and maxLength < len(s[i-j:i+j+1]):
                maxLength = len(s[i-j:i+j+1])
                res = s[i-j:i+j+1]
                # print(s[i-j:i+j+1])
    return maxLength, res

def longestPalindrome3(s):
    res = s[0]
    # for odd length palindrome
    for ax in range(1, len(s)):
        orb = 1 
        leng = 1
        while ax - orb >= 0 and ax + orb < len(s):
            if s[ax-orb] == s[ax+orb]:
                orb += 1
                leng += 2
            else:
                break
            if len(res) < leng:
                si = ax-leng//2
                res = s[si:si+leng]

    # even length palindrome
    for ax in range(0, len(s)-1):
        orb = 1
        leng = 0
        while ax-orb+1 >= 0 and ax+orb < len(s):
            if s[ax-orb+1] == s[ax+orb]:
                orb += 1
                leng += 2
            else:
                break
            if len(res) < leng:
                si = (ax-leng//2) + 1
                res = s[si:si+leng]

    return res



if __name__ == "__main__":
    print(longestPalindrome("adbabad"))
    print(longestPalindrome("tscvrnsnnwjzkynzxwcltutcvvhdivtmcvwdiwnbmdyfdvdiseyxyiiurpnhuuufarbwalzysetxbaziuuywugfzzmhoessycogxgujmgvnncwacziyybryxjagesgcmqdryfbofwxhikuauulaqyiztkpgmelnoudvlobdsgharsdkzzuxouezcycsafvpmrzanrixubvojyeuhbcpkuuhkxdvldhdtpkdhpiejshrqpgsoslbkfyraqbmrwiykggdlkgvbvrficmiignctsxeqslhzonlfekxexpvnblrfatvetwasewpglimeqemdgdgmemvdsrzpgacpnrbmomngjpiklqgbbalzxiikacwwzbzapqmatqmexxqhssggsyzpnvvpmzngtljlrhrjbnxgpcjuokgxcbzxqhmitcxlzfehwfiwcmwfliedljghrvrahlcoiescsbupitckjfkrfhhfvdlweeeverrwfkujjdwtcwbbbbwctwdjjukfwrreveeewldvfhhfrkfjkctipubscseioclharvrhgjldeilfwmcwifwhefzlxctimhqxzbcxgkoujcpgxnbjrhrljltgnzmpvvnpzysggsshqxxemqtamqpazbzwwcakiixzlabbgqlkipjgnmombrnpcagpzrsdvmemgdgdmeqemilgpwesawtevtafrl"))
    print(longestPalindrome("forgeeksskeegfor"))
    print(longestPalindrome("geeks"))

    print(longestPalindrome2("adbabad"))
    print(longestPalindrome2("tscvrnsnnwjzkynzxwcltutcvvhdivtmcvwdiwnbmdyfdvdiseyxyiiurpnhuuufarbwalzysetxbaziuuywugfzzmhoessycogxgujmgvnncwacziyybryxjagesgcmqdryfbofwxhikuauulaqyiztkpgmelnoudvlobdsgharsdkzzuxouezcycsafvpmrzanrixubvojyeuhbcpkuuhkxdvldhdtpkdhpiejshrqpgsoslbkfyraqbmrwiykggdlkgvbvrficmiignctsxeqslhzonlfekxexpvnblrfatvetwasewpglimeqemdgdgmemvdsrzpgacpnrbmomngjpiklqgbbalzxiikacwwzbzapqmatqmexxqhssggsyzpnvvpmzngtljlrhrjbnxgpcjuokgxcbzxqhmitcxlzfehwfiwcmwfliedljghrvrahlcoiescsbupitckjfkrfhhfvdlweeeverrwfkujjdwtcwbbbbwctwdjjukfwrreveeewldvfhhfrkfjkctipubscseioclharvrhgjldeilfwmcwifwhefzlxctimhqxzbcxgkoujcpgxnbjrhrljltgnzmpvvnpzysggsshqxxemqtamqpazbzwwcakiixzlabbgqlkipjgnmombrnpcagpzrsdvmemgdgdmeqemilgpwesawtevtafrl"))
    print(longestPalindrome2("forgeeksskeegfor"))
    print(longestPalindrome2("geeks"))

    print(longestPalindrome3("adbabad"))
    print(longestPalindrome3("tscvrnsnnwjzkynzxwcltutcvvhdivtmcvwdiwnbmdyfdvdiseyxyiiurpnhuuufarbwalzysetxbaziuuywugfzzmhoessycogxgujmgvnncwacziyybryxjagesgcmqdryfbofwxhikuauulaqyiztkpgmelnoudvlobdsgharsdkzzuxouezcycsafvpmrzanrixubvojyeuhbcpkuuhkxdvldhdtpkdhpiejshrqpgsoslbkfyraqbmrwiykggdlkgvbvrficmiignctsxeqslhzonlfekxexpvnblrfatvetwasewpglimeqemdgdgmemvdsrzpgacpnrbmomngjpiklqgbbalzxiikacwwzbzapqmatqmexxqhssggsyzpnvvpmzngtljlrhrjbnxgpcjuokgxcbzxqhmitcxlzfehwfiwcmwfliedljghrvrahlcoiescsbupitckjfkrfhhfvdlweeeverrwfkujjdwtcwbbbbwctwdjjukfwrreveeewldvfhhfrkfjkctipubscseioclharvrhgjldeilfwmcwifwhefzlxctimhqxzbcxgkoujcpgxnbjrhrljltgnzmpvvnpzysggsshqxxemqtamqpazbzwwcakiixzlabbgqlkipjgnmombrnpcagpzrsdvmemgdgdmeqemilgpwesawtevtafrl"))
    print(longestPalindrome3("forgeeksskeegfor"))
    print(longestPalindrome3("geeks"))
    print(longestPalindrome3("a"))
